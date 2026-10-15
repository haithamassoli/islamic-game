# معمارية البيانات (Data Architecture)

المرجع: [PRD 7 و9](PRD.md)، و[TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md)، والقرارات D-005 وD-011 وD-012 في [DECISIONS](../planning/DECISIONS.md). هذه الوثيقة تحدد **شكل** البيانات ومكانها وقواعدها. الحقول الموسومة "مقترح" تُثبت في المهمة المنفذة ([TASK-M01-008](../tasks/M01/TASK-M01-008.md)، [TASK-M01-025](../tasks/M01/TASK-M01-025.md)).

## 1. ثلاثة أنواع من البيانات
| النوع | أين | من يكتبه | يدخل ملف الحفظ؟ |
|---|---|---|---|
| **محتوى اللعبة** (تعريفات ثابتة) | `unity/Assets/_Project/Content/` كملفات JSON (TextAsset) و`.yarn` | المصممون والكتّاب، وأدوات Editor | لا (فقط معرّفاته) |
| **محتوى المراجعة** (للبشر والمراجع الشرعي) | `content/` في جذر المستودع: `sources/`، `sharia/`، `quran/`، `review/` | فريق المحتوى والمراجع | لا، ولا يدخل البناء مباشرة |
| **حالة اللعب** | ملف الحفظ (لقطة JSON) | المحاكاة فقط | نعم ([SAVE_SYSTEM.md](SAVE_SYSTEM.md)) |

النصوص العربية التي يراها اللاعب **ليست** في JSON المحتوى؛ تعيش في جداول Unity Localization ويشير إليها المحتوى بـ `textKey` ([LOCALIZATION.md](LOCALIZATION.md)). الاستثناء الوحيد: نص الآيات المستخرج آلياً في `Content/Story/quran_extract.json` (FR-N2).

### مجلدات `Content/`
`Lines/` (barks والصوتان)، `Story/` (المقاطع والفصول والآيات المستخرجة)، `Npcs/` (الشخصيات والجداول والأسر والشبكة الاجتماعية)، `Goods/`، `Dialogue/` (`.yarn`)، `Endings/`، `Journey/` حسب [AGENTS.md](../AGENTS.md). **مقترح** يُضاف في [TASK-M01-025](../tasks/M01/TASK-M01-025.md) ويكمل القائمة دون تغييرها: `Rules/` (جداول القواعد: أوزان السجل الأخلاقي، قواعد المعتقد والشائعات والعلاقات والعواقب وأحداث الحياة والإدراك والاقتصاد)، و`World/` (`locations.json`)، و`Schemas/` (مخططات توثيقية).

التحميل: `GameRoot` يقرأ TextAssets ويمرر النصوص إلى `ContentDatabase.Load(IReadOnlyDictionary<string,string> files)` في المحاكاة؛ اختبارات EditMode تقرأ الملفات نفسها من القرص. المحاكاة لا ترى `TextAsset`.

## 2. اصطلاح المعرّفات
| الكيان | الصيغة | أمثلة |
|---|---|---|
| شخصية / أسرة / مكان / بضاعة | `^[a-z][a-z0-9_]*$` | `rival`، `market_chief`، `hh_widow`، `market_player_shop`، `dates` |
| اللاعب | ثابت `player` | — |
| سطر (`Line.id`) | مقاطع منقوطة `<group>.<trigger>.<nn>` | `conscience.after_cheat.03`، `rival.greet.01` |
| مقطع قصة | `seg_<chapter>` | `seg_ch1`، `seg_epilogue` |
| نهاية / قالب بطاقة | snake_case | `honest_trusted`، `hidden_cheat` |
| عنصر مصدر ديني | `src_<kind>_<slug>` | `src_hadith_muslim_102` |
| مسألة معلقة | كما في PRD | `SR-01` … `SR-13` |
| حدث / معتقد / عنصر مؤجل | عدد صحيح `long` متزايد | `seq`، `Belief.id`، `ScheduledEvent.id` |
| مفتاح ترجمة | `<domain>.<entity>.<context>.<nn>` | `npc.rival.greet.01`، `line.conscience.after_cheat.03` |

