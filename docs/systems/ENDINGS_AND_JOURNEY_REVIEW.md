# النهايات ومراجعة الرحلة (Endings & Journey Review)

المرجع: [PRD 7.11](../PRD.md) (FR-X1..X3)، و7.12 (FR-J1..J8)، وF5 وF6، والقيود S7 وS9 وS12.

## المسؤوليات
- **محدد النهاية** (`EndingSelector`): دالة نقية تُستدعى **لحظة النهاية فقط** (FR-X1). تأخذ محور الحقيقة من `TruthAxis.Evaluate` ([REPENTANCE](REPENTANCE.md)) ومحور السمعة من `Reputation.IsGoodForEnding()` بعتبة موازنة، وتُرجع واحدة من النهايات الثماني في جدول 7.11.
- FR-X2: `ReformInProgress` نهايتاه مستقلتان عن `Persisting`. FR-X3: لا نص يقول إن التوبة قُبلت أو إن الله غفر، ولا حديث عن الآخرة؛ أسماء الحالات الإنجليزية داخلية.
- **تسلسل F5** (`EndingSequence`، Runtime/Story): النهاية الشخصية ← بطاقة الانتقال ← مقطع خاتمة القوم ← مراجعة الرحلة ← العودة للعب الحر. البلدة لا تُهلك، ونهاية اللاعب لا تُربط بنجاة أو هلاك (F6).
- **مراجعة الرحلة** (`JourneyBuilder`): بطاقات مبنية **فقط** من وقائع حدثت (FR-J1): السجل، وأحداث العواقب، وحالات الشخصيات المحفوظة (المعتقدات بسلاسل نقلها).
  - كل بطاقة تحمل `evidenceEventIds[]` غير فارغة؛ القالب بلا بيانات لا يُعرض (FR-J2).
  - لا نتائج افتراضية ("لو كنت…") ولا آثار لم يحسبها النظام (FR-J3).
  - الأرقام من `amount` وتغير حاجات الأسر فقط، والسببية فقط عبر `causeEventIds` أو سلسلة الشائعة المسجلة ("رآك {A} يوم {d}، ثم أخبر {B}") (FR-J4).
  - أحداث الحياة لا تُربط بأي ذنب (FR-J5).
  - تُعرض الأفعال الخفية: الغش غير المكتشف، والصدقة السرية، والاتهامات الباطلة مع مصدرها (FR-J6).
  - الدروس والأدلة الشرعية معتمدة فقط، والصياغة مراجعة تعليمية لا صحيفة أعمال (FR-J7، S9، S12).
- **FR-J8:** `JourneyVerifier` يتحقق لكل بطاقة أن كل معرّف دليل موجود وكل رقم يطابق مجموع الأحداث المرتبطة؛ يعمل في الاختبارات وفي نسخ التطوير قبل العرض.

## البيانات التي يمتلكها
- لا حالة محاكاة دائمة. `EndingSequenceStep` يُحفظ ضمن `StoryStateData` ([NARRATIVE](NARRATIVE.md)) لاستئناف التسلسل بعد التحميل.
- محتوى: `Content/Endings/endings.json` (معرّف النهاية، `titleKey`، `bodyKey`، `sourceIds[]`، `reviewStatus`)، `Content/Journey/card_templates.json` (مخطط `JourneyCard` في [DATA_ARCHITECTURE](../DATA_ARCHITECTURE.md)).

## الواجهة العامة
```csharp
public static class EndingSelector {
    public static EndingId Select(TruthState truth, bool goodReputation);   // جدول 2×4 ثابت
}
public sealed class JourneyBuilder {
    public JourneyBuilder(DecisionLog log, MemoryStore memory, RightsLedger rights,
                          EconomyLedger economy, JourneyTemplates templates);
    public IReadOnlyList<JourneyCard> Build();         // ترتيب ثابت: القالب ثم أول seq
}
public static class JourneyVerifier {
    public static IReadOnlyList<string> Verify(IReadOnlyList<JourneyCard> cards, IReadOnlyList<GameEvent> log);   // فارغة = نجاح
}
// Runtime/Story: EndingSequence؛ Runtime/UI: JourneyReviewView
```

## الأحداث التي يستقبلها ويصدرها
- **يصدر:** `ENDING_REACHED` (عبر `Log.Submit` عند بدء التسلسل، يحمل معرّف النهاية في `tags`) ثم `STORY_SEGMENT_SEEN` لخاتمة القوم. بعدها يستمر العالم واللعب الحر.
- **يستقبل:** لا يعالج الأحداث مباشرة؛ يقرأ السجل كاملاً عند النهاية. ليس في القائمة الثابتة.

## الاعتمادات
`TruthAxis` و`RightsLedger` ([REPENTANCE](REPENTANCE.md))، `Reputation` و`MemoryStore` (السلاسل)، `DecisionLog`، `EconomyLedger` (حاجات الأسر)، قوالب ونصوص معتمدة.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Endings/`: `EndingSelector.cs`، `EndingId.cs`.
- `Scripts/Simulation/Journey/`: `JourneyCard.cs`، `JourneyBuilder.cs`، `JourneyTemplates.cs`، `JourneyVerifier.cs`.
- `Scripts/Runtime/Story/EndingSequence.cs`، `Scripts/Runtime/UI/JourneyReviewView.cs`.
- `Content/Endings/endings.json`، `Content/Journey/card_templates.json`.
- `Tests/EditMode/Endings/EndingMatrixTests.cs`، `Tests/EditMode/Journey/JourneyVerifierTests.cs`.

## الاختبار المنفرد
- مصفوفة النهايات: 8 حالات (4 حقيقة × 2 سمعة) ← النهاية الصحيحة؛ `ReformInProgress` لا يعطي نهاية `Persisting`.
- النهاية لا تتغير إن تغيرت قيم قبل لحظة النهاية ثم عادت (FR-X1).
- **FR-J8:** على عشرات السيناريوهات ببذور مختلفة: `Verify` يُرجع قائمة فارغة.
- قالب بلا بيانات (لا صدقة سرية) لا يُنتج بطاقة.
- لا بطاقة تضع `LIFE_EVENT` في `evidenceEventIds` مع حدث ذنب.

## حفظ الحالة (FR-S1)
البطاقات تُبنى عند الطلب ولا تُحفظ (مشتقة من السجل). خطوة تسلسل النهاية ضمن حالة القصة. الحفظ مسموح بين خطوات F5 فقط. [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- قوالب بطاقات جديدة لمهن ومحاور جديدة كبيانات، مع بقاء `JourneyVerifier` إلزامياً.
- مراجعة رحلة لكل فصل (لا عند النهاية فقط) بالقواعد نفسها.

## المهام المرتبطة
[TASK-M09-001](../../tasks/M09/TASK-M09-001.md)، [TASK-M09-002](../../tasks/M09/TASK-M09-002.md)، [TASK-M09-003](../../tasks/M09/TASK-M09-003.md)، [TASK-M09-004](../../tasks/M09/TASK-M09-004.md)، [TASK-M09-005](../../tasks/M09/TASK-M09-005.md)، [TASK-M09-006](../../tasks/M09/TASK-M09-006.md)، [TASK-M09-007](../../tasks/M09/TASK-M09-007.md)، [TASK-M09-008](../../tasks/M09/TASK-M09-008.md)، [TASK-M09-009](../../tasks/M09/TASK-M09-009.md)، [TASK-M07-013](../../tasks/M07/TASK-M07-013.md)، [TASK-M12-013](../../tasks/M12/TASK-M12-013.md).
