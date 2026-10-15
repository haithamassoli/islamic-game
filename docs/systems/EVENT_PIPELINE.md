# سجل القرارات وخط المعالجة (Event Pipeline)

المرجع: [PRD 7.1](../PRD.md) (FR-E1..E7)، [TECHNICAL_ARCHITECTURE 4.1–4.2](../TECHNICAL_ARCHITECTURE.md)، القرارات D-002، D-004، D-011 في [DECISIONS](../../planning/DECISIONS.md).

## المسؤوليات
- بناء كل حدث وإعطاؤه `seq = nextSeq++` فريداً لا يتكرر حتى بعد التحميل (FR-E2).
- تنفيذ خطوات FR-E4 بالترتيب، متزامنة في الإطار نفسه: البناء ← الشهود (`Perception`) ← الآثار المادية (`EconomyLedger`) ← الإلحاق ← المعالجات 5.1–5.6 ← `OnRecorded`.
- السجل إلحاقي فقط (FR-E1): `GameEvent` غير قابل للتعديل بعد الخطوة 4.
- طابور المتابعة FIFO للأحداث التي تصدرها المعالجات أثناء المعالجة (لا re-entrancy).
- طابور الأحداث المؤجلة `ScheduledEventQueue` (FR-E5): العنصر يُحذف في خطوة البناء نفسها التي يُنفَّذ فيها.
- منع التكرار (FR-E7): تخطي المعالج لأي `seq <= LastProcessedSeq`، وتحديث المؤشر بعد نجاحه.
- إعلان النقطة الآمنة للحفظ (`IsProcessing=false`، FR-S3).
- النواة الحتمية: `GameClock` بخطوة دقيقة واحدة، و`RngStreams` بتيارات مسماة (D-011).

## البيانات التي يمتلكها
- `DecisionLogState { nextSeq, events[] }` (المخطط في [DATA_ARCHITECTURE](../DATA_ARCHITECTURE.md)).
- `ScheduledQueueState { nextScheduledId, items[] }`، و`ScheduledEvent { id, dueTime, payload }`.
- `ClockState { day, minute }`، و`RngState { streams: { name → state } }`.
- `LastProcessedSeq` لكل معالج يملكه المعالج نفسه ويُكتب في قسمه من اللقطة.

## الواجهة العامة
```csharp
public interface ISimulationHandler {          // الواجهة المشتركة الوحيدة للمعالجات
    string HandlerId { get; }                  // "memory", "moral", ...
    long LastProcessedSeq { get; set; }        // يكتبه DecisionLog فقط بعد Handle
    void Handle(GameEvent e);
}
public sealed class DecisionLog {
    public DecisionLog(GameClock clock, Perception perception, EconomyLedger economy,
                       ISimulationHandler[] orderedHandlers, DecisionLogState state);
    public long NextSeq { get; }
    public bool IsProcessing { get; }
    public IReadOnlyList<GameEvent> Events { get; }
    public GameEvent Get(long seq);
    public long Submit(GameEventDraft draft);  // أثناء المعالجة: يُضاف لطابور المتابعة ويُرجع seq المحجوز
    public event Action<GameEvent> OnRecorded; // عرض فقط
}
public sealed class ScheduledEventQueue {
    public string Schedule(GameTime due, GameEventDraft payload);
    public IReadOnlyList<ScheduledEvent> PopDue(GameTime now);   // ترتيب (dueTime, id)
    public bool Cancel(string id);
}
public sealed class GameClock { public GameTime Now { get; } public void Advance(); public bool IsRumorTick { get; } }
public sealed class RngStreams { public SeededRng Get(string streamName); }
```

