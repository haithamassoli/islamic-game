# الذاكرة والمعتقدات والشائعات (Memory & Rumors)

المرجع: [PRD 7.3](../PRD.md) (FR-M1..M7)، وFR-E6، و[TECHNICAL_ARCHITECTURE 4.2 و6](../TECHNICAL_ARCHITECTURE.md).

## المسؤوليات
- **المعالج 5.1 `MemoryHandler`:** تحويل الحدث إلى معتقدات (`Belief`) لكل شاهد في `witnessIds` وللضحية عند `CONSEQUENCE` بوسم `victim_discovery`، حسب جدول `belief_rules.json` (نوع الحدث ← `claim`، `confidence`، الحجم).
- ذاكرة مستقلة لكل شخصية (FR-M1): لا تعرف إلا ما شهدته أو وصلها.
- المعتقد الخاطئ (FR-M2): `MISTAKE` (ميزان بيت معيب، تلف بعد البيع، خلط الفاعل في الدكان المجاور) و`SLANDER` (بهتان المنافس)، بـ `basisEventId` فارغ أو يشير إلى حدث لم يرتكبه اللاعب.
- **دورة الشائعات `RumorSystem.Tick`** (FR-E6، FR-M3): على فواصل ثابتة من `GameClock`؛ الناقلون بترتيب معرّفاتهم، والمستقبلون بترتيب معرّفاتهم، واحتمال النقل من `gossip` وقوة الرابط الاجتماعي، و`confidence` تنقص مع كل `hop`.
- تقييم السامع (FR-M4): `skeptic` أو الثقة العالية باللاعب ← رفض أو تأجيل الحكم (`Belief.status = Pending`).
- التلاشي (FR-M5): `Memory.DecayDay()` يُنقص الصغيرة يومياً؛ الكبيرة لا تتلاشى، وأقوى عند `grudge`.
- الدفاع (FR-M6): من أحسن إليه اللاعب يعارض الشائعة عند نقلها إليه أو منه، بحسب `trust`.
- التبرئة (FR-M7): `CLEARED` ينشئ معتقداً مضاداً عند الشهود، وينتشر بالدورة نفسها، ويُضعف معتقدات `CHEATED` المرتبطة.
- كشف التغييرات: قائمة `BeliefChange` لكل `seq` ولكل دورة شائعات، ليقرأها `Relationships` (الثابت: السمعة ترى المعتقدات فقط).

## البيانات التي يمتلكها
- `MemoryState { nextBeliefId, beliefsByNpc: { npcId → Belief[] } }` (المخطط في [DATA_ARCHITECTURE](../DATA_ARCHITECTURE.md)).
- `RumorState { lastTickTime }`. الشبكة الاجتماعية بيانات محتوى ثابتة (`Content/Npcs/social_graph.json`)، لا حالة.
- `Belief` يحمل سلسلة النقل (`fromNpcId`، `hops`، `day`) لتعرضها مراجعة الرحلة كما سُجلت (FR-J4).

## الواجهة العامة
```csharp
public sealed class MemoryStore {
    public IReadOnlyList<Belief> BeliefsOf(string npcId);                 // ترتيب id
    public IReadOnlyList<Belief> BeliefsAbout(string subjectId);
    public IReadOnlyList<BeliefChange> ChangesAt(long seq);               // ما أنشأه/عدّله الحدث seq
    public void DecayDay(GameTime now);
}
public sealed class MemoryHandler : ISimulationHandler { /* HandlerId = "memory" */ }
public sealed class RumorSystem {
    public RumorSystem(MemoryStore memory, NpcRegistry npcs, SocialGraph graph,
                       Relationships relationships, RumorRules rules, RngStreams rng);
    public IReadOnlyList<BeliefChange> Tick(GameTime now);                // تيار "rumors" فقط
}
public readonly struct BeliefChange { public long BeliefId; public string HolderId; public BeliefChangeKind Kind; }
```
`SimulationWorld.Step` يمرر ناتج `Tick` مباشرة إلى `Relationships.ApplyBeliefChanges` (مستهلك واحد).

