# نظام الحوار (Dialogue)

المرجع: [PRD 7.10](../PRD.md) (FR-D1..D5)، و8.4، والقرار D-006 في [DECISIONS](../../planning/DECISIONS.md)، والقيد F3 والمسألة SR-10 (شخصيات البلدة لا تتكلم في الدين ولا تقتبس النصوص).

## المسؤوليات
- **الحوار المتفرع** بـ Yarn Spinner (FR-D1): ملفات `.yarn` لكل شخصية، وكل سطر بوسم `#line:` يربطه بمفتاح ترجمة ([LOCALIZATION](../LOCALIZATION.md)).
- **محدد القواعد** للسطور العابرة (barks) والصوتين (FR-D2): يقرأ `Line[]` من JSON، يطابق `conditions[{fact, op, value}]` على `FactSet`، ويختار بالأولوية، ويحترم `cooldown` و`once` (FR-D5)، ويرجع للسطر العام عند غياب المطابق.
- **الحقائق** (FR-D3): `FactSetBuilder` يجمعها من المعتقدات، والعلاقة، والسجل الأخلاقي (خشنة)، والتوبة، والوقت، والمكان، وحالة القصة. الأسماء نصية مسماة: `npc.trust_bucket`، `belief.npc_thinks_cheater`، `moral.pattern`، `story.chapter`، `time.part_of_day`، `loc.id`.
- طباع الشخصية تحدد مجموعة السطور (FR-D4) عبر `Line.speaker` و`conditions` على `npc.traits`.
- **`YarnSimulationBridge`:** أوامر Yarn تقرأ الحقائق (دوال `<<if fact("...")>>`) وتُصدر أحداثاً عبر `Log.Submit` (`ACCUSED`، `APOLOGY`، `REPENT_*`، `RESTITUTION`، `HELP`، طلب الفحص FR-M7). الحوار لا يغيّر حالة المحاكاة إلا عبر الأحداث.
- `IDialogueProvider` (PRD 8.4): التنفيذ الحالي `RuleDialogueProvider`؛ بديل مستقبلي يعيد صياغة السطر المعتمد فقط.

## البيانات التي يمتلكها
- `LineHistory { lineId → { lastSaidAt, timesSaid } }`: الحالة القابلة للحفظ الوحيدة لطبقة العرض.
- `Yarn` variables: لا تُستعمل لحالة اللعب؛ كل حالة تبقى في المحاكاة، وYarn يقرأ الحقائق فقط. استثناء: تقدم العقدة الحالية لا يُحفظ (لا حفظ أثناء الحوار؛ الحوار ليس نقطة آمنة).
- محتوى: `Content/Lines/*.json` (مخطط `Line` في [DATA_ARCHITECTURE](../DATA_ARCHITECTURE.md))، `Content/Dialogue/*.yarn`.

## الواجهة العامة
```csharp
public interface IDialogueProvider { DialogueResult Provide(DialogueRequest request); }
public sealed class RuleDialogueProvider : IDialogueProvider {
    public RuleDialogueProvider(LineDatabase lines, LineHistory history, GameClock clock, RngStreams rng);
}
public readonly struct DialogueRequest { public string Speaker; public string Trigger; public FactSet Facts; }
public readonly struct DialogueResult { public Line? Line; public bool IsFallback; }
public sealed class FactSet { public void Set(string fact, int value); public void Set(string fact, string value); public bool Match(LineCondition c); }
public sealed class FactSetBuilder { public FactSet Build(string? npcId, string? locationId); }
public sealed class LineHistory { public bool IsAvailable(Line l, GameTime now); public void MarkSaid(string lineId, GameTime now); }
// Runtime: YarnSimulationBridge (أوامر ودوال Yarn)، DialogueStarter، DialogueView (RTL)، BarkEmitter
```

