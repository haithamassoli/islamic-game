# السجل الأخلاقي الداخلي (Moral Ledger)

المرجع: [PRD 7.5](../PRD.md) (FR-L1..L4)، والقيد S9، وFR-S7.

## الثابت الحاكم
**يرى كل شيء (العلني والسري) ولا يُعرض أبداً** كرقم أو شريط أو عداد (FR-L2، S9). ليس "صحيفة أعمال" ولا حساباً إلهياً، بل أداة داخلية لاختيار نبرة سطور الضمير ولاستخلاص محور الحقيقة. لا يُقرأ منه إلا عبر **حقائق خشنة** (`FactSet`) ودالة محور الحقيقة.

## المسؤوليات
- **المعالج 5.2 `MoralLedgerHandler`:** يحدّث أربعة محاور من سجل القرارات وحده (FR-L1): الأمانة `amanah`، والصدق `sidq`، والرحمة `rahma`، والعدل `adl`. يرى `secrecy` لكنه لا يجعلها تخفف الأثر.
- أوزان كل نوع حدث على المحاور في جدول بيانات، لا في الكود.
- عدّادات وقائع داخلية لازمة للقواعد: عدد الذنوب حسب النوع، وآخر `seq` ذنب، وتكرار الغش المتتالي (للنبرة FR-C3).
- FR-L4: `SECRET_CHARITY` يُسجَّل هنا فقط، ولا أثر له على السمعة (الذاكرة لا تنشئ معتقداً بلا شهود).
- تزويد `FactSet` بحقائق مصنفة: `moral.pattern = mostly_honest | mixed | persisting_cheat`، `moral.cheat_streak_bucket`، `moral.recent_mercy`، لا قيماً خاماً.
- دالة نقية `MoralLedger.Recompute(IReadOnlyList<GameEvent>)` لمدقق الاتساق (FR-S7).

## البيانات التي يمتلكها
- `MoralLedgerState { axes: { amanah, sidq, rahma, adl }, countsByType: { type → int }, lastSinSeq, cheatStreak }` أعداداً صحيحة.
- `Content/Rules/moral_weights.json`: `{ eventType → { amanah, sidq, rahma, adl } }`، مع حقول `isSin` و`isHelp`.

## الواجهة العامة
```csharp
public sealed class MoralLedger {
    internal MoralAxes Axes { get; }                 // internal: لا يصل إليه Runtime
    public long LastSinSeq { get; }
    public MoralPattern Pattern { get; }             // تصنيف خشن للحقائق
    public void WriteFacts(FactSet facts);
    public static MoralLedgerState Recompute(IReadOnlyList<GameEvent> log, MoralWeights w);
}
public sealed class MoralLedgerHandler : ISimulationHandler { /* HandlerId = "moral" */ }
```
`InternalsVisibleTo` لاختبارات EditMode وللوحة التطوير في نسخ التطوير فقط؛ أي واجهة إصدار تعرض المحاور ممنوعة وتُرفض في المراجعة.

## الأحداث التي يستقبلها ويصدرها
- **يستقبل (5.2):** كل الأنواع؛ الأوزان غير الصفرية لـ: `TRADE_HONEST`، `CHEAT_SCALE`، `CHEAT_MIXING`، `FALSE_DESCRIPTION`، `HELP`، `SECRET_CHARITY`، `RESTITUTION`، `CHARITY_ON_BEHALF`، `APOLOGY`، `SLANDER` (فاعله ليس اللاعب، فلا يحسب له).
- لا يحسب إلا أفعال `actorId = player`. `LIFE_EVENT` و`THEFT_VICTIM` وزنهما صفر دائماً (FR-K2).
- **يصدر:** لا أحداث. لا يربط أحداث الحياة بالسجل (FR-K4 معطل حتى SR-09).

## الاعتمادات
لا شيء سوى `GameEvent` وجدول الأوزان. يقرؤه: `FactSet`، و`TruthAxis` (النهايات)، و`ConsistencyChecker`.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Moral/`: `MoralLedger.cs`، `MoralLedgerHandler.cs`، `MoralWeights.cs`، `MoralPattern.cs`.
- `Content/Rules/moral_weights.json`.
- `Tests/EditMode/Moral/`: `MoralLedgerTests.cs`، `MoralLedgerRecomputeTests.cs`.

## الاختبار المنفرد
- غش سري: يتغير السجل الأخلاقي، ولا يتغير `Reputation` (اختبار مشترك مع [RELATIONSHIPS_AND_REPUTATION](RELATIONSHIPS_AND_REPUTATION.md)).
- `Recompute(log)` يساوي الحالة المتراكمة بعد سيناريو 200 حدث ببذرة ثابتة.
- `LIFE_EVENT` لا يغيّر أي محور.
- فحص آلي: لا مرجع لـ `MoralLedger.Axes` داخل `Scripts/Runtime/UI` (grep في CI).

## حفظ الحالة (FR-S1)
`MoralLedgerState` و`lastProcessedSeq`. في نسخ التطوير يقارن `ConsistencyChecker` بعد التحميل وعند كل حفظ قيمة `Recompute` باللقطة ويسجل الفرق (FR-S7). [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- محاور جديدة (الوفاء بالعهد، بر الوالدين) كأعمدة في الجدول بعد مراجعة شرعية لصياغتها.
- آلية ضعف حضور الضمير (FR-C3) تبقى معطلة حتى حسم SR-01؛ إن فُعّلت تقرأ `cheatStreak` فقط.

## المهام المرتبطة
[TASK-M07-001](../../tasks/M07/TASK-M07-001.md)، [TASK-M07-016](../../tasks/M07/TASK-M07-016.md)، [TASK-M07-014](../../tasks/M07/TASK-M07-014.md)، [TASK-M10-003](../../tasks/M10/TASK-M10-003.md).