## الأحداث التي يستقبلها ويصدرها
- **يستقبل** مسودات من: `TradeService`، و`YarnSimulationBridge`، و`ScheduledEventQueue` المستحقة (عبر `SimulationWorld.Step`)، و`RepentanceHandler` (`RELAPSE`)، و`SchedulingHandler` (`CONSEQUENCE` الفوري)، و`StoryState`.
- **يصدر** كل `GameEventType` (القائمة في [DATA_ARCHITECTURE](../DATA_ARCHITECTURE.md))، ثم `OnRecorded(GameEvent)` في الخطوة 6.
- ترتيب المعالجات مكتوب في `SimulationWorld` كمصفوفة ثابتة: `memory → moral → repentance → relationships → scheduling → story`. إضافة معالج = تعديل هذه المصفوفة في مهمة مستقلة مع اختبار ترتيب.

## الاعتمادات
`Perception` (استدعاء مباشر، الخطوة 2)، `EconomyLedger` (الخطوة 3)، المعالجات الست عبر `ISimulationHandler`. لا يعتمد على Runtime.

## الملفات البرمجية المقترحة
- `unity/Assets/_Project/Scripts/Simulation/Core/`: `GameClock.cs`، `GameTime.cs`، `SeededRng.cs`، `RngStreams.cs`، `GameEvent.cs`، `GameEventDraft.cs`، `GameEventType.cs`، `DecisionLog.cs`، `ISimulationHandler.cs`، `ScheduledEventQueue.cs`، `SimulationWorld.cs`.
- `unity/Assets/_Project/Tests/EditMode/Core/`: `GameClockTests.cs`، `SeededRngTests.cs`، `DecisionLogPipelineTests.cs`، `HandlerIdempotencyTests.cs`، `ScheduledEventQueueTests.cs`.

## الاختبار المنفرد
- معالجات وهمية تسجّل ترتيب استدعائها: الترتيب ثابت مهما كان ترتيب الإنشاء.
- `seq` متزايد بلا فجوات، ولا يتكرر بعد استعادة `nextSeq` من لقطة.
- تعديل `GameEvent` بعد الإلحاق غير ممكن (خصائص للقراءة فقط ومصفوفات منسوخة).
- `Submit` من داخل معالج: يُعالج بعد انتهاء الحدث الحالي بكامل خطواته، و`IsProcessing` يبقى `true` حتى فراغ الطابور.
- FR-E7: إعادة تمرير حدث قديم لا تغيّر الحالة.
- `SeededRng`: البذرة نفسها تعطي التسلسل نفسه، واستعادة الحالة تكمل التسلسل نفسه؛ التيارات مستقلة.
- الحدث المؤجل يُنفَّذ مرة واحدة (أساس T4)، وترتيب (`dueTime`، `id`) ثابت.

## حفظ الحالة (FR-S1)
يُحفظ: `nextSeq`، والسجل كاملاً، وطابور المؤجلات مع `nextScheduledId`، وزمن اللعبة، وحالة كل تيار عشوائي، و`lastProcessedSeq` لكل معالج. لا يُحفظ طابور المتابعة لأنه فارغ دائماً عند النقطة الآمنة. التحميل استعادة لا إعادة تنفيذ (FR-S2): لا يُطلق `OnRecorded` للأحداث المستعادة. التفاصيل: [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- نوع حدث جديد = قيمة enum تُحفظ نصاً + صفوف في جداول القواعد، دون تغيير الخط.
- عند تضخم السجل في جلسات طويلة: ضغط الأحداث القديمة غير الأخلاقية (مثل المشتريات: `TRADE_HONEST` بوسم `purchase`) في ملخص، بقرار جديد وبعد قياس ([PERFORMANCE_TARGETS](../PERFORMANCE_TARGETS.md)).

## المهام المرتبطة
[TASK-M01-006](../../tasks/M01/TASK-M01-006.md)، [TASK-M01-007](../../tasks/M01/TASK-M01-007.md)، [TASK-M01-008](../../tasks/M01/TASK-M01-008.md)، [TASK-M01-009](../../tasks/M01/TASK-M01-009.md)، [TASK-M01-010](../../tasks/M01/TASK-M01-010.md)، [TASK-M01-011](../../tasks/M01/TASK-M01-011.md)، [TASK-M02-012](../../tasks/M02/TASK-M02-012.md)، [TASK-M06-006](../../tasks/M06/TASK-M06-006.md).