## الأحداث التي يستقبلها ويصدرها
- **يصدر (عبر الجسر):** `ACCUSED`، `CLEARED` (نتيجة فحص كبير السوق، يُحسب في المحاكاة لا في Yarn)، `APOLOGY`، `HELP`، `REPENT_REMORSE`، `REPENT_QUIT`، `RESTITUTION`، `CHARITY_ON_BEHALF`.
- **يستقبل (عرض، `OnRecorded`):** `BarkEmitter` يطلق barks على أحداث قريبة (مثل `ACCUSED` في السوق). لا مكان له في القائمة الثابتة.

## الاعتمادات
`FactSetBuilder` (يقرأ `MemoryStore`، `Relationships`، `Reputation`، `MoralLedger.WriteFacts`، `RepentanceSystem.WriteFacts`، `StoryState`)، `DecisionLog` (للجسر)، Yarn Spinner وUnity Localization (Runtime).

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Dialogue/`: `IDialogueProvider.cs`، `RuleDialogueProvider.cs`، `Line.cs`، `LineDatabase.cs`، `LineHistory.cs`، `FactSet.cs`، `FactSetBuilder.cs`.
- `Scripts/Runtime/UI/DialogueView.cs`، `Scripts/Runtime/NPC/BarkEmitter.cs`، `Scripts/Runtime/NPC/DialogueStarter.cs`، `Scripts/Runtime/NPC/YarnSimulationBridge.cs` (Runtime بلا مجلد Dialogue في AGENTS).
- `Content/Lines/barks_*.json`، `Content/Dialogue/<npcId>.yarn`.
- `Tests/EditMode/Dialogue/`، `Tests/PlayMode/DialogueFlowTests.cs`.

## الاختبار المنفرد
- مطابقة الشروط بكل `op` (`eq`، `neq`، `gt`، `gte`، `lt`، `lte`، `has`).
- الأولوية الأعلى تفوز؛ التعادل يُكسر بتيار `presentation` ببذرة ثابتة.
- `cooldown` يمنع التكرار، و`once` لا يتكرر أبداً (أساس T6)؛ الرجوع للسطر العام عند غياب المطابق.
- الجسر: أمر Yarn ينتج المسودة المتوقعة؛ لا يغيّر حالة إلا بالأحداث.
- فحص محتوى: سطور شخصيات البلدة بلا `sourceIds` دينية (F3، SR-10) — في [CONTENT_PIPELINE](CONTENT_PIPELINE.md).

## حفظ الحالة (FR-S1)
`LineHistory` (السطور المقولة ومهلاتها). لا يُحفظ أثناء حوار مفتوح؛ الحفظ التلقائي يُؤجل حتى إغلاقه. [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- `AiParaphraseProvider` يغلّف `RuleDialogueProvider` مع `OutputFilter` (P6، [TECHNICAL_ARCHITECTURE 8](../TECHNICAL_ARCHITECTURE.md)).
- لغة جديدة: جداول ترجمة فقط؛ `Line` و`.yarn` لا يتغيران.

## المهام المرتبطة
[TASK-M01-028](../../tasks/M01/TASK-M01-028.md)، [TASK-M01-029](../../tasks/M01/TASK-M01-029.md)، [TASK-M01-030](../../tasks/M01/TASK-M01-030.md)، [TASK-M03-005](../../tasks/M03/TASK-M03-005.md)، [TASK-M03-006](../../tasks/M03/TASK-M03-006.md)، [TASK-M03-007](../../tasks/M03/TASK-M03-007.md)، [TASK-M03-008](../../tasks/M03/TASK-M03-008.md)، [TASK-M03-009](../../tasks/M03/TASK-M03-009.md)، [TASK-M03-010](../../tasks/M03/TASK-M03-010.md)، [TASK-M05-016](../../tasks/M05/TASK-M05-016.md)، [TASK-M12-014](../../tasks/M12/TASK-M12-014.md)، [TASK-M12-015](../../tasks/M12/TASK-M12-015.md).