قواعد: ASCII صغير فقط، لا يُعاد استخدام معرّف محذوف، والمعرّف لا يتغير بعد ظهوره في ملف حفظ منشور (وإلا يلزم ترحيل). القيم المرقمة (`enum`) تُسلسل **نصاً** ولا يُعاد ترقيمها.

## 3. المخططات الأساسية
الأعداد صحيحة: المال `long` بأصغر وحدة، والنسب والثقة والسرية بالألف `0..1000` (بدل 0–1 في PRD)، والزمن `{day, minute}` حيث `minute` 0..1439.

### GameEvent (PRD 7.1)
```json
{"seq":42,"type":"CHEAT_SCALE","actorId":"player","targetId":"customer_gossip","locationId":"market_player_shop",
 "day":3,"minute":610,"magnitude":2,"amount":35,"secrecy":800,"tags":["goods:dates"],
 "witnessIds":["porter_orphan"],"causeEventIds":[]}
```
`GameEventType`: من PRD: `TRADE_HONEST`، `CHEAT_SCALE`، `CHEAT_MIXING`، `FALSE_DESCRIPTION`، `HELP`، `SECRET_CHARITY`، `THEFT_VICTIM`، `LIFE_EVENT`، `ACCUSED`، `CLEARED`، `REPENT_REMORSE`، `REPENT_QUIT`، `RELAPSE`، `RESTITUTION`، `CHARITY_ON_BEHALF`، `APOLOGY`، `CONSEQUENCE`. **مضافة بالقرار D-013**: `SLANDER`، `NPC_DEPARTED`. **مقترحة تُحسم في مهامها** (TASK-M09-002 وTASK-M12-009):  `STORY_SEGMENT_SEEN`، `CHAPTER_ADVANCED`، `ENDING_REACHED`. حقول اختيارية مقترحة: `goodsId`، `quantityGrams` بدل وضعها في `tags`. `GameEventDraft` = الحقول نفسها قابلة للتعديل حتى الخطوة 4، بلا `seq` قبل الخطوة 1.

### Belief (PRD 7.3)
```json
{"id":118,"holderId":"customer_gossip","subjectId":"player","claim":"CHEATED","basisEventId":42,
 "source":"WITNESS","fromNpcId":null,"hops":0,"confidence":900,"day":3,"status":"Held","major":true}
```
`claim`: `CHEATED | HONEST | GENEROUS | CLEARED_OF_CHEATING` (قابلة للتوسع). `source`: `WITNESS | VICTIM | HEARSAY | MISTAKE | SLANDER`. `status`: `Held | Pending | Rejected`. الحقول `holderId` و`status` و`major` إضافات مقترحة لازمة لـ FR-M1 وFR-M4 وFR-M5.

### Line (PRD 7.10)
```json
{"id":"conscience.after_cheat.03","speaker":"conscience","trigger":"after_decision",
 "conditions":[{"fact":"last_event.type","op":"eq","value":"CHEAT_SCALE"},{"fact":"moral.pattern","op":"neq","value":"persisting_cheat"}],
 "priority":50,"cooldown":1440,"once":false,"vars":["npc","day"],
 "textKey":"line.conscience.after_cheat.03","audioKey":"line.conscience.after_cheat.03",
 "sourceIds":[],"reviewStatus":"draft","pendingIssueIds":[]}
```
`cooldown` بدقائق اللعب. `trigger` و`pendingIssueIds` إضافتان مقترحتان. سطر بلا `sourceIds` ولا لفظ ديني لا يحتاج اعتماداً شرعياً، لكن سطور الضمير التي تذكر الله أو الأجر أو الرجاء تمر بالمسار الكامل (SR-12).

### StorySegment (PRD 7.13)
```json
{"id":"seg_ch1","order":1,"triggerLocation":"narration_point_well","narrationKey":"story.seg_ch1.narration.01",
 "audioKey":"story.seg_ch1.narration.01","ayat":[{"surah":7,"from":85,"to":85},{"surah":11,"from":84,"to":86}],
 "hadithIds":[],"tafsirNotes":[{"textKey":"story.seg_ch1.tafsir.01","sourceIds":["src_tafsir_..."]}],
 "unverifiedFlags":[],"reviewStatus":"draft"}
```
الإحالات من جدول F4 في PRD فقط. `sourceIds` في المثال مثال شكل لا مرجع. `ayat` تُستخرج نصاً من `quran_extract.json`.

