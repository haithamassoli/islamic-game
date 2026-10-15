# العواقب وأحداث الحياة (Consequences & Life Events)

المرجع: [PRD 7.8](../PRD.md) (FR-K1..K4)، وFR-E3، وFR-E5، والمسألة SR-09.

## المسؤوليات
- **المعالج 5.5 `SchedulingHandler`:** يقرأ الحدث الجديد والمعتقدات التي أنشأتها له الذاكرة، ويقرر بالقواعد:
  - **عواقب سببية** (FR-K1): انكشاف ← فقدان زبائن ← مطالبة بتعويض ← امتناع مورد. كل عاقبة حدث `CONSEQUENCE` بـ `causeEventIds` حقيقية (FR-E3)، فورية عبر `Log.Submit` أو مؤجلة عبر `ScheduledEventQueue`.
  - **أحداث مؤجلة:** `CONSEQUENCE` بوسم `victim_discovery` (وزن الضحية في البيت، FR-P2)، ومغادرة تاجر القافلة `NPC_DEPARTED` (F8)، والمطالبة بالتعويض بعد مهلة.
- **أحداث الحياة** (FR-K2): `LifeEvents.RollDay()` عند بداية كل يوم يجدول سرقة أو مرضاً أو تلف بضاعة أو مصروفاً مفاجئاً بمعدل **واحد لكل اللاعبين** (تيار `life`)، **بلا `causeEventIds`**، ونوعها دائماً `LIFE_EVENT` (أو `THEFT_VICTIM` للسرقة).
- FR-K3: لا يوجد نوع بيانات اسمه عقوبة. التأويل في سطور الضمير فقط وبصيغة تأملية (FR-C6).
- FR-K4: ربط معدل أحداث الحياة أو نفقات المال الحرام بالسجل الأخلاقي **معطل** حتى حسم SR-09. لا يُمرر `MoralLedger` إلى `LifeEvents` أصلاً (الاعتماد غير موجود في المُنشئ)، فلا يمكن تفعيله بالخطأ.

## البيانات التي يمتلكها
- لا حالة خاصة سوى `lastProcessedSeq`؛ العواقب المعلقة تعيش في `ScheduledEventQueue` (محفوظ في النواة).
- `LifeEventsState { lastRolledDay }` لمنع اللف المزدوج لليوم نفسه بعد التحميل.
- جداول: `Content/Rules/consequence_rules.json` (شرط ← عاقبة، تأخير، احتمال بالألف)، `Content/Rules/life_events.json` (الأنواع والمعدل الواحد والأثر المادي).

## الواجهة العامة
```csharp
public sealed class SchedulingHandler : ISimulationHandler {     // HandlerId = "scheduling"
    public SchedulingHandler(DecisionLog log, ScheduledEventQueue queue, MemoryStore memory,
                             Reputation reputation, ConsequenceRules rules, RngStreams rng);
}
public sealed class LifeEvents {
    public LifeEvents(ScheduledEventQueue queue, LifeEventRules rules, RngStreams rng);  // لا MoralLedger
    public void RollDay(GameTime dayStart);                       // تيار "life"
}
```

## الأحداث التي يستقبلها ويصدرها
- **يستقبل (5.5):** `CHEAT_*` و`FALSE_DESCRIPTION` (جدولة `CONSEQUENCE` بوسم `victim_discovery` حسب نوع الغش وفحص الزبون)، `CONSEQUENCE` بوسم `victim_discovery` (عواقب الانكشاف)، `ACCUSED`، `CLEARED` (إلغاء عواقب معلقة عبر `Cancel`)، `RESTITUTION` (إلغاء المطالبة المعلقة للضحية نفسها).
- **يصدر:** `CONSEQUENCE` (فوري أو مؤجل)، `CONSEQUENCE` بوسم `victim_discovery`، `NPC_DEPARTED` (مؤجلة)، `LIFE_EVENT`، `THEFT_VICTIM` (من `LifeEvents`).
- كل مؤجل يُنفَّذ عند حلوله عبر `Step` ← `Log.Submit` بالخطوات كاملة، ويُحذف من الطابور في خطوة البناء (FR-E5).

## الاعتمادات
`DecisionLog` (Submit)، `ScheduledEventQueue`، `MemoryStore` و`Reputation` (قراءة)، `RngStreams` (`consequences`، `life`). لا يقرأ `MoralLedger`.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Consequences/`: `SchedulingHandler.cs`، `ConsequenceRules.cs`، `LifeEvents.cs`، `LifeEventRules.cs`.
- `Content/Rules/consequence_rules.json`، `Content/Rules/life_events.json`.
- `Tests/EditMode/Consequences/`: `CausalChainTests.cs`، `LifeEventFairnessTests.cs`.

## الاختبار المنفرد
- سلسلة سببية: غش ← `CONSEQUENCE` بوسم `victim_discovery` ← `CONSEQUENCE`×3، وكل `causeEventIds` تشير إلى أحداث موجودة.
- **عدالة أحداث الحياة:** سيناريو لاعب أمين وسيناريو غاش بالبذرة نفسها ← تسلسل `LIFE_EVENT` متطابق يوماً بيوم.
- `LIFE_EVENT` بلا `causeEventIds` دائماً (فحص على كل السجل).
- `CLEARED` يلغي العواقب المعلقة المبنية على الاتهام.
- أساس T4: عاقبة مؤجلة عبر حد الحفظ تُنفَّذ مرة واحدة.

## حفظ الحالة (FR-S1)
`lastProcessedSeq`، و`LifeEventsState`، وحالة تيارَي `consequences` و`life`. العناصر المؤجلة ضمن طابور النواة. [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- إن حُسمت SR-09 بالجواز: يُضاف الاعتماد في مهمة جديدة بقرار في [DECISIONS](../../planning/DECISIONS.md)، مع مراجعة شرعية للصياغة.
- عواقب لمهن جديدة كصفوف في `consequence_rules.json`.

## المهام المرتبطة
[TASK-M07-002](../../tasks/M07/TASK-M07-002.md)، [TASK-M07-003](../../tasks/M07/TASK-M07-003.md)، [TASK-M04-013](../../tasks/M04/TASK-M04-013.md)، [TASK-M07-010](../../tasks/M07/TASK-M07-010.md)، [TASK-M12-004](../../tasks/M12/TASK-M12-004.md)، [TASK-M12-007](../../tasks/M12/TASK-M12-007.md)، [TASK-M06-005](../../tasks/M06/TASK-M06-005.md).
