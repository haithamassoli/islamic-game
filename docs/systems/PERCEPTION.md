# الإدراك والشهود (Perception)

المرجع: [PRD 7.2](../PRD.md) (FR-P1..P4)، و7.3 (FR-M2)، و[TECHNICAL_ARCHITECTURE](../TECHNICAL_ARCHITECTURE.md).

## المسؤوليات
- الخطوة 2 من FR-E4: حساب `witnessIds` لكل حدث من مواقع الشخصيات لحظة الفعل، وكتابتها في المسودة قبل الإلحاق.
- عوامل الحساب (FR-P1): المدى، وخط الرؤية (يُحسب مسبقاً في Runtime ويُمرر كبيانات)، والانتباه حسب نشاط الجدول، والزحام في المكان، وسمة `observant`، و`secrecy` الحدث.
- تحديد نوع المعرفة (FR-P2): شاهد مباشر هنا؛ الضحية المكتشِفة لاحقاً عبر حدث مؤجل `CONSEQUENCE` بوسم `victim_discovery` تجدوله قواعد الجدولة؛ السامع عبر الشائعات.
- ضمان FR-P4: يمكن أن تكون `witnessIds` فارغة، وهذا مسار مقصود لا خطأ.
- تقديم احتمال الانكشاف المتدرج حسب طريقة الغش (FR-P3) من جدول بيانات، لا من الكود.

## البيانات التي يمتلكها
لا حالة قابلة للحفظ. يقرأ:
- `NpcRegistry`: موقع كل شخصية (`locationId` + إحداثيات صحيحة بالسنتيمتر)، ونشاطها الحالي، وسماتها.
- `LocationRegistry`: الزحام لكل مكان ووقت، ومجموعات الرؤية بين الأماكن (`visibilityGroups`).
- جدول `perception_rules.json`: مدى الرؤية الأساسي، ومعامل `observant`، ومعامل الزحام، وانكشاف كل نوع غش بالألف.

## الواجهة العامة
```csharp
public sealed class Perception {
    public Perception(NpcRegistry npcs, LocationRegistry locations, PerceptionRules rules, RngStreams rng);
    public void ComputeWitnesses(GameEventDraft draft);       // يكتب draft.WitnessIds بترتيب Ordinal
    public int WitnessChancePermille(string npcId, GameEventDraft draft);  // للاختبار ولوحة التطوير
}
public readonly struct LineOfSightSnapshot { /* npcId → قائمة npcIds المرئية، يملؤها Runtime قبل Submit */ }
```
العشوائية من تيار `perception` فقط، والشخصيات تُعالج بترتيب معرّفاتها. الفاعل والهدف لا يُحسبان شهوداً (الهدف يعرف بصفته طرفاً في الصفقة أو ضحية لاحقاً).

## الأحداث التي يستقبلها ويصدرها
- **يستقبل:** كل مسودة في الخطوة 2 باستدعاء مباشر من `DecisionLog`. ليس معالجاً في القائمة الثابتة ولا مشتركاً في `OnRecorded`.
- **يصدر:** لا أحداث. الاكتشاف المؤجل (`CONSEQUENCE` بوسم `victim_discovery`) يجدوله `SchedulingHandler` (5.5) بقواعده، ثم يمر في الخط كأي حدث.

## الاعتمادات
`NpcRegistry` و`LocationRegistry` (Core)، و`RngStreams`. لا يعتمد على الذاكرة ولا السمعة. Runtime يزوّده بلقطة خط الرؤية عبر `NpcRegistry` قبل `Submit` (راجع [NPC_AGENTS](NPC_AGENTS.md)).

## الملفات البرمجية المقترحة
- `unity/Assets/_Project/Scripts/Simulation/Perception/Perception.cs`، `PerceptionRules.cs`.
- `unity/Assets/_Project/Scripts/Runtime/NPC/LineOfSightSampler.cs` (Raycast في Runtime، يكتب النتيجة كبيانات).
- `unity/Assets/_Project/Content/Rules/perception_rules.json`.
- `unity/Assets/_Project/Tests/EditMode/Perception/PerceptionTests.cs`.

## الاختبار المنفرد
- مواقع مبرمجة بلا مشهد: شخصية خارج المدى لا تشهد أبداً؛ `observant` يرفع الاحتمال؛ الزحام يخفضه.
- بذرة ثابتة: النتيجة نفسها في كل تشغيل؛ تغيير ترتيب إدخال الشخصيات لا يغيّر النتيجة.
- `secrecy=1000` بلا أحد في المدى ← `witnessIds` فارغة (FR-P4).
- توزيع إحصائي على 10,000 تكرار ببذرة ثابتة يطابق جدول FR-P3 (نقص الكيل أقل انكشافاً من الصنجات المغشوشة).

## حفظ الحالة (FR-S1)
لا حالة خاصة. النتائج تُحفظ داخل `GameEvent.witnessIds`، وحالة تيار `perception` ضمن `RngState`، ومواقع الشخصيات ضمن حالة `NpcRegistry`.

## التوسع المستقبلي
- حواس إضافية (السمع خلف الجدران) كصفوف في `perception_rules.json`.
- مهنة جديدة: أنواع أفعال جديدة بقيم انكشاف في الجدول نفسه، دون تغيير الصنف.

## المهام المرتبطة
[TASK-M05-001](../../tasks/M05/TASK-M05-001.md)، [TASK-M03-004](../../tasks/M03/TASK-M03-004.md)، [TASK-M02-011](../../tasks/M02/TASK-M02-011.md)، [TASK-M04-013](../../tasks/M04/TASK-M04-013.md)، [TASK-M05-013](../../tasks/M05/TASK-M05-013.md).
