# نظام الحفظ (Save System)

المرجع الملزم: [PRD 7.15](PRD.md) (FR-S1..S7 واختبارات T1–T9)، وFR-E4 الخطوة 6، و[TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md). القرارات: D-002 (الحفظ والحتمية من M01)، D-005 (Newtonsoft قانوني)، D-011 (مولد عشوائي بحالة محفوظة) في [DECISIONS](../planning/DECISIONS.md). مخططات البيانات وقواعد JSON القانوني: [DATA_ARCHITECTURE.md](DATA_ARCHITECTURE.md).

## 1. المبادئ
- **لقطة كاملة لا إعادة تشغيل** (FR-S2): التحميل يضع الحالة كما حُفظت. السجل تاريخ يُقرأ، لا أوامر تُعاد. لا يُطلق `OnRecorded` ولا سطر ولا صوت عند التحميل.
- **الحفظ عند نقطة آمنة فقط** (FR-S3): `SimulationWorld.IsAtSafePoint` = لا معالجة FR-E4 جارية (`DecisionLog.IsProcessing=false`)، ولا `Step` في منتصفه، ولا حوار أو تفاعل ميزان أو مقطع قصة مفتوح. طلب حفظ في غير ذلك يُؤجل لأول نقطة آمنة.
- **حتمية بايتية:** JSON قانوني (D-005) بلا أعداد عشرية ولا زمن حقيقي داخل اللقطة، فيتحقق T1.
- لا Singletons ولا ScriptableObject للحالة؛ كل نظام يملك صنف `*State` عادياً.

## 2. محتوى اللقطة (FR-S1)
```json
{"schemaVersion":1,
 "clock":{"day":3,"minute":1260},
 "rng":{"consequences":{...},"customers":{...},"economy":{...},"life":{...},"memory":{...},"npcs":{...},"perception":{...},"presentation":{...},"rumors":{...}},
 "log":{"nextSeq":431,"events":[...]},
 "scheduled":{"nextId":58,"items":[...]},
 "handlers":{"memory":{"lastProcessedSeq":430},"moral":{...},"repentance":{...},"relationships":{...},"scheduling":{...},"story":{...}},
 "economy":{...},"memory":{...},"rumors":{...},"relationships":{...},"moral":{...},
 "repentance":{...},"rights":{...},"lifeEvents":{...},"story":{...},"npcs":{...},"lineHistory":{...}}
```
المفاتيح مرتبة Ordinal عند الكتابة (الترتيب أعلاه للقراءة فقط). كل تيار عشوائي يُحفظ حالته الداخلية الكاملة (D-011).

**بيانات الخانة** (اسم، زمن حقيقي، يوم اللعب، الفصل) في ملف `slotN.meta.json` منفصل، لأنها تحمل زمناً حقيقياً وتكسر T1 لو دخلت اللقطة. لا تُقرأ في المحاكاة.

### مساهمة كل نظام
| النظام | ما يكتبه في اللقطة | ما **لا** يُحفظ (مشتق) |
|---|---|---|
| [EVENT_PIPELINE](systems/EVENT_PIPELINE.md) | `clock`، `rng`، `log` (`nextSeq` + السجل كاملاً)، `scheduled` | طابور المتابعة (فارغ عند النقطة الآمنة) |
| كل معالج (5.1–5.6) | `handlers.<id>.lastProcessedSeq` (FR-E7) | — |
| [MEMORY_AND_RUMORS](systems/MEMORY_AND_RUMORS.md) | `memory` (المعتقدات لكل شخصية، `nextBeliefId`)، `rumors` (`lastTickTime`) | الشبكة الاجتماعية (محتوى) |
| [RELATIONSHIPS_AND_REPUTATION](systems/RELATIONSHIPS_AND_REPUTATION.md) | `relationships` (`trust`، `affection`) | السمعة (دالة من المعتقدات) |
| [ECONOMY_AND_TRADE](systems/ECONOMY_AND_TRADE.md) | `economy` (مال اللاعب ومخزونه والأسر والطلب اليومي) | الأسعار (مشتقة) |
| [MORAL_LEDGER](systems/MORAL_LEDGER.md) | `moral` (المحاور والعدادات) | — (يُقارن بـ `Recompute` في FR-S7) |
| [REPENTANCE](systems/REPENTANCE.md) | `repentance` (آلة السلوك)، `rights` (دفتر الحقوق) | محور الحقيقة (مشتق، يُقارن في FR-S7) |
| [CONSEQUENCES_AND_LIFE_EVENTS](systems/CONSEQUENCES_AND_LIFE_EVENTS.md) | `lifeEvents` (`lastRolledDay`)؛ العواقب المؤجلة داخل `scheduled` | — |
| [NARRATIVE](systems/NARRATIVE.md) | `story` (الفصل، المقاطع المفتوحة والمشاهدة، خطوة تسلسل النهاية) | — |
| [NPC_AGENTS](systems/NPC_AGENTS.md) | `npcs` (مواقع الشخصيات واللاعب بالسنتيمتر، النشاط، كتلة الجدول، الحضور) | مسارات NavMesh |
| [DIALOGUE](systems/DIALOGUE.md) و[INNER_VOICE](systems/INNER_VOICE.md) | `lineHistory` (السطور المقولة ومهلاتها، FR-E4 الخطوة 6) | متغيرات Yarn، حالة العرض |
| [ENDINGS_AND_JOURNEY_REVIEW](systems/ENDINGS_AND_JOURNEY_REVIEW.md) | لا شيء | البطاقات (تُبنى من السجل) |
| [INTERACTION](systems/INTERACTION.md) | لا شيء (موقع اللاعب ضمن `npcs`) | تفضيلات الأزرار (ملف إعدادات منفصل) |

