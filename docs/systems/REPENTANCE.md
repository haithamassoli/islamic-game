# التوبة ورد الحقوق (Repentance & Rights)

المرجع: [PRD 7.9](../PRD.md) (FR-W1..W6)، و7.11 (محور الحقيقة)، وF8، والمسائل SR-02، SR-03، SR-11 (نمذجة التوبة معلقة على المراجعة: تُبنى كما في 7.9 و7.11 ولا تُعرض نصوصها قبل الحسم).

## المسؤوليات
- **المعالج 5.3 `RepentanceHandler`** يدير عنصرين منفصلين:
  1. **آلة السلوك:** `Clean → Sinning → Remorseful → Quit`، و`Quit + ذنب ← RELAPSE ← Sinning`. الندم `REPENT_REMORSE` (FR-W1)، والإقلاع والعزم `REPENT_QUIT` قرار حواري صريح يُسجَّل فوراً بلا شرط أيام أو صفقات (FR-W2).
  2. **دفتر الحقوق `RightsLedger`:** لكل ضحية: المستحق = مجموع `amount` في أحداث الغش لها − ما رُد (FR-W3). يشمل من غُش سراً ولم يعلم.
- إصدار `RELAPSE` عند ذنب بعد `REPENT_QUIT` (عبر `Log.Submit` إلى طابور المتابعة).
- الرد المباشر `RESTITUTION` لأي ضحية، وعند ضحية لم تعلم يختار اللاعب: الإخبار (`tags: disclosed`) أو الرد دون تفصيل (FR-W4، نصوص SR-03).
- التصدق عنه `CHARITY_ON_BEHALF` فقط عند تعذر الوصول (`NPC_DEPARTED`، تاجر القافلة F8). الضحية المسافرة لا تعود في MVP (SR-02).
- FR-W5: الصفقات الأمينة بعد الإقلاع **ليست شرطاً**؛ أثرها ثقة الناس عبر المعتقدات (نظام العلاقات)، لا هنا.
- FR-W6: التوبة متاحة مرة بعد مرة؛ لا حد لعدد الدورات.
- دالة نقية لمحور الحقيقة (7.11): `TruthAxis.Evaluate(log, rights)` ← `Honest | Persisting | ReformInProgress | Reformed`. FR-X2: `ReformInProgress` لا يُعامل كـ `Persisting` في أي حقيقة.

## البيانات التي يمتلكها
- `RepentanceState { behavior, lastSinSeq, lastQuitSeq, relapseCount }`.
- `RightsLedgerState { victims: [{ npcId, owedTotal, repaidTotal, reachable, aware, sinSeqs[], repaySeqs[] }] }` بترتيب `npcId`.
- أسماء الحالات الإنجليزية داخلية ولا تظهر للاعب (FR-X3).

## الواجهة العامة
```csharp
public sealed class RepentanceSystem {
    public BehaviorState Behavior { get; }
    public RightsLedger Rights { get; }
    public bool CanOfferRemorse(); public bool CanOfferQuit();
    public void WriteFacts(FactSet facts);        // repent.behavior, rights.has_owed, rights.victim_unaware...
}
public sealed class RightsLedger {
    public long Owed(string victimId);            // owedTotal - repaidTotal
    public long TotalOwed { get; }
    public IReadOnlyList<VictimRights> Victims { get; }
    public static RightsLedgerState Recompute(IReadOnlyList<GameEvent> log);   // FR-S7
}
public static class TruthAxis { public static TruthState Evaluate(IReadOnlyList<GameEvent> log); }
public sealed class RepentanceHandler : ISimulationHandler { /* HandlerId = "repentance" */ }
```

## الأحداث التي يستقبلها ويصدرها
- **يستقبل (5.3):** `CHEAT_SCALE`، `CHEAT_MIXING`، `FALSE_DESCRIPTION` (حق + ذنب)، `REPENT_REMORSE`، `REPENT_QUIT`، `RELAPSE`، `RESTITUTION`، `CHARITY_ON_BEHALF`، `NPC_DEPARTED` (`reachable=false`)، `CONSEQUENCE` بوسم `victim_discovery` (`aware=true`).
- **يصدر:** `RELAPSE` فقط. `REPENT_*` و`RESTITUTION` و`CHARITY_ON_BEHALF` يصدرها جسر Yarn من خيارات الحوار ([DIALOGUE](DIALOGUE.md))، والمال يُنقل في الخطوة 3 قبل وصولها هنا.
- **عرض:** كل خطوة توبة تحفز الصوتين عبر `OnRecorded` ([INNER_VOICE](INNER_VOICE.md)). الضمير يشجع ولا يُيئس، ولا يحكم بالقبول (FR-C7).

## الاعتمادات
`DecisionLog` (Submit لـ `RELAPSE`، وقراءة للحساب). لا يقرأ المعتقدات ولا السمعة. يقرؤه: `FactSet`، والنهايات، ومراجعة الرحلة، و`ConsistencyChecker`.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Repentance/`: `RepentanceSystem.cs`، `RepentanceHandler.cs`، `BehaviorState.cs`، `RightsLedger.cs`، `TruthAxis.cs`.
- `Content/Dialogue/repentance.yarn` (خيارات الندم والإقلاع والرد)، `Content/Lines/` (سطور الضمير المرتبطة).
- `Tests/EditMode/Repentance/`: `BehaviorMachineTests.cs`، `RightsLedgerTests.cs`، `TruthAxisTests.cs`.

## الاختبار المنفرد
- جدول حالات: كل تسلسل ذنب/ندم/إقلاع/عودة ← الحالة المتوقعة من الأربع.
- غش لضحيتين (إحداهما سراً) ← `Owed` لكل منهما = مجموع `amount`؛ رد جزئي ← الباقي صحيح.
- رحيل تاجر القافلة ← `RESTITUTION` له مرفوض، و`CHARITY_ON_BEHALF` مقبول.
- `Recompute(log)` يساوي الحالة المتراكمة.
- أساس T9: رد جزئي ← حفظ ← تحميل ← المستحق والحالة بلا تغيير.

## حفظ الحالة (FR-S1)
`RepentanceState`، `RightsLedgerState`، `lastProcessedSeq`. محور الحقيقة مشتق ولا يُحفظ، ويُقارن في FR-S7. [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- حقوق غير مالية (غيبة، بهتان من اللاعب) كأنواع حقوق جديدة بعد مراجعة شرعية.
- عودة الضحية المسافرة وتخييرها (SR-02) إن حُسمت المسألة.

## المهام المرتبطة
[TASK-M07-007](../../tasks/M07/TASK-M07-007.md)، [TASK-M07-008](../../tasks/M07/TASK-M07-008.md)، [TASK-M07-009](../../tasks/M07/TASK-M07-009.md)، [TASK-M07-010](../../tasks/M07/TASK-M07-010.md)، [TASK-M07-011](../../tasks/M07/TASK-M07-011.md)، [TASK-M07-012](../../tasks/M07/TASK-M07-012.md)، [TASK-M07-013](../../tasks/M07/TASK-M07-013.md)، [TASK-M07-014](../../tasks/M07/TASK-M07-014.md)، [TASK-M07-015](../../tasks/M07/TASK-M07-015.md)، [TASK-M07-018](../../tasks/M07/TASK-M07-018.md)، [TASK-M07-019](../../tasks/M07/TASK-M07-019.md).
