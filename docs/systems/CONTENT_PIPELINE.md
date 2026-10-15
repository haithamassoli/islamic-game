# خط المحتوى والتحقق الشرعي (Content Pipeline)

المرجع: [PRD 9](../PRD.md) (FR-Q1..Q5)، و9.1، و10 (SR-*)، والقيد S12، والقرار D-010 في [DECISIONS](../../planning/DECISIONS.md). الضوابط التفصيلية: [ISLAMIC_CONTENT_GUIDELINES.md](../ISLAMIC_CONTENT_GUIDELINES.md). المخططات: [DATA_ARCHITECTURE.md](../DATA_ARCHITECTURE.md).

## المسؤوليات
- **مرحلتان منفصلتان لكل عنصر ديني** (آية، حديث، حكم، سرد، سطر ضمير، دليل في المراجعة): `sourceCheck` (`unverified → verified`، فريق المحتوى) و`reviewStatus` (`draft → reviewed → approved` أو `rejected`، المراجع الشرعي فقط). الوكلاء لا يغيّرون `reviewStatus` أبداً.
- **بوابة البناء `ContentValidator`** (FR-Q1، FR-Q2): تفشل البناء وCI إذا وُجد في مجموعة البناء:
  - عنصر ديني ليس `verified` + `approved` معاً.
  - حديث بلا مصدر أو رقم أو درجة؛ آية بلا إحالة `surah:from-to`.
  - `sourceIds` تشير إلى معرّف غير موجود في سجل المصادر.
  - سطر شخصية بلدة يحمل `sourceIds` دينية (F3، SR-10).
  - ميزة مرتبطة بمسألة معلقة مفعّلة دون حسم (`pendingIssueIds` في البيانات، FR-Q5).
  - مفتاح ترجمة مفقود من جدول العربية.
- **FR-Q3:** أي تعديل على عنصر معتمد يعيده إلى `draft`: يُحسب `contentHash` للحقول الجوهرية ويُخزن مع الاعتماد؛ اختلاف البصمة = `draft` تلقائياً.
- **`TanzilImporter`** (FR-N2): يستورد ملف المصحف الخام من `content/quran/` مع التحقق من بصمته، ويولّد `Content/Story/quran_extract.json` بالإحالات المطلوبة فقط. نص الآيات لا يُكتب يدوياً.
- **FR-Q4:** `ReviewExporter` يصدّر المحتوى إلى جدول CSV في `content/review/` يقرؤه المراجع غير المبرمج (النص العربي، المصدر، الدرجة، السياق في اللعبة)، و`ReviewImporter` يستورد عمودي القرار والملاحظة فقط.
- المسائل المعلقة: سجل `content/sharia/pending_register.csv` بمعرّفات SR وسلوكها الافتراضي؛ أي مسألة جديدة تُضاف قبل بناء الميزة.

## البيانات التي يمتلكها
- **content/ (للبشر):** `content/sources/sources.csv` (سجل المصادر الدينية)، `content/sharia/pending_register.csv`، `content/quran/` (الملف الخام وبصمته)، `content/review/` (جداول التصدير والاستيراد).
- **unity/Assets/_Project/Content/ (للعبة):** `Lines/`، `Story/`، `Endings/`، `Journey/` تحمل `sourceIds[]` و`reviewStatus`. مصدر الحقيقة لـ `sourceCheck` هو سجل المصادر، ولـ `reviewStatus` حقل العنصر نفسه بعد الاستيراد.
- لا حالة لعب، ولا شيء من هذا يُحفظ في ملف الحفظ.

## الواجهة العامة
```csharp
// Editor assembly فقط
public static class ContentValidator {
    public static ValidationReport Validate(ContentDatabase db, SourceRegistry sources, PendingRegister sr, BuildProfile profile);
    [MenuItem("IslamicGame/Validate Content")] static void Menu();
}
public sealed class BuildGate : IPreprocessBuildWithReport { /* يستدعي Validate ويرمي BuildFailedException */ }
public static class TanzilImporter { public static void Import(string rawPath, string expectedSha256, IEnumerable<AyahRange> ranges, string outPath); }
public static class ReviewExporter { public static void Export(ContentDatabase db, string csvPath); }
public static class ReviewImporter { public static ImportReport Import(string csvPath, ContentDatabase db); }   // لا يرفع sourceCheck
```
`BuildProfile`: `Dev` يسمح بالمسودات مع علامة مرئية "مسودة غير معتمدة" ولا يُوزَّع؛ `Release` صارم.

