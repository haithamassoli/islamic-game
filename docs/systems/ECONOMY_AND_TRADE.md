# الاقتصاد والتجارة (Economy & Trade)

المرجع: [PRD 7.7](../PRD.md) (FR-T1..T5)، وFR-P3، و[TECHNICAL_ARCHITECTURE 4](../TECHNICAL_ARCHITECTURE.md). قيد S10: طرق الغش لا تعلّم أساليب واقعية تفصيلية.

## المسؤوليات
- **`EconomyLedger` (الخطوة 3 من FR-E4):** تطبيق الآثار المادية المباشرة لكل حدث (نقل المال والبضاعة بين اللاعب والأسر) وكتابة `amount` في المسودة. `amount` في الغش = ما نقص من الضحية فعلاً (الفرق بين المدفوع وقيمة ما استُلم)، وهو أساس FR-W3 وFR-J4.
- **`TradeService`:** يحوّل نتيجة تفاعل الميزان إلى مسودة حدث (`TRADE_HONEST`، `CHEAT_SCALE`، `CHEAT_MIXING`، `FALSE_DESCRIPTION`)، والشراء من المورد `TRADE_HONEST` بوسم `purchase` ويستدعي `Log.Submit`. لا يعدّل المال بنفسه.
- البضائع السبع (FR-T1) بجودة وسعر شراء وطلب يومي متغير (`RollDailyDemand` ببذرة، تيار `economy`).
- اقتصاد الأسر (FR-T4): رصيد ومخزون وحاجات لكل أسرة؛ المساعدة (`HELP`، `SECRET_CHARITY`، `CHARITY_ON_BEHALF`) تغيّر حاجات المستفيد فعلاً.
- الزبائن (FR-T3): `CustomerFlow.Tick` يولّد زبائن حسب الوقت والسمعة (تيار `customers`)، وبعضهم يفحص أو يزن في بيته (يجدول `CONSEQUENCE` بوسم `victim_discovery` عبر القواعد).
- الأسعار وامتناع الموردين حسب `Reputation` (FR-R3) — قراءة فقط.
- قاعدة الموازنة (FR-T5): الغش أربح قصيراً، والأمانة تنمو بالتكرار؛ تُثبت بمحاكاة بلا واجهة.

## البيانات التي يمتلكها
- `EconomyState { playerMoney, playerInventory[], households[], dailyDemand[], weightsOwned[] }` (المال `long` بأصغر وحدة).
- بيانات ثابتة: `Content/Goods/goods.json`، و`Content/Npcs/households.json` (القيم الابتدائية)، و`Content/Rules/economy_rules.json` (منحنيات الطلب، أثر السمعة، نسب الغش).

## الواجهة العامة
```csharp
public sealed class EconomyLedger {
    public long PlayerMoney { get; }
    public HouseholdView Household(string householdId);
    public void ApplyDirectEffects(GameEventDraft draft);   // الخطوة 3: يكتب draft.Amount
    public void RollDailyDemand(GameTime day);              // تيار "economy"
    public int PriceOf(string goodsId, string forNpcId);    // يقرأ Reputation
}
public sealed class TradeService {
    public long Sell(ScaleReading reading, string customerId, string goodsId, SellClaim claim);
    public long Buy(string supplierId, string goodsId, int quantity);  // يرفض إن امتنع المورد
}
public readonly struct ScaleReading { public int GoodsGrams; public int DeclaredGrams; public string WeightSetId; public int MixedPermille; }
```
`ScaleReading` يأتي من `ScaleInteraction` في Runtime (التفاعل الجسدي FR-T2)؛ الغش يُستنتج من القراءة نفسها (صنجة مغشوشة، نقص، خلط) لا من زر "غش".

