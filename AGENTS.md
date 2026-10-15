# AGENTS.md — تعليمات وكلاء الذكاء الاصطناعي

اقرأ هذا الملف كاملاً قبل أي عمل. هو العقد الذي يضمن أن يعمل أي وكيل أو مطور على المشروع بنفس القواعد.

## 1. ما الذي نبنيه؟
لعبة مغامرات إسلامية ثلاثية الأبعاد (Unity 6 + URP + C#) للمسلمين من 10 إلى 18 سنة والعائلات. عالم حي مستوحى من بيئة مدين، يعيش فيه اللاعب تاجراً ويتعلم الأمانة من قراراته وعواقبها، وقصة شعيب عليه السلام تُروى سرداً قرآنياً ثابتاً دون تجسيد الأنبياء. التفاصيل: [docs/VISION.md](docs/VISION.md).

## 2. خريطة المصادر (بترتيب السلطة)
| المصدر | الدور |
|---|---|
| [docs/PRD.md](docs/PRD.md) | **مصدر الحقيقة** للمتطلبات (FR-*)، والقيود الشرعية (S1–S13)، وسجل المسائل المعلقة (SR-*). عند التعارض يفوز PRD. |
| [docs/GDD.md](docs/GDD.md) | تصميم اللعب التفصيلي. |
| [docs/TECHNICAL_ARCHITECTURE.md](docs/TECHNICAL_ARCHITECTURE.md) و[docs/systems/](docs/systems/) | البنية التقنية ووثيقة لكل نظام. |
| [docs/ISLAMIC_CONTENT_GUIDELINES.md](docs/ISLAMIC_CONTENT_GUIDELINES.md) | الضوابط الشرعية وخط المراجعة. |
| [planning/TASK_INDEX.md](planning/TASK_INDEX.md) و[planning/TASKS.csv](planning/TASKS.csv) | فهرس المهام (مولَّد آلياً، لا تعدّله يدوياً). |
| [milestones/](milestones/) | ملف لكل مرحلة. |
| [tasks/](tasks/) | ملف لكل مهمة: **مصدر الحقيقة لحالة المهمة**. |
| [PROJECT_STATUS.md](PROJECT_STATUS.md) | الحالة والتقدم. |
| [planning/DECISIONS.md](planning/DECISIONS.md) | القرارات المعتمدة. لا تخالف قراراً دون إضافة قرار جديد يلغيه. عند تعارض وثيقة نظام مع ملف مهمة في تفصيل تنفيذي يفوز ملف المهمة (D-013). |

## 3. كيف تعرف المرحلة الحالية وتختار المهمة التالية
1. افتح [PROJECT_STATUS.md](PROJECT_STATUS.md): المرحلة الحالية وقائمة المهام `Ready`.
2. اختر مهمة حالتها `Ready` بهذا الترتيب: المرحلة الأقدم أولاً، ثم `Critical` ثم `High` ثم `Medium` ثم `Low`، ثم المهمة التي تفتح أكبر عدد من المهام بعدها (انظر [planning/DEPENDENCIES.md](planning/DEPENDENCIES.md)).
3. **لا تبدأ مهمة إلا إذا كانت كل مهام `Dependencies` حالتها `Done`.** المهمة `Ready` تعني ذلك بالتحديد.
4. إن طُلب منك عمل بلا مهمة، أنشئ مهمة جديدة أولاً (القسم 9).

### حالات المهمة
| الحالة | المعنى |
|---|---|
| `Todo` | لها اعتمادات لم تكتمل. |
| `Ready` | كل اعتماداتها `Done`، ويمكن البدء. |
| `In Progress` | يعمل عليها أحد الآن. اكتب اسمك/معرّفك في Notes. |
| `Blocked` | متوقفة لسبب خارجي (مراجعة شرعية، ترخيص، عطل). اكتب السبب في Notes. |
| `In Review` | منفذة وتنتظر مراجعة بشرية أو شرعية. |
| `Done` | **كل** معايير القبول محققة ومختبرة فعلياً. كتابة الكود وحدها ليست Done. |

## 4. قواعد التنفيذ
### نطاق التعديل
- عدّل فقط الملفات المذكورة في `Expected Files` لمهمتك، وما تحتاجه اختباراتها.
- لا تعدّل نظاماً آخر. إن احتجت تغييراً فيه: أضف ملاحظة في مهمتك، وأنشئ مهمة جديدة، وضعها في `Dependencies` إن كانت تمنعك.
- لا تغيّر معرّف أي مهمة أبداً، ولا تحذف ملف مهمة. المهمة الملغاة تبقى بحالتها مع سطر `Cancelled:` في Notes.

### هيكل المستودع (ثابت)
```
/                      وثائق الإدارة (README, AGENTS, PROJECT_STATUS, NEXT_STEPS, CHANGELOG)
docs/                  الوثائق، docs/systems/ وثيقة لكل نظام، docs/reports/ تقارير التجارب والقياس
planning/              التخطيط (TASKS.csv وTASK_INDEX.md مولَّدان)
milestones/M00.md…     ملف لكل مرحلة
tasks/Mxx/TASK-Mxx-NNN.md  ملف لكل مهمة
content/               محتوى يقرؤه البشر والمراجع الشرعي: sources/ (سجل المصادر)، sharia/ (المسائل المعلقة)، quran/ (ملف المصحف الخام وبصمته)، review/ (جداول المراجعة)
tools/                 سكربتات (plan.py)
unity/                 مشروع Unity
  Assets/_Project/
    Scripts/Simulation/   منطق المحاكاة: C# عادي، asmdef IslamicGame.Simulation، noEngineReferences=true
      Core/ (GameClock, SeededRng, GameEvent, DecisionLog, ScheduledEventQueue)
      Perception/ Memory/ Rumors/ Social/ Economy/ Moral/ Consequences/
      Repentance/ InnerVoice/ Dialogue/ Narrative/ Endings/ Journey/ Save/
    Scripts/Runtime/      MonoBehaviours، asmdef IslamicGame.Runtime
      Bootstrap/ (GameRoot) Player/ Camera/ Interaction/ NPC/ Trade/ UI/ Audio/ Story/
    Scripts/Editor/       أدوات المحرر، asmdef IslamicGame.Editor (ContentValidator, TanzilImporter, BuildScripts)
    Tests/EditMode/       asmdef IslamicGame.Tests.EditMode
    Tests/PlayMode/       asmdef IslamicGame.Tests.PlayMode
    Content/              بيانات اللعبة: Lines/ Story/ Npcs/ Goods/ Dialogue/(.yarn) Endings/ Journey/ Rules/ World/ Schemas/
    Scenes/ Art/ Audio/ Fonts/ Localization/ Settings/
.github/workflows/     CI
```
- الـ namespace يطابق المسار: `IslamicGame.Simulation.Memory`، `IslamicGame.Runtime.Trade`.

### ملفات Unity
- لا تعدّل ملفات `.unity` و`.prefab` و`.asset` يدوياً كنص إلا لتغيير بسيط ومفهوم. فضّل التعديل من المحرر أو سكربت Editor.
- كل ملف أصل له ملف `.meta`؛ لا تحذفه ولا تنشئه يدوياً، واحفظهما معاً في commit واحد.
- الإعداد: Force Text serialization، وVisible Meta Files، والأصول الثنائية عبر Git LFS.
- لا تفتح نفس المشهد في مهمتين متوازيتين. المشاهد المشتركة تُعدَّل في مهمة واحدة في الوقت نفسه.

### قواعد C#
- منطق المحاكاة في `Scripts/Simulation` بلا أي مرجع لـ `UnityEngine`. يُحقن الوقت والعشوائية (`GameClock`، `SeededRng`)، ولا استخدام لـ `DateTime.Now` أو `UnityEngine.Random` أو `System.Random` في المحاكاة.
- التواصل حسب [PRD 8.2](docs/PRD.md):
  - مستهلك واحد معروف ← استدعاء مباشر.
  - معالجات المحاكاة ← قائمة ثابتة الترتيب في `DecisionLog` (FR-E4).
  - العرض ← حدث C# `DecisionLog.OnRecorded`، لا يغيّر حالة المحاكاة.
  - واجهات فقط عند وجود بديل متوقع: `ISaveStorage`، `IDialogueProvider`، والواجهة المشتركة لمعالجات المحاكاة.
- **ممنوع:** message bus عام، أطر DI، ECS، Singletons للحالة القابلة للحفظ، وواجهة لها تنفيذ واحد بلا بديل متوقع.
- أي حالة قابلة للحفظ: صنف C# عادي يُسلسل بـ JSON قانوني (FR-S4)، ولا تُحفظ مراجع Unity.
- نظام السمعة لا يقرأ سجل القرارات مباشرة. يرى فقط **معتقدات** الشخصيات (FR-R2). الأفعال السرية لا تصل إليه.
- كل نص يراه اللاعب بمفتاح ترجمة. لا نصوص عربية ثابتة داخل الكود.
- أسماء المعرفات بالإنجليزية، والتعليقات قليلة وتشرح "لماذا".

## 5. الاختبارات
- منطق المحاكاة: اختبارات EditMode حتمية ببذرة ثابتة في `Tests/EditMode`.
- التكامل والمشاهد: PlayMode في `Tests/PlayMode`.
- اختبارات الحفظ T1–T9 (PRD 7.15) إلزامية في CI بعد إنشائها.
- تشغيل محلي (بعد إنشاء مشروع Unity؛ عدّل المسار حسب إصدارك):
  ```
  /Applications/Unity/Hub/Editor/<version>/Unity.app/Contents/MacOS/Unity -batchmode -projectPath unity -runTests -testPlatform EditMode -testResults results.xml -logFile -
  ```
- **لا تكتب أن اختباراً نجح ما لم تشغّله فعلاً وترَ النتيجة.** إن لم تستطع تشغيله فاكتب ذلك صراحة في Notes، واترك المهمة `In Review` لا `Done`.

## 6. توثيق الإنجاز وتحديث الحالة
عند الانتهاء من مهمة:
1. **ملف المهمة:** حدّث `Status`، وضع علامة `[x]` على كل معيار قبول محقق، وأضف في Notes: ما نُفذ، والملفات المعدلة، وكيف اختُبر ونتيجته.
2. **مزامنة الفهارس:** شغّل `python3 tools/plan.py sync`. يحدّث تلقائياً:
   - `planning/TASKS.csv`.
   - `planning/TASK_INDEX.md`.
   - جداول المهام في `milestones/Mxx.md`.
   - كتلة التقدم في `PROJECT_STATUS.md`.
   - ترقية مهام `Todo` إلى `Ready` عند اكتمال اعتماداتها.
3. **ملف المرحلة:** إن اكتملت كل شروط المرحلة، حدّث قسم الحالة فيه يدوياً.
4. **PROJECT_STATUS.md:** حدّث الأقسام اليدوية (المشكلات الحالية، والخطوة التالية).
5. **CHANGELOG.md:** أضف سطراً لكل مهمة `Done` أو قرار مهم.
6. شغّل `python3 tools/plan.py check` ويجب أن ينجح قبل أي commit.

## 7. الأعطال
- اختبار فشل: لا تعطّله ولا تحذفه لتمرير البناء. أصلح السبب، أو اترك المهمة `In Progress` مع وصف العطل.
- عطل خارج نطاق مهمتك: أنشئ مهمة جديدة (`Type: Programming` أو `QA`) بأولوية مناسبة واذكرها في Notes.
- مانع خارجي: الحالة `Blocked` مع السبب، وانتقل لمهمة `Ready` أخرى.

## 8. المحتوى الديني: قواعد صارمة
- **لا تخترع أبداً** آية أو رقم آية أو حديثاً أو رقم حديث أو درجة حديث أو قول عالم أو فتوى.
- نص الآيات يُستخرج آلياً من ملف المصحف (FR-N2)، ولا يُكتب يدوياً، ولا تُولّده.
- أي مرجع لم تتحقق منه من مصدر أصلي: ضع `sourceCheck=unverified` وعلامة **Needs Verification**.
- أنت (الوكيل) لا تغيّر `reviewStatus` إلى `reviewed` أو `approved` أبداً. هذا للمراجع الشرعي البشري وحده.
- `sourceCheck=verified` يُغيّر فقط بعد مطابقة نص العزو والدرجة مع مصدر أصلي، مع ذكر المصدر.
- كل عنصر ديني جديد يدخل [content/sources/](content/sources/) قبل استخدامه.
- مسألة شرعية جديدة؟ أضفها لسجل المسائل المعلقة بمعرّف SR جديد وسلوك افتراضي محايد **قبل** بناء الميزة.
- القيود S1–S13 غير قابلة للتفاوض، ومنها:
  - لا تصوير للأنبياء ولا لأصواتهم.
  - لا ربط للمصيبة بعقوبة إلهية.
  - لا عدادات حسنات أو إيمان.
  - لا موسيقى بمعازف.
  - لا نص يحكم بقبول التوبة.
  - شخصيات البلدة لا تقتبس النصوص الشرعية.
- المهمة التي حقل `Religious Review` فيها `Yes` لا تصبح `Done` قبل تسجيل نتيجة المراجعة الشرعية في Notes. حتى ذلك الحين حالتها `In Review`.

## 9. إنشاء مهمة جديدة
1. خذ الرقم التالي في مجلد المرحلة (لا تعِد استخدام رقم).
2. انسخ القالب أدناه بكل أقسامه.
3. شغّل `python3 tools/plan.py sync` ثم `check`.

## 10. قالب ملف المهمة (إلزامي)
`tools/plan.py` يقرأ جدول الرأس، فلا تغيّر أسماء الحقول ولا شكل الجدول. القيم المسموحة:
- **Priority:** `Critical` | `High` | `Medium` | `Low`.
- **Status:** `Todo` | `Ready` | `In Progress` | `Blocked` | `In Review` | `Done`.
- **Type:** `Programming` | `Art` | `Design` | `Audio` | `Writing` | `Religious Review` | `QA` | `DevOps`.
- **Complexity:** `S` (أقل من يوم) | `M` (1–3 أيام) | `L` (3–7 أيام) | `XL` (أكثر من أسبوع، ويُقسَّم إلى Subtasks).
- **Level:** `Foundation` | `Prototype` | `VerticalSlice` | `MVP` | `PostMVP`.
- **Religious Review:** `Yes` | `No`.

```markdown
# TASK-M01-009 — سجل القرارات DecisionLog وخط المعالجة FR-E4

| Field | Value |
|---|---|
| **Task ID** | TASK-M01-009 |
| **Title** | سجل القرارات DecisionLog وخط المعالجة FR-E4 |
| **Milestone** | [M01](../../milestones/M01.md) |
| **Epic** | EP-03 |
| **Priority** | Critical |
| **Status** | Todo |
| **Type** | Programming |
| **Complexity** | L |
| **Level** | Foundation |
| **Dependencies** | [TASK-M01-006](../M01/TASK-M01-006.md), [TASK-M01-008](../M01/TASK-M01-008.md) |
| **Religious Review** | No |

## Objective
## Description
## Implementation Plan
## Expected Files
## Acceptance Criteria
- [ ] ...
## Testing
## Definition of Done
## Potential Issues
## Related Tasks
## Notes
## Religious Review
```
- خلية `Dependencies` بلا اعتمادات تُكتب `—`.
- `Definition of Done` تبدأ بـ `تنطبق [شروط الإنجاز العامة](../../planning/DEFINITION_OF_DONE.md)، إضافة إلى:` ثم الشروط الخاصة بالمهمة.

## 11. الاتساق
- مصطلحات ثابتة: FR-*, S*, SR-*, T1–T9, P0–P6 كما في PRD. أسماء الأنظمة كما في [docs/systems/](docs/systems/).
- روابط Markdown نسبية دائماً.
- لا تكرر محتوى PRD. اربط إليه بالقسم أو بالمعرّف.
- قبل الـ commit: يجب أن ينجح `python3 tools/plan.py check`، وكذلك اختبارات EditMode بعد وجودها.
- رسالة الـ commit تبدأ بمعرّف المهمة: `TASK-M01-009: DecisionLog pipeline`.