## الأحداث التي يستقبلها ويصدرها
لا يشارك في FR-E4 ولا `OnRecorded`. يعمل قبل البناء وفي CI. في التشغيل، `ContentDatabase` في الإصدار يحتوي فقط ما اجتاز البوابة، فلا يحتاج محدد السطور فحصاً إضافياً.

## الاعتمادات
Newtonsoft JSON، Unity Build Pipeline (`IPreprocessBuildWithReport`)، Unity Localization (فحص المفاتيح). البيانات من [DIALOGUE](DIALOGUE.md) و[NARRATIVE](NARRATIVE.md) و[ENDINGS_AND_JOURNEY_REVIEW](ENDINGS_AND_JOURNEY_REVIEW.md).

## الملفات البرمجية المقترحة
- `Scripts/Editor/`: `ContentValidator.cs`، `BuildGate.cs`، `TanzilImporter.cs`، `ReviewExporter.cs`، `ReviewImporter.cs`، `SourceRegistry.cs`، `PendingRegister.cs`.
- `Content/Schemas/*.schema.json` (Line، StorySegment، SourceItem، PendingIssue).
- `Tests/EditMode/Content/`: `ContentValidatorTests.cs`، `TanzilImporterTests.cs`، `ReviewRoundTripTests.cs`.

## الاختبار المنفرد
- حزمة بيانات مصغرة فيها: حديث بلا درجة، آية بلا إحالة، سطر `approved` + `unverified`، سطر بلدة بمصدر ديني ← كل واحد يُفشل البوابة برسالة محددة.
- تعديل نص عنصر معتمد ← يصبح `draft` (FR-Q3).
- `TanzilImporter` على ملف مختلف البصمة ← يرفض.
- تصدير ثم استيراد بلا تعديل ← لا تغيير بايت واحد في JSON (قانوني).
- CI: الفحص يعمل على كل commit مع EditMode.

## حفظ الحالة (FR-S1)
لا ينطبق: لا حالة لعب. ملف الحفظ يخزن معرّفات المحتوى فقط (مثل `lineId`)؛ المحتوى المحذوف أو المرفوض بعد الحفظ يُتجاهل عند التحميل مع تحذير في نسخ التطوير.

## التوسع المستقبلي
- ترجمة المحتوى الديني (P5): لكل لغة `sourceCheck` و`reviewStatus` مستقلان للترجمة ([LOCALIZATION.md](../LOCALIZATION.md)).
- مخرجات الذكاء الاصطناعي (P6) تمر على `OutputFilter` ولا تدخل هذا الخط كمحتوى ديني أبداً.

## المهام المرتبطة
[TASK-M00-004](../../tasks/M00/TASK-M00-004.md)، [TASK-M00-006](../../tasks/M00/TASK-M00-006.md)، [TASK-M00-007](../../tasks/M00/TASK-M00-007.md)، [TASK-M01-025](../../tasks/M01/TASK-M01-025.md)، [TASK-M01-026](../../tasks/M01/TASK-M01-026.md)، [TASK-M01-027](../../tasks/M01/TASK-M01-027.md)، [TASK-M08-005](../../tasks/M08/TASK-M08-005.md)، [TASK-M08-006](../../tasks/M08/TASK-M08-006.md)، [TASK-M08-008](../../tasks/M08/TASK-M08-008.md)، [TASK-M11-005](../../tasks/M11/TASK-M11-005.md)، [TASK-M13-004](../../tasks/M13/TASK-M13-004.md)، [TASK-M13-005](../../tasks/M13/TASK-M13-005.md).
