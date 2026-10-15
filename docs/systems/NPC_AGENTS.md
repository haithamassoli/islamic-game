# وكلاء الشخصيات (NPC Agents)

المرجع: [PRD 5.2](../PRD.md) (الأدوار والسمات)، وF8، وFR-P1، و[TECHNICAL_ARCHITECTURE 2 و7](../TECHNICAL_ARCHITECTURE.md) (حركة NavMesh غير حتمية بين الأجهزة).

## المسؤوليات
- **`NpcRegistry` (Simulation/Core):** تعريفات الشخصيات (المعرّف، الدور، السمات الثماني، الأسرة، المجموعة الحوارية)، وحالتها الحية: `locationId`، الموقع بالسنتيمتر، النشاط الحالي، الحضور (موجود/مغادر).
- **الجداول اليومية:** `Npcs.UpdateSchedules(now)` يحدد لكل شخصية نشاطها ومكانها المستهدف حسب الساعة (كتل زمنية من البيانات)، و`Npcs.BeginDay()` يعيد ضبط اليوم.
- **الزحام:** كثافة لكل مكان حسب الوقت من بيانات `LocationRegistry` (FR-P1)، ويقرؤها الإدراك والزبائن.
- **`NpcAgent` (Runtime/NPC):** ينفّذ الهدف على NavMesh، ويكتب الموقع الفعلي في `NpcRegistry` كل فترة ثابتة، ويعيد التموضع من اللقطة عند التحميل (لا يعيد حساب المسار من الصفر).
- **سلوك المنافس المتقدم:** قرارات الغش والإغراء والبهتان تصدر كأحداث (`SLANDER`، وغش المنافس `CHEAT_SCALE` بفاعل `rival`) من قواعد بيانات بتيار عشوائي محاكاة، لا من MonoBehaviour.
- الشخصيات التي تغادر (تاجر القافلة) تصبح `present=false` بحدث `NPC_DEPARTED` (F8).

## البيانات التي يمتلكها
- تعريفات ثابتة: `Content/Npcs/npcs.json` (مخطط NPC def في [DATA_ARCHITECTURE](../DATA_ARCHITECTURE.md))، `Content/Npcs/schedules.json`، `Content/World/locations.json`.
- حالة حية: `NpcRegistryState { entities: [{ id, locationId, posCm{x,y,z}, yawDeg, activity, scheduleBlock, present }] }` بترتيب `id`، وتشمل `player`.

## الواجهة العامة
```csharp
public sealed class NpcRegistry {
    public IReadOnlyList<NpcDef> All { get; }                 // ترتيب Ordinal
    public NpcDef Def(string npcId); public NpcLive Live(string npcId);
    public bool HasTrait(string npcId, NpcTrait t);
    public void ReportPosition(string id, string locationId, PositionCm p, int yaw);   // من Runtime
    public void SetLineOfSight(LineOfSightSnapshot s);       // من Runtime قبل Submit
    public void BeginDay(GameTime day); public void UpdateSchedules(GameTime now);
}
public sealed class LocationRegistry { public LocationDef Get(string id); public int CrowdPermille(string id, GameTime t); }
public sealed class RivalBehavior { public void Tick(GameTime now); }    // Simulation/Core، يصدر أحداثاً
// Runtime/NPC: NpcAgent (NavMeshAgent)، NpcSpawner، NpcAnimator
```

## الأحداث التي يستقبلها ويصدرها
- **يصدر:** `SLANDER` و`CHEAT_*` بفاعل المنافس (من `RivalBehavior`)، و`NPC_DEPARTED` (مجدول عبر قواعد الجدولة).
- **يستقبل (عرض، `OnRecorded`):** `NpcAgent` يشغّل ردة فعل مرئية (التفات، إيماءة) للشهود. لا مكان له في القائمة الثابتة؛ المعالجون يقرؤون السجل لا الوكلاء.

## الاعتمادات
`GameClock`، `RngStreams` (تيار `npcs` لاختيارات الجدول وسلوك المنافس؛ تيار مضاف لقائمة TECHNICAL_ARCHITECTURE 7 دون إزاحة غيره)، `DecisionLog` (لـ `RivalBehavior`). Runtime: AI Navigation، Animator.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Core/`: `NpcRegistry.cs`، `NpcDef.cs`، `NpcTrait.cs`، `Schedule.cs`، `LocationRegistry.cs`، `RivalBehavior.cs`.
- `Scripts/Runtime/NPC/`: `NpcAgent.cs`، `NpcSpawner.cs`، `LineOfSightSampler.cs`.
- `Content/Npcs/npcs.json`، `Content/Npcs/schedules.json`، `Content/World/locations.json`.
- `Tests/EditMode/Core/NpcScheduleTests.cs`، `Tests/PlayMode/NpcAgentTests.cs`.

## الاختبار المنفرد
- الجدول: لكل ساعة مبرمجة، المكان والنشاط المتوقعان لكل شخصية.
- الزحام في السوق ذروته في الصباح حسب البيانات.
- حتمية: المحاكاة تقرأ المواقع المحفوظة لا NavMesh؛ اختبارات EditMode تستخدم مواقع مبرمجة.
- PlayMode: وكيل يصل إلى هدف الجدول خلال مهلة معقولة؛ الاستعادة من لقطة تضعه في الموقع المحفوظ.

## حفظ الحالة (FR-S1)
`NpcRegistryState` (المواقع والجداول والحضور)، وحالة تيار `npcs`. لا تُحفظ مسارات NavMesh؛ تُعاد من الهدف. [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- عند مئات الوكلاء: مستويات تفصيل للمحاكاة (خارج المدى = جدول فقط)، قبل التفكير في ECS ([TECHNICAL_ARCHITECTURE 10](../TECHNICAL_ARCHITECTURE.md)).
- علاقات بين الشخصيات تؤثر في الجداول (زيارات).

## المهام المرتبطة
[TASK-M03-001](../../tasks/M03/TASK-M03-001.md)، [TASK-M03-002](../../tasks/M03/TASK-M03-002.md)، [TASK-M03-003](../../tasks/M03/TASK-M03-003.md)، [TASK-M03-004](../../tasks/M03/TASK-M03-004.md)، [TASK-M03-011](../../tasks/M03/TASK-M03-011.md)، [TASK-M02-007](../../tasks/M02/TASK-M02-007.md)، [TASK-M02-011](../../tasks/M02/TASK-M02-011.md)، [TASK-M12-003](../../tasks/M12/TASK-M12-003.md)، [TASK-M12-019](../../tasks/M12/TASK-M12-019.md).
