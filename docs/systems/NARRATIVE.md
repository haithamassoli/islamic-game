# السرد ومقاطع القصة (Narrative)

المرجع: [PRD 4](../PRD.md) (F1–F7)، و7.13 (FR-N1..N3)، والقيود S1–S4 وS12، والمسائل SR-04 وSR-05. الضوابط: [ISLAMIC_CONTENT_GUIDELINES.md](../ISLAMIC_CONTENT_GUIDELINES.md).

## المسؤوليات
- **فصل الطبقتين:** طبقة القصة (خبر ثابت) منفصلة عن المحاكاة (خيال معلن)، ومؤشر الطبقة ظاهر دائماً (F5، [TASK-M08-010](../../tasks/M08/TASK-M08-010.md)).
- **`StoryState` والمعالج 5.6 `StoryStateHandler`:** الفصل الحالي (1–3، الخاتمة)، وأي المقاطع فُتحت وأيها شوهد. الفصول تفتح المقاطع ولا تغيّرها (FR-N1)، والترتيب الثابت من F4 لا يتأثر بقرارات اللاعب (S2).
- شروط تقدم الفصول من بيانات (`chapters.json`): مثل أول إغراء بالتطفيف للفصل 1، وتراكم أيام لعب أو أحداث موضوعية للفصلين 2 و3.
- **`StorySegmentPlayer` (Runtime/Story):** عند نقطة سرد مفتوحة يشغّل المقطع بأسلوب بصري مميز: سرد الراوي (`narrationKey`، `audioKey`)، والآيات من النص المستخرج فقط (FR-N2)، وملاحظات التفسير، ووسم "رواية غير ثابتة" (S4).
- لا أنبياء ولا ملائكة: لا وجه ولا جسد ولا صوت ولا ظل ولا يد (S1). البيئة والأثر فقط.
- خاتمة القوم بالعرض الافتراضي لـ SR-04: سرد صوتي ونص الآيات وبيئة خالية من البشر. الأيكة لا تُذكر في المحاكاة، ومقاطعها تقتصر على النص القرآني (SR-05).
- بوابة S12: مقطع لا يحقق `verified` + `approved` لا يدخل البناء (يُفحص في [CONTENT_PIPELINE](CONTENT_PIPELINE.md)).

## البيانات التي يمتلكها
- `StoryStateData { chapter, unlockedSegmentIds[], seenSegmentIds[], endingSequenceStep }`.
- محتوى: `Content/Story/segments.json` (مخطط `StorySegment`)، `Content/Story/chapters.json`، `Content/Story/quran_extract.json` (يولّده `TanzilImporter`، لا يُحرر يدوياً).

## الواجهة العامة
```csharp
public sealed class StoryState {
    public int Chapter { get; }
    public bool IsUnlocked(string segmentId); public bool IsSeen(string segmentId);
    public string? NextSegmentAt(string locationId);
    public void WriteFacts(FactSet facts);                     // story.chapter, story.seen.<id>
}
public sealed class StoryStateHandler : ISimulationHandler { /* HandlerId = "story" */ }
// Runtime/Story: NarrationPoint (Interactable)، StorySegmentPlayer، AyahView، LayerIndicator، TransitionCard
```

## الأحداث التي يستقبلها ويصدرها
- **يستقبل (5.6، الأخير):** الأحداث الموضوعية لشروط الفصول (`CHEAT_*`، `TRADE_HONEST`، `ACCUSED`، `REPENT_QUIT`...) و`STORY_SEGMENT_SEEN`.
- **يصدر:** `STORY_SEGMENT_SEEN` (من `StorySegmentPlayer` عند الإكمال، عبر `Log.Submit`)، و`CHAPTER_ADVANCED` (من المعالج). هذان النوعان لا وزن أخلاقي لهما ولا معتقدات.
- **عرض:** فتح مقطع جديد يُظهر تلميحاً عبر `OnRecorded`.

## الاعتمادات
`DecisionLog`، `ContentDatabase` (المقاطع والآيات المستخرجة)، Runtime: الترجمة، عرض الآيات حسب قرار [TASK-M01-022](../../tasks/M01/TASK-M01-022.md) ([LOCALIZATION](../LOCALIZATION.md))، الصوت.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/Narrative/`: `StoryState.cs`، `StoryStateHandler.cs`، `StorySegment.cs`، `ChapterRules.cs`.
- `Scripts/Runtime/Story/`: `NarrationPoint.cs`، `StorySegmentPlayer.cs`، `AyahView.cs`، `LayerIndicator.cs`، `TransitionCard.cs`.
- `Content/Story/segments.json`، `Content/Story/chapters.json`، `Content/Story/quran_extract.json`.
- `Tests/EditMode/Narrative/`.

## الاختبار المنفرد
- الترتيب: محاولة تشغيل مقطع الفصل 2 قبل 1 مرفوضة؛ أي تسلسل قرارات يعطي ترتيب الفتح نفسه.
- مقاطع القصة لا تغيّر المال ولا المعتقدات ولا السجل الأخلاقي (اختبار عدم الأثر).
- كل `ayat[{surah, from, to}]` له نص في `quran_extract.json` مطابق لبصمة ملف المصحف.
- لا مقطع بـ `reviewStatus != approved` في قائمة البناء.

## حفظ الحالة (FR-S1)
`StoryStateData` و`lastProcessedSeq`. لا يُحفظ أثناء تشغيل مقطع؛ عند التحميل لا يُعاد تشغيل مقطع شوهد (FR-S2). [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- عالم نبي آخر = حزمة بيانات (`segments.json` و`chapters.json` جديدان) مع مراجعة شرعية كاملة، بلا تغيير في الكود.
- تلاوة مسجلة اختيارية (FR-N2) كأصل صوتي مرتبط بالمقطع.

## المهام المرتبطة
[TASK-M08-001](../../tasks/M08/TASK-M08-001.md)، [TASK-M08-002](../../tasks/M08/TASK-M08-002.md)، [TASK-M08-003](../../tasks/M08/TASK-M08-003.md)، [TASK-M08-004](../../tasks/M08/TASK-M08-004.md)، [TASK-M08-005](../../tasks/M08/TASK-M08-005.md)، [TASK-M08-006](../../tasks/M08/TASK-M08-006.md)، [TASK-M08-007](../../tasks/M08/TASK-M08-007.md)، [TASK-M08-009](../../tasks/M08/TASK-M08-009.md)، [TASK-M08-010](../../tasks/M08/TASK-M08-010.md)، [TASK-M08-011](../../tasks/M08/TASK-M08-011.md)، [TASK-M12-009](../../tasks/M12/TASK-M12-009.md)، [TASK-M12-010](../../tasks/M12/TASK-M12-010.md)، [TASK-M12-011](../../tasks/M12/TASK-M12-011.md)، [TASK-M12-012](../../tasks/M12/TASK-M12-012.md).