## 3. الواجهات
```csharp
public interface ISaveStorage {                         // FR-S6: محلي الآن، Convex لاحقاً
    IReadOnlyList<string> ListSlots();
    bool TryRead(string slot, out byte[] data);         // يرجع للنسخة الاحتياطية إن تلف الأساسي
    void WriteAtomic(string slot, byte[] data);         // FR-S5
    void Delete(string slot);
}
public sealed class LocalFileSaveStorage : ISaveStorage { public LocalFileSaveStorage(string rootDirectory); }
public sealed class SaveManager {
    public SaveManager(ISaveStorage storage, ContentDatabase content);
    public SaveResult Save(SimulationWorld world, string slot);   // يرفض إن !IsAtSafePoint
    public SimulationWorld Load(string slot);                      // ترحيل ← تحقق ← Restore
    public static byte[] Serialize(SaveSnapshot s); public static SaveSnapshot Deserialize(byte[] b);
}
public static class SaveMigrations {                    // FR-S4: دوال مرتبة، لا واجهة لكل ترحيل
    public static readonly Func<JObject, JObject>[] Steps;   // Steps[v] ترحّل من v إلى v+1
}
public static class ConsistencyChecker { public static IReadOnlyList<string> Check(SimulationWorld w); }   // FR-S7، نسخ التطوير
```
`LocalFileSaveStorage` في `Simulation/Save` (System.IO فقط، بلا `UnityEngine`)؛ `GameRoot` يمرر له `Application.persistentDataPath + "/saves"`، والاختبارات تمرر مجلداً مؤقتاً.

## 4. الكتابة والتحميل (FR-S4، FR-S5)
**الكتابة:** تسلسل قانوني ← كتابة `slotN.json.tmp` مع `Flush(true)` ← `File.Replace(tmp, json, bak)` يستبدل الأساسي ويحفظ السابق نسخة احتياطية في خطوة واحدة (أول حفظ: `File.Move`) ← كتابة `slotN.meta.json`. أي انقطاع قبل الاستبدال يترك الأساسي القديم سليماً، وبعده يبقى `bak` متاحاً.
**التحميل:** قراءة `slotN.json`؛ إن فشل التحليل أو التحقق البنيوي ← `slotN.json.bak`؛ ثم `SaveMigrations` من `schemaVersion` إلى الحالي؛ ثم `SimulationWorld.Restore`؛ ثم `ConsistencyChecker` في نسخ التطوير (يسجل الفروق ولا يصلحها بصمت).
**النقاط:** حفظ تلقائي عند النوم (نهاية الحلقة اليومية) ودورياً كل فترة لعب ثابتة عند أول نقطة آمنة، في الخانة الجارية. **3 خانات** للاعب ([TASK-M10-002](../tasks/M10/TASK-M10-002.md)) ومؤشر حفظ تلقائي ([TASK-M10-013](../tasks/M10/TASK-M10-013.md)).
**الإصدار:** `schemaVersion` يزيد مع أي تغيير غير متوافق؛ كل ترحيل يُختبر بملف تثبيت (fixture) من الإصدار الأقدم في `Tests/EditMode/Save/Fixtures/`.

## 5. اختبارات الحفظ T1–T9 (إلزامية في CI)
كلها EditMode ببذرة ثابتة عبر `SimulationWorld` بلا مشهد، في `unity/Assets/_Project/Tests/EditMode/Save/`. تُعاد كلها على محتوى MVP مع اختبار تحمل في [TASK-M13-001](../tasks/M13/TASK-M13-001.md).

