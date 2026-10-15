# الضمير والإغراء: الصوتان الداخليان (Inner Voice)

المرجع: [PRD 7.6](../PRD.md) (FR-C1..C7)، والقيود S7، S8، S10، والمسائل SR-01، SR-12، SR-13.

## الثابت الحاكم
**الصوتان الداخليان طبقة عرض.** يعملان على `DecisionLog.OnRecorded` ومحفزات Runtime، ولا يغيّران أي حالة محاكاة. لا يحفظان إلا السطور المقولة ومهلاتها في `LineHistory` (FR-E4 الخطوة 6). تشغيل سيناريو معهما وبدونهما يعطي اللقطة نفسها باستثناء `LineHistory`.

## المسؤوليات
- التقاط المحفزات (7.6): قبل القرار (الاقتراب من خيار محرم في الميزان)، بعد القرار، نجاح الغش دون كشف (عند نهاية اليوم بلا `CONSEQUENCE` بوسم `victim_discovery`)، الانكشاف أو الاتهام الباطل، حدث حياة، كل خطوة توبة، تأمل المساء، لقاء ضحية سابقة.
- طلب السطر من `IDialogueProvider` بسياق `DialogueRequest { trigger, speaker = conscience|temptation, facts }` (FR-C1)، ثم ملء المتغيرات من أحداث فعلية في السجل (FR-C2): `{npc}` و`{day}` و`{goods}` من `GameEvent` محدد بـ `seq`.
- تطور النبرة لا الحكم (FR-C3) عبر حقيقة `moral.pattern`. ضعف الحضور مع الإصرار **معطل** (SR-01): حضور الضمير ثابت.
- الإغراء لا يمنع خياراً، ولا مؤقت (FR-C4)؛ يقترح خيارات اللعبة الموجودة فقط (S10).
- التمييز: صوت مسجل مختلف ومؤثر بصري وترجمة نصية دائمة (FR-C5).
- صياغة المصيبة تأملية، وللمظلوم والمبتلى صبر واحتساب (FR-C6). الممنوعات (FR-C7، S7): الجزم بالسببية، الإخبار بالمستقبل، الحكم بقبول التوبة. تُفرض بالمراجعة الشرعية للسطور، وبحقل `trigger` لا يسمح لسطور `life_event` بمتغير `{cause}`.
- SR-12: السطور التي تذكر الله أو الأجر أو الرجاء لا تُعرض إلا `approved`. SR-13: الإغراء كصوت داخلي لا يُشحن قبل الحسم.

## البيانات التي يمتلكها
- لا حالة محاكاة. `LineHistory` (مشترك مع barks): `{ lineId → { lastSaidAt, timesSaid } }` لمهلة `cooldown` و`once`.
- محتوى: `Content/Lines/conscience.json`، `Content/Lines/temptation.json` بمخطط `Line` ([DATA_ARCHITECTURE](../DATA_ARCHITECTURE.md)).

## الواجهة العامة
```csharp
public sealed class InnerVoiceDirector {                       // Simulation/InnerVoice: منطق نقي
    public InnerVoiceDirector(IDialogueProvider provider, FactSetBuilder facts, LineHistory history, DecisionLog log);
    public VoiceLine? OnEvent(GameEvent e);                    // من OnRecorded
    public VoiceLine? OnTrigger(InnerVoiceTrigger t, string? contextNpcId);   // من Runtime
}
public readonly struct VoiceLine { public string LineId; public VoiceSpeaker Speaker; public string TextKey; public string AudioKey; public IReadOnlyDictionary<string,string> Vars; }
// Runtime/UI: InnerVoicePresenter يعرض VoiceLine (ترجمة + مؤثر + صوت) ويستدعي history.MarkSaid
```
العشوائية (عند التعادل في الأولوية) من تيار `presentation` فقط.

## الأحداث التي يستقبلها ويصدرها
- **يستقبل:** `OnRecorded` لـ `CHEAT_*`، `FALSE_DESCRIPTION`، `TRADE_HONEST` (بعد قرار صعب)، `CONSEQUENCE` بوسم `victim_discovery`، `ACCUSED`، `CLEARED`، `LIFE_EVENT`، `THEFT_VICTIM`، `REPENT_REMORSE`، `REPENT_QUIT`، `RELAPSE`، `RESTITUTION`، `CHARITY_ON_BEHALF`. ومحفزات Runtime: `ApproachForbiddenChoice`، `EveningReflection`، `MeetFormerVictim`، `UndetectedCheatDayEnd`.
- **يصدر:** لا أحداث. خيارات الندم والإقلاع في التأمل تُعرض كحوار Yarn، والحدث يصدره الجسر ([DIALOGUE](DIALOGUE.md)).

## الاعتمادات
`IDialogueProvider` (`RuleDialogueProvider`)، `FactSetBuilder`، `LineHistory`، `DecisionLog` (قراءة الأحداث للمتغيرات). Runtime: الترجمة والصوت والمؤثر. حسب [TECHNICAL_ARCHITECTURE 4.1](../TECHNICAL_ARCHITECTURE.md): كل المراجع للقراءة فقط (`FactSetBuilder` يبني لقطة حقائق، و`DecisionLog.Get`)، والمرجع القابل للتغيير الوحيد `LineHistory`.

## الملفات البرمجية المقترحة
- `Scripts/Simulation/InnerVoice/`: `InnerVoiceDirector.cs`، `InnerVoiceTrigger.cs`، `VoiceLine.cs`.
- `Scripts/Runtime/UI/InnerVoicePresenter.cs`، `Scripts/Runtime/Audio/InnerVoiceAudio.cs`.
- `Content/Lines/conscience.json`، `Content/Lines/temptation.json`.
- `Tests/EditMode/InnerVoice/`.

## الاختبار المنفرد
- كل محفز مع حقائق مبرمجة ← سطر متوقع؛ المهلة تمنع التكرار؛ `once` لا يتكرر (أساس T6).
- كل متغير في السطر المختار يُحل من حدث موجود (`seq` صالح)، وإلا يُختار السطر العام (FR-D5).
- **اختبار عدم الأثر:** سيناريو 3 أيام مع المدير وبدونه ← اللقطة نفسها (عدا `lineHistory`).
- لا سطر `reviewStatus != approved` يحمل `sourceIds` يُختار في نسخة الإصدار.

## حفظ الحالة (FR-S1)
`LineHistory` فقط. عند التحميل لا يُعاد إطلاق أي سطر (FR-S2). [SAVE_SYSTEM.md](../SAVE_SYSTEM.md).

## التوسع المستقبلي
- مزود ذكاء اصطناعي يعيد صياغة السطر المعتمد فقط عبر `OutputFilter` (PRD 8.4)، دون تغيير المدير.
- تفعيل SR-01 إن حُسم: قاعدة إضافية على `moral.cheat_streak_bucket` بقرار جديد.

## المهام المرتبطة
[TASK-M06-002](../../tasks/M06/TASK-M06-002.md)، [TASK-M06-003](../../tasks/M06/TASK-M06-003.md)، [TASK-M07-004](../../tasks/M07/TASK-M07-004.md)، [TASK-M07-005](../../tasks/M07/TASK-M07-005.md)، [TASK-M07-006](../../tasks/M07/TASK-M07-006.md)، [TASK-M07-017](../../tasks/M07/TASK-M07-017.md)، [TASK-M07-019](../../tasks/M07/TASK-M07-019.md)، [TASK-M10-012](../../tasks/M10/TASK-M10-012.md)، [TASK-M12-015](../../tasks/M12/TASK-M12-015.md)، [TASK-M03-010](../../tasks/M03/TASK-M03-010.md).