### تعريف الشخصية (NPC def)
```json
{"id":"rival","nameKey":"npc.rival.name","roleKey":"npc.rival.role","traits":["greedy","observant"],
 "householdId":"hh_rival","lineGroup":"merchant_greedy","yarnNode":"rival_start","scheduleId":"rival",
 "homeLocationId":"market_rival_shop","leavesAfterDay":null,"pendingIssueIds":[]}
```
السمات الثماني من PRD 5.2. `leavesAfterDay` لتاجر القافلة (F8).

### تعريف البضاعة (Goods def)
```json
{"id":"dates","nameKey":"goods.dates.name","qualities":["good","poor"],"buyPricePerKg":{"good":120,"poor":70},
 "demand":{"baseKgPerDay":20,"variancePermille":150},"spoilsAfterDays":null,"mixable":true}
```
البضائع السبع من FR-T1. الأرقام في الأمثلة توضيحية، والموازنة في [TASK-M12-018](../tasks/M12/TASK-M12-018.md).

### الأسرة (Household)
```json
{"id":"hh_widow","memberIds":["widow"],"money":300,"inventory":[{"goodsId":"wheat","grams":2000}],
 "needs":[{"id":"food","level":400,"dailyDelta":-50}]}
```
التعريف الابتدائي في `Content/Npcs/households.json`، والحالة الحية في `EconomyState` (FR-T4).

### ScheduledEvent (PRD FR-E5)
```json
{"id":17,"due":{"day":4,"minute":1140},"payload":{"type":"CONSEQUENCE","tags":["victim_discovery"],"actorId":"customer_gossip","targetId":"player",
 "locationId":"home_customer_gossip","causeEventIds":[42],"tags":[]}}
```
`payload` مسودة بلا `seq` ولا `witnessIds` ولا `amount` (تُحسب عند التنفيذ). الترتيب (`due`، `id`).

### JourneyCard (PRD 7.12)
```json
{"templateId":"hidden_cheat","titleKey":"journey.hidden_cheat.title","bodyKey":"journey.hidden_cheat.body",
 "vars":{"npc":"customer_gossip","day":"3"},"numbers":[{"key":"amount","value":35,"sourceEventIds":[42]}],
 "evidenceEventIds":[42],"chain":[]}
```
`chain` لسلاسل الشائعة: `[{"npcId":"porter_orphan","day":3,"toNpcId":"customer_gossip"}]` من حقول `Belief`. القالب (`Content/Journey/card_templates.json`): `{id, query, titleKey, bodyKey, sourceIds[], reviewStatus}`، و`query` اسم استعلام C# مسجل لا تعبير حر.

### عنصر مصدر ديني (`content/sources/sources.csv`)
أعمدة: `id, kind (quran|hadith|tafsir|fatwa|fiqh), citation, surah, ayahFrom, ayahTo, collection, number, grade, gradedBy, textAr, sourceCheck, checkedAgainst, checkedBy, reviewStatus, reviewerNotes, pendingIssueIds, contentHash`. مثال من PRD 9.1 فقط: `src_hadith_muslim_102, hadith, "مسلم 102", ..., sourceCheck=verified, reviewStatus=draft`. أي عنصر خارج PRD 9.1 يدخل `unverified` مع **Needs Verification**. الضوابط: [ISLAMIC_CONTENT_GUIDELINES.md](ISLAMIC_CONTENT_GUIDELINES.md).

### مسألة معلقة (`content/sharia/pending_register.csv`)
أعمدة: `id (SR-xx), title, usedIn (FR/F/S refs), defaultBehavior, featureFlag, status (open|resolved), resolution, resolvedBy, resolvedOn, decisionRef`. `featureFlag` (مثل `conscience_fade` لـ SR-01) يُقرأ من `Content/Rules/feature_flags.json`؛ `ContentValidator` يفشل إن كانت الراية مفعّلة والمسألة `open`.

