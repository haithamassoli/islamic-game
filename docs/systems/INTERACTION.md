# التفاعل واللاعب (Interaction)

المرجع: [PRD 7.7](../PRD.md) (FR-T2: الميزان تفاعل جسدي)، و7.14 (إعادة تعيين الأزرار، RTL)، وFR-C4 (لا مؤقت ضاغط)، و[TECHNICAL_ARCHITECTURE 4](../TECHNICAL_ARCHITECTURE.md).

## المسؤوليات
- **مصدر أفعال فقط:** يحوّل مدخلات اللاعب إلى استدعاءات مباشرة لخدمات المحاكاة (`TradeService`، `DialogueStarter`، نقاط السرد، النوم). لا يحمل منطق محاكاة ولا يقرر النتائج.
- متحكم الشخصية بالشخص الثالث وكاميرا Cinemachine مع تفادي التصادم.
- `Interactor`: اكتشاف أقرب `Interactable` في المدى وزاوية النظر، وعرض التلميح بالعربية داخل العالم أو على الشاشة، وتنفيذ الفعل عند الضغط.
- `ScaleInteraction` (FR-T2): وضع الصنجات والبضاعة جسدياً وقراءة الكفتين، وإنتاج `ScaleReading`. الغش يحدث داخل التفاعل نفسه (صنجة مغشوشة، ضغط الكفة، خلط)، دون زر "غش" ودون تعليم أساليب واقعية (S10).
- محفز "الاقتراب من خيار محرم" للصوتين (`ApproachForbiddenChoice`) يُطلق من هنا، بلا مؤقت ضاغط (FR-C4).
- لقطة خط الرؤية قبل كل `Submit` (يزوّد [PERCEPTION](PERCEPTION.md) عبر `NpcRegistry`).

## البيانات التي يمتلكها
- لا حالة محاكاة. موقع اللاعب واتجاهه يُحفظان ضمن حالة `NpcRegistry` (كيان `player`).
- `Input Actions` asset (`Settings/Input/GameControls.inputactions`) وإعادة التعيين تُحفظ في تفضيلات المستخدم (ملف إعدادات منفصل عن الحفظ، لا يدخل T1).
- `Interactable` على الكائنات: `interactionId`، `locationId`، `promptKey` (مفتاح ترجمة)، والهدف (`npcId` أو `goodsId` أو `segmentId`).

## الواجهة العامة
```csharp
public sealed class Interactor : MonoBehaviour {
    public Interactable Current { get; }
    public event Action<Interactable> FocusChanged;     // للتلميح فقط
}
public abstract class Interactable : MonoBehaviour {   // صنف أساس في Runtime، ليس واجهة
    public string InteractionId; public string LocationId; public string PromptKey;
    public abstract bool CanInteract(InteractionContext ctx);
    public abstract void Interact(InteractionContext ctx);
}
public sealed class ScaleInteraction : Interactable {
    public ScaleReading CurrentReading { get; }
    public void PlaceWeight(string weightId, int pan); public void PlaceGoods(string goodsId, int grams);
    public void Confirm(string customerId, SellClaim claim);   // ← TradeService.Sell(...)
}
```
`InteractionContext` يحمل مرجع `SimulationWorld` الذي يمرره `GameRoot`.

## الأحداث التي يستقبلها ويصدرها
- **يصدر (بشكل غير مباشر):** عبر `TradeService` (`TRADE_HONEST` (ومنه الشراء بوسم `purchase`)، `CHEAT_*`، `FALSE_DESCRIPTION`)، وعبر الحوار (`HELP`، `SECRET_CHARITY` عند الترك سراً في بيت المحتاج)، وعبر النوم (نقطة حفظ تلقائي).
- **يستقبل (عرض):** `OnRecorded` لتحديث التلميحات (مثلاً إخفاء خيار رد الحق بعد إتمامه). لا مكان له في القائمة الثابتة.

## الاعتمادات
Input System، Cinemachine، `IslamicGame.Simulation` (`TradeService`، `NpcRegistry`)، الترجمة (التلميحات)، [DIALOGUE](DIALOGUE.md) و[NARRATIVE](NARRATIVE.md) للأفعال المتخصصة.

## الملفات البرمجية المقترحة
- `Scripts/Runtime/Player/`: `PlayerController.cs`، `PlayerAnimator.cs`.
- `Scripts/Runtime/Camera/ThirdPersonCamera.cs`.
- `Scripts/Runtime/Interaction/`: `Interactor.cs`، `Interactable.cs`، `InteractionContext.cs`، `InteractionPrompt.cs`، `SleepInteractable.cs`.
- `Scripts/Runtime/Trade/ScaleInteraction.cs`.
- `Settings/Input/GameControls.inputactions`.
- `Tests/PlayMode/Interaction/`.

## الاختبار المنفرد
- PlayMode: اللاعب يقترب من كائن ← التلميح يظهر بمفتاح صحيح؛ يبتعد ← يختفي.
- `ScaleInteraction` بلا مشهد كامل: تسلسل وضع صنجات مبرمج ← `ScaleReading` متوقع ← مسودة الحدث الصحيحة (مع `TradeService` حقيقي و`SimulationWorld` ببذرة ثابتة).
- إعادة تعيين زر ← يعمل بعد إعادة التشغيل.
- لا `UnityEngine.Random` في منطق التفاعل الذي يؤثر على النتائج.

## حفظ الحالة (FR-S1)
موقع اللاعب واتجاهه ضمن `NpcRegistry`. التفاعل المفتوح (الميزان أثناء الوزن) ليس نقطة آمنة: الحفظ التلقائي ينتظر انتهاءه. تفضيلات الأزرار خارج ملف الحفظ.

## التوسع المستقبلي
- مخطط تحكم باللمس للجوال (P4) بنفس `Interactable` وInput Actions إضافية.
- مهن جديدة: `Interactable` جديد (محراث، سندان) يُنتج قراءة خاصة بالمهنة.

## المهام المرتبطة
[TASK-M02-001](../../tasks/M02/TASK-M02-001.md)، [TASK-M02-002](../../tasks/M02/TASK-M02-002.md)، [TASK-M02-003](../../tasks/M02/TASK-M02-003.md)، [TASK-M02-008](../../tasks/M02/TASK-M02-008.md)، [TASK-M02-009](../../tasks/M02/TASK-M02-009.md)، [TASK-M04-006](../../tasks/M04/TASK-M04-006.md)، [TASK-M04-007](../../tasks/M04/TASK-M04-007.md)، [TASK-M04-014](../../tasks/M04/TASK-M04-014.md)، [TASK-M10-004](../../tasks/M10/TASK-M10-004.md)، [TASK-M14-002](../../tasks/M14/TASK-M14-002.md).