## الأحداث التي يستقبلها ويصدرها
- **يستقبل (5.1):** `TRADE_HONEST`، `CHEAT_SCALE`، `CHEAT_MIXING`، `FALSE_DESCRIPTION`، `HELP`، `ACCUSED`، `CLEARED`، `CONSEQUENCE` بوسم `victim_discovery`، `SLANDER`، `RESTITUTION` (عند الإخبار، FR-W4)، `APOLOGY`. `SECRET_CHARITY` بلا شهود لا ينشئ شيئاً.
- **يصدر:** لا أحداث مباشرة. الاتهام العلني `ACCUSED` يصدره الحوار أو `SchedulingHandler` بناءً على المعتقدات. الشائعات **ليست أحداثاً في السجل**؛ أثرها في المعتقدات المحفوظة.
- **مجدول:** دورة الشائعات من `Step` (لا من الطابور)، والتلاشي عند بداية اليوم.

## الاعتمادات
`NpcRegistry` (السمات)، `SocialGraph`، `Relationships` (قراءة `trust` لـ FR-M4 وFR-M6)، `RngStreams` (`rumors` للنقل، و`memory` لخلط الفاعل). لا يقرأ `MoralLedger` ولا `Reputation`.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Memory/`: `Belief.cs`، `MemoryStore.cs`، `MemoryHandler.cs`، `BeliefRules.cs`.
- `Scripts/Simulation/Rumors/`: `RumorSystem.cs`، `SocialGraph.cs`، `RumorRules.cs`.
- `Content/Rules/belief_rules.json`، `Content/Rules/rumor_rules.json`، `Content/Npcs/social_graph.json`.
- `Tests/EditMode/Memory/`، `Tests/EditMode/Rumors/`.

## الاختبار المنفرد
- غش بلا شهود ← صفر معتقدات (أساس ثابت السمعة).
- شاهد واحد `gossip` ← انتشار عبر N دورات ببذرة ثابتة؛ `confidence` تنقص مع `hops`.
- `skeptic` يرفض خبراً بثقة منخفضة؛ صاحب إحسان يدافع.
- `grudge` لا يتلاشى معتقده الكبير بعد 30 يوماً.
- `CLEARED` يُضعف `CHEATED` وينتشر.
- أساس T5: دورة تعبر حد الحفظ تعطي نتيجة مطابقة.

## حفظ الحالة (FR-S1)
`MemoryState` كاملاً، و`RumorState`، و`lastProcessedSeq` للمعالج، وحالة تيارَي `rumors` و`memory`. اختبارا T2 وT5: [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- `claim` جديد (مثل `UNRELIABLE_DEBTOR` للقروض في P6) = قيمة enum + صفوف قواعد.
- عند مئات الشخصيات: فهرسة المعتقدات حسب `subjectId` بدل المسح الخطي.

## المهام المرتبطة
[TASK-M05-002](../../tasks/M05/TASK-M05-002.md)، [TASK-M05-003](../../tasks/M05/TASK-M05-003.md)، [TASK-M05-004](../../tasks/M05/TASK-M05-004.md)، [TASK-M05-005](../../tasks/M05/TASK-M05-005.md)، [TASK-M05-006](../../tasks/M05/TASK-M05-006.md)، [TASK-M05-007](../../tasks/M05/TASK-M05-007.md)، [TASK-M05-012](../../tasks/M05/TASK-M05-012.md)، [TASK-M05-013](../../tasks/M05/TASK-M05-013.md)، [TASK-M05-014](../../tasks/M05/TASK-M05-014.md)، [TASK-M05-015](../../tasks/M05/TASK-M05-015.md)، [TASK-M05-016](../../tasks/M05/TASK-M05-016.md)، [TASK-M05-017](../../tasks/M05/TASK-M05-017.md)، [TASK-M06-004](../../tasks/M06/TASK-M06-004.md).
