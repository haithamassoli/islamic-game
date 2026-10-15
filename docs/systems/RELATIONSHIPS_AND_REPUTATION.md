# العلاقات والثقة والسمعة (Relationships & Reputation)

المرجع: [PRD 7.4](../PRD.md) (FR-R1..R4)، وFR-W5، و[TECHNICAL_ARCHITECTURE 6](../TECHNICAL_ARCHITECTURE.md).

## الثابت الحاكم
**السمعة لا ترى الأفعال السرية أبداً، بل المعتقدات فقط (FR-R2).** `RelationshipsHandler` لا يقرأ من `GameEvent` إلا `Seq` ليجلب `MemoryStore.ChangesAt(seq)`. لا يقرأ `type` ولا `amount` ولا `secrecy` ولا `witnessIds`. الغش الذي لم يشهده أحد لا ينشئ معتقداً، فلا يصل هنا. يُفرض باختبار وبمراجعة الكود (لا مرجع لـ `DecisionLog` في `Social/`).

## المسؤوليات
- `trust` و`affection` لكل شخصية تجاه اللاعب في المدى -100..100 (FR-R1)، أعداداً صحيحة.
- تحويل تغييرات المعتقدات إلى تغيّر في القيمتين عبر جدول `relationship_rules.json` (حسب `claim` و`source` و`confidence` وسمات الحامل).
- عدم التماثل (FR-R4): الخسارة أسرع من الاستعادة، وسقف استعادة لصاحب `grudge` (قد لا يسامح أبداً).
- FR-W5: الصفقات الأمينة بعد الإقلاع تنشئ معتقدات `HONEST` عند من يراها (عبر الذاكرة)، فترتفع الثقة تدريجياً بسقف يومي، ولا تعود دفعة واحدة.
- **السمعة** دالة مشتقة نقية من المعتقدات: لكل شخصية `ReputationView` (إيجابي/سلبي/محايد)، وللبلدة `TownReputation` مرجّحة بأوزان الأدوار. تُستعمل في عدد الزبائن والأسعار والموردين والحوار (FR-R3) وفي محور السمعة للنهاية بعتبة موازنة.

## البيانات التي يمتلكها
- `RelationshipsState { entries: [{ npcId, trust, affection, lastChangeDay, recoveredToday }] }` بترتيب `npcId`.
- السمعة **لا تُحفظ**: تُعاد من المعتقدات عند الطلب أو تُخزَّن مؤقتاً وتُبطَل عند أي `BeliefChange`.
- جداول: `Content/Rules/relationship_rules.json`، `Content/Rules/reputation_rules.json` (أوزان الأدوار، عتبة النهاية).

## الواجهة العامة
```csharp
public sealed class Relationships {
    public int Trust(string npcId); public int Affection(string npcId);
    public void ApplyBeliefChanges(IReadOnlyList<BeliefChange> changes);   // من الشائعات مباشرة
}
public sealed class RelationshipsHandler : ISimulationHandler {           // HandlerId = "relationships"
    public RelationshipsHandler(Relationships rel, MemoryStore memory);   // لا DecisionLog هنا
    public void Handle(GameEvent e) => rel.ApplyBeliefChanges(memory.ChangesAt(e.Seq));
}
public sealed class Reputation {
    public Reputation(MemoryStore memory, Relationships rel, NpcRegistry npcs, ReputationRules rules);
    public ReputationView ViewOf(string npcId);
    public int TownScore();                       // داخلي، لا يُعرض رقماً للاعب
    public bool IsGoodForEnding();                // محور السمعة (7.11)
}
```

## الأحداث التي يستقبلها ويصدرها
- **يستقبل (5.4):** كل حدث، لكن أثره فقط عبر `ChangesAt(seq)`. يأتي بعد الذاكرة (5.1) فتكون المعتقدات جاهزة.
- **يستقبل خارج الخط:** نتائج `RumorSystem.Tick` و`Memory.DecayDay` باستدعاء مباشر من `Step`.
- **يصدر:** لا أحداث. آثار السمعة يقرؤها الآخرون: `CustomerFlow` و`PriceModel` و`SupplierPolicy` (اقتصاد)، و`FactSet` (حوار وbarks)، وقواعد الجدولة (امتناع المورد).

## الاعتمادات
`MemoryStore` (قراءة فقط)، `NpcRegistry` (السمات). ممنوع الاعتماد على `DecisionLog` و`MoralLedger` و`RightsLedger`.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Social/`: `Relationships.cs`، `RelationshipsHandler.cs`، `Reputation.cs`، `RelationshipRules.cs`، `ReputationRules.cs`.
- `Tests/EditMode/Social/`: `RelationshipsTests.cs`، `ReputationInvariantTests.cs`.

## الاختبار المنفرد
- **اختبار الثابت:** غش سري بلا شهود ← `TownScore` و`Trust` بلا تغيير؛ اتهام باطل (`SLANDER`) ← تنخفض.
- `SECRET_CHARITY` لا يرفع السمعة (FR-L4).
- عدم التماثل: خسارة 20 تحتاج أياماً متعددة من `HONEST` للاستعادة؛ `grudge` لا يتجاوز سقفه.
- اختبار معماري: تحليل انعكاسي يتأكد أن أنواع `Social/` لا تشير إلى `DecisionLog`.

## حفظ الحالة (FR-S1)
`RelationshipsState` و`lastProcessedSeq`. السمعة مشتقة ولا تُحفظ، فلا تكسر T1. ضمن T2 وT5: [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- علاقات بين الشخصيات أنفسهم (لا مع اللاعب فقط) بإضافة `subjectId` للمدخل.
- سمعة لكل حي أو جماعة في عوالم أكبر، من الأوزان نفسها.

## المهام المرتبطة
[TASK-M05-008](../../tasks/M05/TASK-M05-008.md)، [TASK-M05-009](../../tasks/M05/TASK-M05-009.md)، [TASK-M05-010](../../tasks/M05/TASK-M05-010.md)، [TASK-M05-011](../../tasks/M05/TASK-M05-011.md)، [TASK-M05-017](../../tasks/M05/TASK-M05-017.md)، [TASK-M07-012](../../tasks/M07/TASK-M07-012.md)، [TASK-M12-006](../../tasks/M12/TASK-M12-006.md)، [TASK-M12-018](../../tasks/M12/TASK-M12-018.md).