## 4. JSON القانوني (D-005)
يطبق على ملف الحفظ وعلى ملفات المحتوى المحفوظة في git:
- Newtonsoft JSON مع `ContractResolver` يرتب الخصائص ترتيباً Ordinal، والقواميس تُكتب مرتبة بالمفتاح (`SortedDictionary` بمقارن Ordinal)، والمجموعات بترتيب معرّفاتها.
- أعداد صحيحة فقط في الحالة؛ لا `float` ولا `double` (يمنع اختلاف التقريب). المواقع بالسنتيمتر والزوايا بالدرجات الصحيحة.
- `enum` كنص، و`InvariantCulture`، وUTF-8 بلا BOM، وأسطر LF، والنصوص غير ASCII تُكتب كما هي.
- `null` يُحذف، والمصفوفة الفارغة تُكتب `[]`.
- ملف الحفظ: مضغوط بلا مسافات. ملفات المحتوى: إزاحة مسافتين وسطر أخير، ويعيد `ContentFormatter` تنسيقها، وCI يفشل إن اختلفت بعد التنسيق.

## 5. التحقق
- التحقق في C# داخل `ContentValidator` (Editor): تحميل إلى أصناف مكتوبة ثم قواعد صريحة: المعرّفات فريدة وصيغتها صحيحة، كل مرجع (`npcId`، `goodsId`، `locationId`، `sourceIds`، `pendingIssueIds`) موجود، كل `textKey`/`audioKey` موجود في جدوله، وبوابة FR-Q1/Q2 ([CONTENT_PIPELINE](systems/CONTENT_PIPELINE.md)).
- ملفات `Content/Schemas/*.schema.json` للتوثيق والإكمال التلقائي في المحرر فقط؛ لا نعتمد مكتبة تحقق بمخططات JSON داخل البناء (مكتبة Newtonsoft.Json.Schema مرخصة AGPL أو تجارياً).
- ملف الحفظ يُتحقق منه عند التحميل: `schemaVersion` معروف، وقيود بنيوية (`nextSeq > آخر seq`، كل `lastProcessedSeq <= nextSeq-1`)، ثم مدقق الاتساق FR-S7 في نسخ التطوير.

## 6. `textKey` و`audioKey`
- `textKey` إلزامي لكل نص يراه اللاعب، ويشير إلى جدول String Table؛ `audioKey` اختياري ويشير إلى Asset Table للأصوات بالمفتاح نفسه عادةً.
- غياب التسجيل لا يكسر شيئاً: الترجمة النصية دائمة (FR-C5، PRD 7.14). `ContentValidator` يحذّر في `Dev` ويفشل في `Release` فقط للسطور المطلوب تسجيلها في MVP.
- المتغيرات `{npc}` و`{day}` تُملأ بقيم مترجمة (اسم الشخصية من `nameKey`، والأرقام حسب [LOCALIZATION.md](LOCALIZATION.md)).

## 7. المهام المرتبطة
[TASK-M01-008](../tasks/M01/TASK-M01-008.md)، [TASK-M01-011](../tasks/M01/TASK-M01-011.md)، [TASK-M01-012](../tasks/M01/TASK-M01-012.md)، [TASK-M01-025](../tasks/M01/TASK-M01-025.md)، [TASK-M01-026](../tasks/M01/TASK-M01-026.md)، [TASK-M02-011](../tasks/M02/TASK-M02-011.md)، [TASK-M03-001](../tasks/M03/TASK-M03-001.md)، [TASK-M04-001](../tasks/M04/TASK-M04-001.md)، [TASK-M04-003](../tasks/M04/TASK-M04-003.md)، [TASK-M05-002](../tasks/M05/TASK-M05-002.md)، [TASK-M09-004](../tasks/M09/TASK-M09-004.md)، [TASK-M00-006](../tasks/M00/TASK-M00-006.md)، [TASK-M00-007](../tasks/M00/TASK-M00-007.md).