## الأحداث التي يستقبلها ويصدرها
- **يصدر (عبر `TradeService`):** `TRADE_HONEST` (ومنه الشراء بوسم `purchase`)، `CHEAT_SCALE`، `CHEAT_MIXING`، `FALSE_DESCRIPTION`.
- **يستقبل (الخطوة 3، استدعاء مباشر):** كل حدث له أثر مادي: الأنواع أعلاه، و`HELP`، `SECRET_CHARITY`، `RESTITUTION`، `CHARITY_ON_BEHALF`، `THEFT_VICTIM`، `LIFE_EVENT` (نفقات)، `CONSEQUENCE` (تعويض).
- ليس معالجاً في القائمة الثابتة: آثاره قبل الإلحاق لأن `amount` جزء من الحدث غير القابل للتعديل.

## الاعتمادات
`Reputation` (قراءة)، `NpcRegistry`، `RngStreams` (`economy`، `customers`)، `DecisionLog` (لـ `TradeService` فقط). Runtime: `ScaleInteraction`، واجهة التسعير والبيع.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Economy/`: `EconomyLedger.cs`، `TradeService.cs`، `Inventory.cs`، `Household.cs`، `DemandModel.cs`، `CustomerFlow.cs`، `PriceModel.cs`، `SupplierPolicy.cs`، `ScaleReading.cs`.
- `Scripts/Runtime/Trade/`: `ScaleInteraction.cs`، `WeightPiece.cs`، `PricingPanel.cs`.
- `Content/Goods/goods.json`، `Content/Npcs/households.json`، `Content/Rules/economy_rules.json`.
- `Tests/EditMode/Economy/`: `EconomyLedgerTests.cs`، `BalanceSimulationTests.cs` (FR-T5).

## الاختبار المنفرد
- صفقة أمينة: مجموع المال في البلدة ثابت (حفظ الكتلة)؛ `amount=0` للأمانة.
- غش بالكيل: `amount` = النقص المحسوب بالضبط، ورصيد الضحية ينقص به.
- `BalanceSimulationTests`: 30 يوماً ببذرة ثابتة لثلاث استراتيجيات (أمين، غاش مكشوف، غاش مستتر): الغاش أغنى في الأيام الأولى، والأمين يلحق بتكرار الزبائن، والمستتر قد ينهي أغنى (FR-T5).
- الطلب اليومي متطابق لنفس البذرة.

## حفظ الحالة (FR-S1)
`EconomyState` كاملاً، وحالة تيارَي `economy` و`customers`. T2 يتحقق من المال ورصيد الضحية: [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- مهنة جديدة: `ScaleReading` يقابله مدخل خاص بالمهنة، و`TradeService` آخر، والأسر والمال كما هي.
- الربا والقروض والدَّين (P6) كأنواع أحداث وحالة ديون للأسر، بعد مراجعة شرعية.

## المهام المرتبطة
[TASK-M04-001](../../tasks/M04/TASK-M04-001.md)، [TASK-M04-002](../../tasks/M04/TASK-M04-002.md)، [TASK-M04-003](../../tasks/M04/TASK-M04-003.md)، [TASK-M04-004](../../tasks/M04/TASK-M04-004.md)، [TASK-M04-005](../../tasks/M04/TASK-M04-005.md)، [TASK-M04-006](../../tasks/M04/TASK-M04-006.md)، [TASK-M04-007](../../tasks/M04/TASK-M04-007.md)، [TASK-M04-008](../../tasks/M04/TASK-M04-008.md)، [TASK-M04-009](../../tasks/M04/TASK-M04-009.md)، [TASK-M04-010](../../tasks/M04/TASK-M04-010.md)، [TASK-M04-011](../../tasks/M04/TASK-M04-011.md)، [TASK-M04-012](../../tasks/M04/TASK-M04-012.md)، [TASK-M04-014](../../tasks/M04/TASK-M04-014.md)، [TASK-M04-015](../../tasks/M04/TASK-M04-015.md)، [TASK-M04-016](../../tasks/M04/TASK-M04-016.md)، [TASK-M05-010](../../tasks/M05/TASK-M05-010.md)، [TASK-M07-016](../../tasks/M07/TASK-M07-016.md)، [TASK-M12-004](../../tasks/M12/TASK-M12-004.md)، [TASK-M12-008](../../tasks/M12/TASK-M12-008.md)، [TASK-M12-018](../../tasks/M12/TASK-M12-018.md).