| # | الاختبار (PRD 7.15) | الأنظمة المختبرة | المهمة | المرحلة |
|---|---|---|---|---|
| T1 | حفظ ← تحميل ← حفظ: تطابق بايتي | النواة، JSON القانوني | [TASK-M01-015](../tasks/M01/TASK-M01-015.md) | M01 |
| T2 | غش ← حفظ ← تحميل: المال ورصيد الضحية وعدد المعتقدات وطول السجل و`nextSeq` ثابتة | الاقتصاد، الذاكرة، السجل | [TASK-M05-017](../tasks/M05/TASK-M05-017.md) | M05 |
| T3 | سيناريو مبرمج مع حفظ وتحميل في منتصفه وبدونه: الحالة النهائية متطابقة | كل المحاكاة، تيارات العشوائية | [TASK-M06-005](../tasks/M06/TASK-M06-005.md) | M06 |
| T4 | حدث مؤجل عبر حدود الحفظ: يُنفَّذ مرة واحدة | `ScheduledEventQueue`، FR-E7 | [TASK-M06-005](../tasks/M06/TASK-M06-005.md) | M06 |
| T5 | دورة شائعات تعبر حد الحفظ: مطابقة للتشغيل بلا حفظ | الشائعات، تيار `rumors` | [TASK-M05-017](../tasks/M05/TASK-M05-017.md) | M05 |
| T6 | سطر `once` قيل قبل الحفظ لا يتكرر بعده | `LineHistory` | [TASK-M06-005](../tasks/M06/TASK-M06-005.md) | M06 |
| T7 | ملف من إصدار مخطط أقدم يُرحَّل ثم ينجح في T1 | `SaveMigrations` | [TASK-M01-015](../tasks/M01/TASK-M01-015.md) | M01 |
| T8 | انقطاع أثناء الكتابة: يبقى آخر حفظ سليم قابلاً للتحميل | `LocalFileSaveStorage` | [TASK-M01-015](../tasks/M01/TASK-M01-015.md) | M01 |
| T9 | رد حق جزئي ← حفظ ← تحميل: المستحق المتبقي والحالة الداخلية ثابتان | التوبة، دفتر الحقوق | [TASK-M07-015](../tasks/M07/TASK-M07-015.md) | M07 |

تفاصيل التنفيذ: T3 يقارن **لقطتين مسلسلتين** بايتياً لا كائنات. T8 يحاكي الانقطاع بكتابة `tmp` مبتورة دون إعادة تسمية، وبملف أساسي تالف مع `bak` سليم. اختبار إضافي في كل مرحلة: العرض لا يغيّر اللقطة (مع مشتركي `OnRecorded` وبدونهم) — [TECHNICAL_ARCHITECTURE 7](TECHNICAL_ARCHITECTURE.md).

## 6. Convex مستقبلاً (P6)
- خارج MVP (S13: لا شبكة ولا حسابات). يُضاف `ConvexSaveStorage : ISaveStorage` بموافقة ولي الأمر، دون تغيير `SaveManager` أو صيغة اللقطة.
- الكتابة الذرية تقابلها نسخ متعددة على الخادم مع رقم نسخة، والتعارض بين الأجهزة يُحل باختيار صريح من المستخدم لا بدمج تلقائي.
- النسخة المحلية تبقى المصدر الأساسي؛ السحابة نسخة اختيارية. التصميم في [TASK-M14-004](../tasks/M14/TASK-M14-004.md).
- WebGL: `persistentDataPath` يمر عبر IndexedDB ويحتاج مزامنة صريحة بعد الكتابة؛ يُتحقق من سلوك الإعادة الذرية هناك قبل قرار المنصة ([PERFORMANCE_TARGETS.md](PERFORMANCE_TARGETS.md)).

## 7. الميزانية
حجم الملف وزمن الحفظ والتحميل في [PERFORMANCE_TARGETS.md](PERFORMANCE_TARGETS.md).

## 8. المهام المرتبطة
[TASK-M01-012](../tasks/M01/TASK-M01-012.md)، [TASK-M01-013](../tasks/M01/TASK-M01-013.md)، [TASK-M01-014](../tasks/M01/TASK-M01-014.md)، [TASK-M01-015](../tasks/M01/TASK-M01-015.md)، [TASK-M03-010](../tasks/M03/TASK-M03-010.md)، [TASK-M05-017](../tasks/M05/TASK-M05-017.md)، [TASK-M06-001](../tasks/M06/TASK-M06-001.md)، [TASK-M06-005](../tasks/M06/TASK-M06-005.md)، [TASK-M07-014](../tasks/M07/TASK-M07-014.md)، [TASK-M07-015](../tasks/M07/TASK-M07-015.md)، [TASK-M10-002](../tasks/M10/TASK-M10-002.md)، [TASK-M10-013](../tasks/M10/TASK-M10-013.md)، [TASK-M13-001](../tasks/M13/TASK-M13-001.md)، [TASK-M14-004](../tasks/M14/TASK-M14-004.md).
