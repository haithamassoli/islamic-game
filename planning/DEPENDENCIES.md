# DEPENDENCIES — الاعتماديات

> **لقطة (snapshot)** محسوبة آلياً من [TASKS.csv](TASKS.csv) بتاريخ توليد هذا الملف. إذا تغيّرت `Dependencies` أو `Complexity` في أي ملف مهمة، شغّل `python3 tools/plan.py sync` ثم أعد توليد هذا الملف بالطريقة في القسم الأخير. لا تعدّل الجداول المولَّدة يدوياً.

- عدد المهام: 199. عدد حواف الاعتماد: 402. الرسم بلا دورات (تحقق بالفرز الطوبولوجي).
- الوزن: S=1، M=2، L=4، XL=8 نقاط.

## (أ) المسار الحرج حتى الإطلاق TASK-M13-010

أطول سلسلة اعتماد بالوزن تنتهي عند [TASK-M13-010](../tasks/M13/TASK-M13-010.md): **38 مهمة، 101 نقطة**. أي تأخير في مهمة منها يؤخر الإطلاق مباشرة؛ أي مهمة خارجها لها هامش. المسار يمر ببوابتي النموذج (M06) والشريحة (M11)، وبالمراجعة الشرعية النهائية.

| # | المهمة | العنوان | الحجم | التراكم |
|---|---|---|---|---|
| 1 | [TASK-M00-001](../tasks/M00/TASK-M00-001.md) | إنشاء نظام التخطيط والتتبع ومدقق الاتساق tools/plan.py | M | 2 |
| 2 | [TASK-M00-002](../tasks/M00/TASK-M00-002.md) | إكمال إعداد مستودع git (.gitignore لـ Unity وGit LFS وأول commit) | S | 3 |
| 3 | [TASK-M01-001](../tasks/M01/TASK-M01-001.md) | إنشاء مشروع Unity 6 بقالب URP وإعداداته الأساسية | S | 4 |
| 4 | [TASK-M01-002](../tasks/M01/TASK-M01-002.md) | هيكل المجلدات وملفات Assembly Definition | S | 5 |
| 5 | [TASK-M01-006](../tasks/M01/TASK-M01-006.md) | ساعة اللعبة GameClock (يوم ووقت وفواصل ثابتة) | S | 6 |
| 6 | [TASK-M01-009](../tasks/M01/TASK-M01-009.md) | سجل القرارات DecisionLog وخط المعالجة FR-E4 | L | 10 |
| 7 | [TASK-M01-011](../tasks/M01/TASK-M01-011.md) | طابور الأحداث المؤجلة ScheduledEventQueue (FR-E5) | M | 12 |
| 8 | [TASK-M01-013](../tasks/M01/TASK-M01-013.md) | لقطة الحفظ وSaveManager وISaveStorage المحلي | L | 16 |
| 9 | [TASK-M04-002](../tasks/M04/TASK-M04-002.md) | المخزون والمال Inventory | M | 18 |
| 10 | [TASK-M04-009](../tasks/M04/TASK-M04-009.md) | صفقة البيع الأمينة عبر خط المعالجة TRADE_HONEST | M | 20 |
| 11 | [TASK-M04-010](../tasks/M04/TASK-M04-010.md) | الغش بالكيل والصنجات CHEAT_SCALE | M | 22 |
| 12 | [TASK-M04-013](../tasks/M04/TASK-M04-013.md) | اكتشاف الضحية عند الوزن في البيت (حدث مؤجل) | M | 24 |
| 13 | [TASK-M05-013](../tasks/M05/TASK-M05-013.md) | مصادر المعتقد الخاطئ MISTAKE (ميزان معيب وتلف وخلط الفاعل) | L | 28 |
| 14 | [TASK-M05-015](../tasks/M05/TASK-M05-015.md) | تصحيح المعتقد والتبرئة (FR-M7 وCLEARED) | L | 32 |
| 15 | [TASK-M06-004](../tasks/M06/TASK-M06-004.md) | سيناريو اتهام باطل واحد | S | 33 |
| 16 | [TASK-M06-008](../tasks/M06/TASK-M06-008.md) | اختبار النموذج مع 5 أطفال أو أكثر وتقريره | M | 35 |
| 17 | [TASK-M06-009](../tasks/M06/TASK-M06-009.md) | مراجعة الاستمرار وتعديل الخطة بعد النموذج | S | 36 |
| 18 | [TASK-M07-001](../tasks/M07/TASK-M07-001.md) | معالج السجل الأخلاقي المخفي (FR-L1 إلى FR-L4) | M | 38 |
| 19 | [TASK-M07-007](../tasks/M07/TASK-M07-007.md) | آلة حالة التوبة (REPENT_REMORSE وREPENT_QUIT وRELAPSE) | M | 40 |
| 20 | [TASK-M07-008](../tasks/M07/TASK-M07-008.md) | دفتر الحقوق: المستحق لكل ضحية (FR-W3) | M | 42 |
| 21 | [TASK-M07-013](../tasks/M07/TASK-M07-013.md) | اشتقاق حالة محور الحقيقة (الحالات الأربع) | S | 43 |
| 22 | [TASK-M09-001](../tasks/M09/TASK-M09-001.md) | محدد النهاية من مصفوفة المحورين (8 نهايات) وعتبة السمعة | S | 44 |
| 23 | [TASK-M09-002](../tasks/M09/TASK-M09-002.md) | تسلسل النهاية F5 (النهاية الشخصية ثم الانتقال ثم خاتمة القوم ثم المراجعة ثم اللعب الحر) | M | 46 |
| 24 | [TASK-M09-003](../tasks/M09/TASK-M09-003.md) | محتوى نهايتين للشريحة العمودية | M | 48 |
| 25 | [TASK-M11-002](../tasks/M11/TASK-M11-002.md) | دمج محتوى الشريحة (يوم كامل ومسار توبة ومقطع قصة ونهايتان ومراجعة) | L | 52 |
| 26 | [TASK-M11-005](../tasks/M11/TASK-M11-005.md) | تدقيق المحتوى الديني في بناء الشريحة | S | 53 |
| 27 | [TASK-M11-006](../tasks/M11/TASK-M11-006.md) | اختبار لعب الشريحة مع أطفال وأولياء أمور وتقريره | M | 55 |
| 28 | [TASK-M11-007](../tasks/M11/TASK-M11-007.md) | تقدير كلفة إنتاج MVP | M | 57 |
| 29 | [TASK-M11-009](../tasks/M11/TASK-M11-009.md) | قرار الاستمرار وتثبيت نطاق MVP | S | 58 |
| 30 | [TASK-M12-001](../tasks/M12/TASK-M12-001.md) | مخطط البلدة الكامل (الأحياء وطريق القوافل والبئر والمراعي ونقاط السرد) | L | 62 |
| 31 | [TASK-M12-003](../tasks/M12/TASK-M12-003.md) | إعداد الأدوار الإحدى عشرة بسماتها وجداولها وأسرها | L | 66 |
| 32 | [TASK-M12-015](../tasks/M12/TASK-M12-015.md) | مجموعات barks والصوتين الداخليين الكاملة | XL | 74 |
| 33 | [TASK-M12-017](../tasks/M12/TASK-M12-017.md) | التسجيل العربي الكامل (الراوي والصوتان والسطور الرئيسية) | XL | 82 |
| 34 | [TASK-M13-004](../tasks/M13/TASK-M13-004.md) | المراجعة الشرعية النهائية لكل المحتوى | XL | 90 |
| 35 | [TASK-M13-006](../tasks/M13/TASK-M13-006.md) | اختبار لعب MVP وقياس معايير القسم 12 | L | 94 |
| 36 | [TASK-M13-007](../tasks/M13/TASK-M13-007.md) | إصلاحات ما بعد اختبار اللعب | L | 98 |
| 37 | [TASK-M13-008](../tasks/M13/TASK-M13-008.md) | بناء إصدار macOS (التوقيع والتوثيق والتوزيع المجاني) | M | 100 |
| 38 | [TASK-M13-010](../tasks/M13/TASK-M13-010.md) | الإطلاق وفرز الأعطال بعده | S | 101 |

ملاحظات: أطول سلسلة في الخطة كلها تنتهي عند [TASK-M14-002](../tasks/M14/TASK-M14-002.md) (103 نقاط) لأنها تأتي بعد الإطلاق (PostMVP). [TASK-M00-001](../tasks/M00/TASK-M00-001.md) منجزة، فالمتبقي على المسار 99 نقطة. أثقل حلقات المسار: الحفظ (TASK-M01-009/013)، والمعتقد الخاطئ ثم التبرئة (TASK-M05-013/015)، واختبارا اللعب في البوابتين (TASK-M06-008، وTASK-M11-006 بعد تدقيق المحتوى الديني TASK-M11-005)، وإنتاج سطور الصوتين وتسجيلها ثم المراجعة الشرعية النهائية (XL ×3)، ثم اختبار لعب MVP وإصلاحاته (TASK-M13-006/007) قبل بناء الإصدار.

## (ب) اعتماديات الأنظمة

### ب-1. اعتماد وقت التشغيل (معماري، PRD 8.2 وFR-E4)

| النظام | يحتاج | نوع الربط |
|---|---|---|
| DecisionLog (Core) | GameClock، SeededRng، Perception (الشهود)، Economy (`amount`) | استدعاء مباشر في الخطوات 1–3 |
| Memory/Beliefs | DecisionLog، Perception، Social network | معالج #1 في القائمة الثابتة |
| MoralLedger | DecisionLog فقط | معالج #2 |
| Repentance | DecisionLog، أحداث الغش (`amount`) لدفتر الحقوق | معالج #3 |
| Relationships/Reputation | Beliefs فقط (FR-R2)، لا السجل الخام | معالج #4 |
| Scheduling (ScheduledEventQueue، Consequences) | GameClock، Reputation، SeededRng | معالج #5 |
| StoryState | تقدم الفصول، Content (StorySegment) | معالج #6 |
| Rumors | Beliefs، Social network، SeededRng، GameClock tick | دورة ثابتة الفاصل (FR-E6): الشخصيات بترتيب معرّفاتها والعشوائية من المولد المحفوظ |
| Economy/Trade | Inventory، Goods، Reputation (عدد الزبائن والأسعار) | استدعاء مباشر |
| Dialogue (Yarn + LineSelector) | Facts provider (Beliefs، Relationships، MoralLedger، الوقت، المكان، StoryState)، DecisionLog للتسجيل | `IDialogueProvider` |
| InnerVoice | LineSelector، Facts، `OnRecorded` | عرض فقط، لا يغير المحاكاة |
| Endings | Truth axis (Repentance + دفتر الحقوق)، Reputation | دالة بلا آثار جانبية |
| Journey Review | DecisionLog، `causeEventIds`، سلاسل الشائعة المسجلة | قراءة فقط |
| Save | حالة كل ما سبق + RNG + `nextSeq` + `lastProcessedSeq` | `ISaveStorage` |
| Content gate | مخططات المحتوى، سجل المصادر، ملف المصحف | فحص بناء (Editor/CI) |

### ب-2. اعتماد الملاحم (محسوب من حواف المهام)

عدد الحواف من مهام الملحمة إلى مهام ملحمة أخرى. يقرأ: الملحمة في الصف تحتاج الملاحم المذكورة.

| الملحمة | تحتاج (عدد الحواف) | تعتمد عليها الملاحم |
|---|---|---|
| [EP-01](EPICS.md#ep-01) | EP-04 (1)، EP-18 (1)، EP-22 (3)، EP-23 (1)، EP-24 (1) | EP-02، EP-08، EP-14، EP-17، EP-24 |
| [EP-02](EPICS.md#ep-02) | EP-01 (1)، EP-03 (2) | EP-03، EP-04، EP-05، EP-06، EP-21، EP-23 |
| [EP-03](EPICS.md#ep-03) | EP-02 (2)، EP-04 (1)، EP-08 (1) | EP-02، EP-04، EP-05، EP-06، EP-07، EP-08، EP-09، EP-10، EP-11، EP-12، EP-14، EP-18، EP-23 |
| [EP-04](EPICS.md#ep-04) | EP-02 (1)، EP-03 (4)، EP-10 (1)، EP-11 (2)، EP-12 (1)، EP-13 (1)، EP-14 (1)، EP-16 (3)، EP-17 (1)، EP-24 (1) | EP-01، EP-03، EP-06، EP-09، EP-11، EP-19، EP-22، EP-24 |
| [EP-05](EPICS.md#ep-05) | EP-02 (1)، EP-03 (1)، EP-06 (1)، EP-23 (5)، EP-24 (1) | EP-10، EP-17، EP-19 |
| [EP-06](EPICS.md#ep-06) | EP-02 (2)، EP-03 (1)، EP-04 (1)، EP-08 (1)، EP-10 (1)، EP-11 (3)، EP-14 (2)، EP-15 (2)، EP-16 (2)، EP-17 (4)، EP-18 (3)، EP-20 (1) | EP-05، EP-08، EP-09، EP-10، EP-11، EP-15، EP-17، EP-20، EP-22، EP-24 |
| [EP-07](EPICS.md#ep-07) | EP-03 (1)، EP-23 (1) | EP-10، EP-11، EP-17، EP-19، EP-21 |
| [EP-08](EPICS.md#ep-08) | EP-01 (1)، EP-03 (5)، EP-06 (2)، EP-11 (3)، EP-12 (1)، EP-13 (1)، EP-16 (1)، EP-17 (1)، EP-18 (1)، EP-19 (1)، EP-21 (1) | EP-03، EP-06، EP-09، EP-17، EP-20، EP-21، EP-22، EP-23 |
| [EP-09](EPICS.md#ep-09) | EP-03 (1)، EP-04 (1)، EP-06 (1)، EP-08 (3)، EP-10 (1)، EP-12 (1) | EP-10، EP-11، EP-12، EP-13، EP-14، EP-15، EP-16، EP-23 |
| [EP-10](EPICS.md#ep-10) | EP-03 (4)، EP-05 (1)، EP-06 (1)، EP-07 (1)، EP-09 (4) | EP-04، EP-06، EP-09، EP-12، EP-15، EP-16، EP-19، EP-20، EP-22 |
| [EP-11](EPICS.md#ep-11) | EP-03 (5)، EP-04 (1)، EP-06 (1)، EP-07 (2)، EP-09 (7)، EP-16 (1)، EP-17 (1) | EP-04، EP-06، EP-08، EP-12، EP-13، EP-14، EP-15، EP-16، EP-19، EP-20، EP-22 |
| [EP-12](EPICS.md#ep-12) | EP-03 (5)، EP-09 (3)، EP-10 (2)، EP-11 (2)، EP-13 (2) | EP-04، EP-08، EP-09، EP-13، EP-18، EP-22 |
| [EP-13](EPICS.md#ep-13) | EP-09 (1)، EP-11 (2)، EP-12 (1) | EP-04، EP-08، EP-12، EP-14، EP-16، EP-18 |
| [EP-14](EPICS.md#ep-14) | EP-01 (3)، EP-03 (4)، EP-09 (2)، EP-11 (2)، EP-13 (1) | EP-04، EP-06، EP-15، EP-16، EP-18 |
| [EP-15](EPICS.md#ep-15) | EP-06 (3)، EP-09 (1)، EP-10 (2)، EP-11 (1)، EP-14 (1)، EP-19 (1) | EP-06، EP-16، EP-20، EP-22 |
| [EP-16](EPICS.md#ep-16) | EP-09 (1)، EP-10 (1)، EP-11 (1)، EP-13 (1)، EP-14 (1)، EP-15 (1) | EP-04، EP-06، EP-08، EP-11، EP-18 |
| [EP-17](EPICS.md#ep-17) | EP-01 (1)، EP-05 (1)، EP-06 (10)، EP-07 (1)، EP-08 (1) | EP-04، EP-06، EP-08، EP-11، EP-18، EP-19، EP-20، EP-22 |
| [EP-18](EPICS.md#ep-18) | EP-03 (1)، EP-12 (1)، EP-13 (1)، EP-14 (2)، EP-16 (2)، EP-17 (1) | EP-01، EP-06، EP-08، EP-19، EP-22 |
| [EP-19](EPICS.md#ep-19) | EP-04 (1)، EP-05 (5)، EP-07 (2)، EP-10 (1)، EP-11 (1)، EP-17 (1)، EP-18 (1)، EP-20 (1)، EP-21 (1) | EP-08، EP-15، EP-22 |
| [EP-20](EPICS.md#ep-20) | EP-06 (2)، EP-08 (1)، EP-10 (1)، EP-11 (1)، EP-15 (1)، EP-17 (3) | EP-06، EP-19، EP-22 |
| [EP-21](EPICS.md#ep-21) | EP-02 (1)، EP-07 (1)، EP-08 (3) | EP-08، EP-19، EP-22، EP-23 |
| [EP-22](EPICS.md#ep-22) | EP-04 (1)، EP-06 (2)، EP-08 (2)، EP-10 (1)، EP-11 (1)، EP-12 (2)، EP-15 (2)، EP-17 (1)، EP-18 (1)، EP-19 (2)، EP-20 (1)، EP-21 (1) | EP-01، EP-24 |
| [EP-23](EPICS.md#ep-23) | EP-02 (2)، EP-03 (1)، EP-08 (2)، EP-09 (1)، EP-21 (1)، EP-24 (1) | EP-01، EP-05، EP-07، EP-24 |
| [EP-24](EPICS.md#ep-24) | EP-01 (1)، EP-04 (1)، EP-06 (2)، EP-22 (1)، EP-23 (2) | EP-01، EP-04، EP-05، EP-23 |

## (ج) الاعتماد بين المراحل

لكل مرحلة: المراحل التي تعتمد عليها (عدد الحواف)، والمهام الخارجية التي يجب أن تكون `Done` قبل أن تصبح مهام المرحلة المعتمدة عليها `Ready`. المرحلة لا تحتاج أن تكتمل سابقتها كلها؛ يكفي أن تكتمل هذه المهام بعينها.

| المرحلة | تعتمد على | المهام الخارجية المطلوبة |
|---|---|---|
| [M00](../milestones/M00.md) | — | — |
| [M01](../milestones/M01.md) | M00 (8) | [TASK-M00-002](../tasks/M00/TASK-M00-002.md)، [TASK-M00-003](../tasks/M00/TASK-M00-003.md)، [TASK-M00-004](../tasks/M00/TASK-M00-004.md)، [TASK-M00-006](../tasks/M00/TASK-M00-006.md)، [TASK-M00-008](../tasks/M00/TASK-M00-008.md) |
| [M02](../milestones/M02.md) | M00 (1)، M01 (8) | [TASK-M00-003](../tasks/M00/TASK-M00-003.md)، [TASK-M01-001](../tasks/M01/TASK-M01-001.md)، [TASK-M01-003](../tasks/M01/TASK-M01-003.md)، [TASK-M01-006](../tasks/M01/TASK-M01-006.md)، [TASK-M01-008](../tasks/M01/TASK-M01-008.md)، [TASK-M01-013](../tasks/M01/TASK-M01-013.md)، [TASK-M01-022](../tasks/M01/TASK-M01-022.md)، [TASK-M01-024](../tasks/M01/TASK-M01-024.md) |
| [M03](../milestones/M03.md) | M01 (11)، M02 (3) | [TASK-M01-006](../tasks/M01/TASK-M01-006.md)، [TASK-M01-009](../tasks/M01/TASK-M01-009.md)، [TASK-M01-013](../tasks/M01/TASK-M01-013.md)، [TASK-M01-022](../tasks/M01/TASK-M01-022.md)، [TASK-M01-025](../tasks/M01/TASK-M01-025.md)، [TASK-M01-028](../tasks/M01/TASK-M01-028.md)، [TASK-M01-029](../tasks/M01/TASK-M01-029.md)، [TASK-M01-030](../tasks/M01/TASK-M01-030.md)، [TASK-M02-007](../tasks/M02/TASK-M02-007.md)، [TASK-M02-008](../tasks/M02/TASK-M02-008.md)، [TASK-M02-011](../tasks/M02/TASK-M02-011.md) |
| [M04](../milestones/M04.md) | M00 (1)، M01 (8)، M02 (2)، M03 (3) | [TASK-M00-004](../tasks/M00/TASK-M00-004.md)، [TASK-M01-006](../tasks/M01/TASK-M01-006.md)، [TASK-M01-007](../tasks/M01/TASK-M01-007.md)، [TASK-M01-010](../tasks/M01/TASK-M01-010.md)، [TASK-M01-011](../tasks/M01/TASK-M01-011.md)، [TASK-M01-013](../tasks/M01/TASK-M01-013.md)، [TASK-M01-022](../tasks/M01/TASK-M01-022.md)، [TASK-M01-025](../tasks/M01/TASK-M01-025.md)، [TASK-M02-008](../tasks/M02/TASK-M02-008.md)، [TASK-M03-001](../tasks/M03/TASK-M03-001.md)، [TASK-M03-003](../tasks/M03/TASK-M03-003.md)، [TASK-M03-004](../tasks/M03/TASK-M03-004.md) |
| [M05](../milestones/M05.md) | M01 (6)، M03 (5)، M04 (5) | [TASK-M01-006](../tasks/M01/TASK-M01-006.md)، [TASK-M01-007](../tasks/M01/TASK-M01-007.md)، [TASK-M01-008](../tasks/M01/TASK-M01-008.md)، [TASK-M01-009](../tasks/M01/TASK-M01-009.md)، [TASK-M01-010](../tasks/M01/TASK-M01-010.md)، [TASK-M01-015](../tasks/M01/TASK-M01-015.md)، [TASK-M03-001](../tasks/M03/TASK-M03-001.md)، [TASK-M03-004](../tasks/M03/TASK-M03-004.md)، [TASK-M03-007](../tasks/M03/TASK-M03-007.md)، [TASK-M04-005](../tasks/M04/TASK-M04-005.md)، [TASK-M04-006](../tasks/M04/TASK-M04-006.md)، [TASK-M04-008](../tasks/M04/TASK-M04-008.md)، [TASK-M04-010](../tasks/M04/TASK-M04-010.md)، [TASK-M04-013](../tasks/M04/TASK-M04-013.md) |
| [M06](../milestones/M06.md) | M01 (2)، M02 (1)، M03 (2)، M04 (5)، M05 (6) | [TASK-M01-025](../tasks/M01/TASK-M01-025.md)، [TASK-M01-030](../tasks/M01/TASK-M01-030.md)، [TASK-M02-012](../tasks/M02/TASK-M02-012.md)، [TASK-M03-008](../tasks/M03/TASK-M03-008.md)، [TASK-M03-010](../tasks/M03/TASK-M03-010.md)، [TASK-M04-005](../tasks/M04/TASK-M04-005.md)، [TASK-M04-007](../tasks/M04/TASK-M04-007.md)، [TASK-M04-009](../tasks/M04/TASK-M04-009.md)، [TASK-M04-010](../tasks/M04/TASK-M04-010.md)، [TASK-M04-013](../tasks/M04/TASK-M04-013.md)، [TASK-M05-005](../tasks/M05/TASK-M05-005.md)، [TASK-M05-010](../tasks/M05/TASK-M05-010.md)، [TASK-M05-013](../tasks/M05/TASK-M05-013.md)، [TASK-M05-015](../tasks/M05/TASK-M05-015.md)، [TASK-M05-016](../tasks/M05/TASK-M05-016.md)، [TASK-M05-017](../tasks/M05/TASK-M05-017.md) |
| [M07](../milestones/M07.md) | M00 (2)، M01 (6)، M03 (3)، M04 (3)، M05 (2)، M06 (4) | [TASK-M00-004](../tasks/M00/TASK-M00-004.md)، [TASK-M00-006](../tasks/M00/TASK-M00-006.md)، [TASK-M01-007](../tasks/M01/TASK-M01-007.md)، [TASK-M01-010](../tasks/M01/TASK-M01-010.md)، [TASK-M01-011](../tasks/M01/TASK-M01-011.md)، [TASK-M01-013](../tasks/M01/TASK-M01-013.md)، [TASK-M01-015](../tasks/M01/TASK-M01-015.md)، [TASK-M03-003](../tasks/M03/TASK-M03-003.md)، [TASK-M03-006](../tasks/M03/TASK-M03-006.md)، [TASK-M03-007](../tasks/M03/TASK-M03-007.md)، [TASK-M04-002](../tasks/M04/TASK-M04-002.md)، [TASK-M04-003](../tasks/M04/TASK-M04-003.md)، [TASK-M04-010](../tasks/M04/TASK-M04-010.md)، [TASK-M05-008](../tasks/M05/TASK-M05-008.md)، [TASK-M05-010](../tasks/M05/TASK-M05-010.md)، [TASK-M06-003](../tasks/M06/TASK-M06-003.md)، [TASK-M06-009](../tasks/M06/TASK-M06-009.md) |
| [M08](../milestones/M08.md) | M00 (2)، M01 (5)، M02 (2) | [TASK-M00-004](../tasks/M00/TASK-M00-004.md)، [TASK-M00-006](../tasks/M00/TASK-M00-006.md)، [TASK-M01-022](../tasks/M01/TASK-M01-022.md)، [TASK-M01-025](../tasks/M01/TASK-M01-025.md)، [TASK-M01-026](../tasks/M01/TASK-M01-026.md)، [TASK-M01-027](../tasks/M01/TASK-M01-027.md)، [TASK-M02-005](../tasks/M02/TASK-M02-005.md)، [TASK-M02-008](../tasks/M02/TASK-M02-008.md) |
| [M09](../milestones/M09.md) | M01 (1)، M05 (2)، M07 (4)، M08 (1)، M10 (1) | [TASK-M01-008](../tasks/M01/TASK-M01-008.md)، [TASK-M05-005](../tasks/M05/TASK-M05-005.md)، [TASK-M05-009](../tasks/M05/TASK-M05-009.md)، [TASK-M07-002](../tasks/M07/TASK-M07-002.md)، [TASK-M07-008](../tasks/M07/TASK-M07-008.md)، [TASK-M07-013](../tasks/M07/TASK-M07-013.md)، [TASK-M07-016](../tasks/M07/TASK-M07-016.md)، [TASK-M08-010](../tasks/M08/TASK-M08-010.md)، [TASK-M10-001](../tasks/M10/TASK-M10-001.md) |
| [M10](../milestones/M10.md) | M00 (1)، M01 (2)، M02 (3)، M04 (1)، M07 (2) | [TASK-M00-005](../tasks/M00/TASK-M00-005.md)، [TASK-M01-013](../tasks/M01/TASK-M01-013.md)، [TASK-M01-022](../tasks/M01/TASK-M01-022.md)، [TASK-M02-001](../tasks/M02/TASK-M02-001.md)، [TASK-M02-005](../tasks/M02/TASK-M02-005.md)، [TASK-M04-006](../tasks/M04/TASK-M04-006.md)، [TASK-M07-006](../tasks/M07/TASK-M07-006.md)، [TASK-M07-019](../tasks/M07/TASK-M07-019.md) |
| [M11](../milestones/M11.md) | M01 (2)، M05 (1)، M06 (1)، M07 (2)، M08 (2)، M09 (4)، M10 (1) | [TASK-M01-023](../tasks/M01/TASK-M01-023.md)، [TASK-M01-026](../tasks/M01/TASK-M01-026.md)، [TASK-M05-015](../tasks/M05/TASK-M05-015.md)، [TASK-M06-007](../tasks/M06/TASK-M06-007.md)، [TASK-M07-011](../tasks/M07/TASK-M07-011.md)، [TASK-M07-019](../tasks/M07/TASK-M07-019.md)، [TASK-M08-006](../tasks/M08/TASK-M08-006.md)، [TASK-M08-007](../tasks/M08/TASK-M08-007.md)، [TASK-M09-003](../tasks/M09/TASK-M09-003.md)، [TASK-M09-006](../tasks/M09/TASK-M09-006.md)، [TASK-M09-007](../tasks/M09/TASK-M09-007.md)، [TASK-M09-008](../tasks/M09/TASK-M09-008.md)، [TASK-M10-009](../tasks/M10/TASK-M10-009.md) |
| [M12](../milestones/M12.md) | M03 (1)، M04 (1)، M05 (1)، M07 (4)، M08 (7)، M09 (1)، M10 (1)، M11 (2) | [TASK-M03-011](../tasks/M03/TASK-M03-011.md)، [TASK-M04-003](../tasks/M04/TASK-M04-003.md)، [TASK-M05-014](../tasks/M05/TASK-M05-014.md)، [TASK-M07-003](../tasks/M07/TASK-M07-003.md)، [TASK-M07-010](../tasks/M07/TASK-M07-010.md)، [TASK-M07-016](../tasks/M07/TASK-M07-016.md)، [TASK-M07-019](../tasks/M07/TASK-M07-019.md)، [TASK-M08-002](../tasks/M08/TASK-M08-002.md)، [TASK-M08-006](../tasks/M08/TASK-M08-006.md)، [TASK-M08-008](../tasks/M08/TASK-M08-008.md)، [TASK-M09-003](../tasks/M09/TASK-M09-003.md)، [TASK-M10-007](../tasks/M10/TASK-M10-007.md)، [TASK-M11-009](../tasks/M11/TASK-M11-009.md) |
| [M13](../milestones/M13.md) | M06 (1)، M07 (1)، M11 (1)، M12 (18) | [TASK-M06-005](../tasks/M06/TASK-M06-005.md)، [TASK-M07-015](../tasks/M07/TASK-M07-015.md)، [TASK-M11-009](../tasks/M11/TASK-M11-009.md)، [TASK-M12-002](../tasks/M12/TASK-M12-002.md)، [TASK-M12-003](../tasks/M12/TASK-M12-003.md)، [TASK-M12-007](../tasks/M12/TASK-M12-007.md)، [TASK-M12-009](../tasks/M12/TASK-M12-009.md)، [TASK-M12-010](../tasks/M12/TASK-M12-010.md)، [TASK-M12-011](../tasks/M12/TASK-M12-011.md)، [TASK-M12-012](../tasks/M12/TASK-M12-012.md)، [TASK-M12-013](../tasks/M12/TASK-M12-013.md)، [TASK-M12-014](../tasks/M12/TASK-M12-014.md)، [TASK-M12-015](../tasks/M12/TASK-M12-015.md)، [TASK-M12-016](../tasks/M12/TASK-M12-016.md)، [TASK-M12-017](../tasks/M12/TASK-M12-017.md)، [TASK-M12-018](../tasks/M12/TASK-M12-018.md) |
| [M14](../milestones/M14.md) | M11 (1)، M13 (3) | [TASK-M11-004](../tasks/M11/TASK-M11-004.md)، [TASK-M13-008](../tasks/M13/TASK-M13-008.md) |

## (د) المسارات المتوازية: موجات كل مرحلة

**الموجة** = 1 + أطول عمق اعتماد داخل المرحلة نفسها (المهمة بلا اعتماد داخلي في الموجة 1). مهام الموجة الواحدة لا يعتمد بعضها على بعض، فتُنفَّذ بالتوازي بشرط أن تكون اعتماداتها الخارجية (الجدول ج) `Done`. العمود "عمق عام" هو أطول سلسلة من أول الخطة (0 = بلا اعتمادات) ويفيد في ترتيب المراحل المتداخلة. تنبيه AGENTS.md §4: لا تفتح نفس المشهد في مهمتين متوازيتين.

### M00

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M00-001](../tasks/M00/TASK-M00-001.md) (M، 0)، [TASK-M00-003](../tasks/M00/TASK-M00-003.md) (S، 0)، [TASK-M00-004](../tasks/M00/TASK-M00-004.md) (M، 0)، [TASK-M00-006](../tasks/M00/TASK-M00-006.md) (S، 0)، [TASK-M00-007](../tasks/M00/TASK-M00-007.md) (S، 0)، [TASK-M00-008](../tasks/M00/TASK-M00-008.md) (S، 0) | 8 |
| 2 | [TASK-M00-002](../tasks/M00/TASK-M00-002.md) (S، 1)، [TASK-M00-005](../tasks/M00/TASK-M00-005.md) (S، 1) | 2 |

### M01

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M01-001](../tasks/M01/TASK-M01-001.md) (S، 2)، [TASK-M01-019](../tasks/M01/TASK-M01-019.md) (S، 1) | 2 |
| 2 | [TASK-M01-002](../tasks/M01/TASK-M01-002.md) (S، 3)، [TASK-M01-003](../tasks/M01/TASK-M01-003.md) (S، 3)، [TASK-M01-005](../tasks/M01/TASK-M01-005.md) (S، 3) | 3 |
| 3 | [TASK-M01-004](../tasks/M01/TASK-M01-004.md) (M، 4)، [TASK-M01-006](../tasks/M01/TASK-M01-006.md) (S، 4)، [TASK-M01-007](../tasks/M01/TASK-M01-007.md) (S، 4)، [TASK-M01-008](../tasks/M01/TASK-M01-008.md) (S، 4)، [TASK-M01-012](../tasks/M01/TASK-M01-012.md) (S، 4)، [TASK-M01-016](../tasks/M01/TASK-M01-016.md) (S، 4)، [TASK-M01-024](../tasks/M01/TASK-M01-024.md) (S، 4) | 8 |
| 4 | [TASK-M01-009](../tasks/M01/TASK-M01-009.md) (L، 5)، [TASK-M01-017](../tasks/M01/TASK-M01-017.md) (M، 5)، [TASK-M01-018](../tasks/M01/TASK-M01-018.md) (M، 5)، [TASK-M01-025](../tasks/M01/TASK-M01-025.md) (M، 5)، [TASK-M01-028](../tasks/M01/TASK-M01-028.md) (M، 5) | 12 |
| 5 | [TASK-M01-010](../tasks/M01/TASK-M01-010.md) (S، 6)، [TASK-M01-011](../tasks/M01/TASK-M01-011.md) (M، 6)، [TASK-M01-020](../tasks/M01/TASK-M01-020.md) (M، 6)، [TASK-M01-021](../tasks/M01/TASK-M01-021.md) (M، 6)، [TASK-M01-023](../tasks/M01/TASK-M01-023.md) (S، 6)، [TASK-M01-026](../tasks/M01/TASK-M01-026.md) (M، 6)، [TASK-M01-027](../tasks/M01/TASK-M01-027.md) (M، 6)، [TASK-M01-029](../tasks/M01/TASK-M01-029.md) (M، 6) | 14 |
| 6 | [TASK-M01-013](../tasks/M01/TASK-M01-013.md) (L، 7)، [TASK-M01-022](../tasks/M01/TASK-M01-022.md) (S، 7)، [TASK-M01-030](../tasks/M01/TASK-M01-030.md) (S، 7) | 6 |
| 7 | [TASK-M01-014](../tasks/M01/TASK-M01-014.md) (M، 8) | 2 |
| 8 | [TASK-M01-015](../tasks/M01/TASK-M01-015.md) (M، 9) | 2 |

### M02

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M02-001](../tasks/M02/TASK-M02-001.md) (S، 4)، [TASK-M02-005](../tasks/M02/TASK-M02-005.md) (M، 3) | 3 |
| 2 | [TASK-M02-002](../tasks/M02/TASK-M02-002.md) (M، 5)، [TASK-M02-006](../tasks/M02/TASK-M02-006.md) (S، 4)، [TASK-M02-010](../tasks/M02/TASK-M02-010.md) (S، 5)، [TASK-M02-011](../tasks/M02/TASK-M02-011.md) (S، 5)، [TASK-M02-012](../tasks/M02/TASK-M02-012.md) (M، 8) | 7 |
| 3 | [TASK-M02-003](../tasks/M02/TASK-M02-003.md) (S، 6)، [TASK-M02-004](../tasks/M02/TASK-M02-004.md) (S، 6)، [TASK-M02-007](../tasks/M02/TASK-M02-007.md) (S، 5)، [TASK-M02-008](../tasks/M02/TASK-M02-008.md) (M، 6) | 5 |
| 4 | [TASK-M02-009](../tasks/M02/TASK-M02-009.md) (S، 8) | 1 |

### M03

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M03-001](../tasks/M03/TASK-M03-001.md) (S، 6)، [TASK-M03-010](../tasks/M03/TASK-M03-010.md) (S، 8) | 2 |
| 2 | [TASK-M03-002](../tasks/M03/TASK-M03-002.md) (M، 7)، [TASK-M03-008](../tasks/M03/TASK-M03-008.md) (M، 7) | 4 |
| 3 | [TASK-M03-003](../tasks/M03/TASK-M03-003.md) (M، 8)، [TASK-M03-005](../tasks/M03/TASK-M03-005.md) (M، 8)، [TASK-M03-009](../tasks/M03/TASK-M03-009.md) (M، 8) | 6 |
| 4 | [TASK-M03-004](../tasks/M03/TASK-M03-004.md) (S، 9)، [TASK-M03-006](../tasks/M03/TASK-M03-006.md) (M، 9)، [TASK-M03-007](../tasks/M03/TASK-M03-007.md) (M، 9)، [TASK-M03-011](../tasks/M03/TASK-M03-011.md) (S، 9) | 6 |

### M04

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M04-001](../tasks/M04/TASK-M04-001.md) (S، 6) | 1 |
| 2 | [TASK-M04-002](../tasks/M04/TASK-M04-002.md) (M، 8)، [TASK-M04-003](../tasks/M04/TASK-M04-003.md) (M، 7)، [TASK-M04-004](../tasks/M04/TASK-M04-004.md) (S، 7)، [TASK-M04-006](../tasks/M04/TASK-M04-006.md) (L، 7) | 9 |
| 3 | [TASK-M04-005](../tasks/M04/TASK-M04-005.md) (M، 9)، [TASK-M04-007](../tasks/M04/TASK-M04-007.md) (S، 8)، [TASK-M04-008](../tasks/M04/TASK-M04-008.md) (M، 10)، [TASK-M04-009](../tasks/M04/TASK-M04-009.md) (M، 9) | 7 |
| 4 | [TASK-M04-010](../tasks/M04/TASK-M04-010.md) (M، 10)، [TASK-M04-011](../tasks/M04/TASK-M04-011.md) (S، 10)، [TASK-M04-012](../tasks/M04/TASK-M04-012.md) (M، 10)، [TASK-M04-014](../tasks/M04/TASK-M04-014.md) (M، 10) | 7 |
| 5 | [TASK-M04-013](../tasks/M04/TASK-M04-013.md) (M، 11)، [TASK-M04-015](../tasks/M04/TASK-M04-015.md) (M، 11)، [TASK-M04-016](../tasks/M04/TASK-M04-016.md) (S، 11) | 5 |

### M05

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M05-001](../tasks/M05/TASK-M05-001.md) (M، 10)، [TASK-M05-002](../tasks/M05/TASK-M05-002.md) (M، 7)، [TASK-M05-004](../tasks/M05/TASK-M05-004.md) (S، 7) | 5 |
| 2 | [TASK-M05-003](../tasks/M05/TASK-M05-003.md) (M، 11) | 2 |
| 3 | [TASK-M05-005](../tasks/M05/TASK-M05-005.md) (L، 12)، [TASK-M05-007](../tasks/M05/TASK-M05-007.md) (S، 12)، [TASK-M05-008](../tasks/M05/TASK-M05-008.md) (M، 12)، [TASK-M05-013](../tasks/M05/TASK-M05-013.md) (L، 12)، [TASK-M05-016](../tasks/M05/TASK-M05-016.md) (M، 12) | 13 |
| 4 | [TASK-M05-006](../tasks/M05/TASK-M05-006.md) (S، 13)، [TASK-M05-009](../tasks/M05/TASK-M05-009.md) (M، 13)، [TASK-M05-011](../tasks/M05/TASK-M05-011.md) (S، 13)، [TASK-M05-014](../tasks/M05/TASK-M05-014.md) (M، 13)، [TASK-M05-015](../tasks/M05/TASK-M05-015.md) (L، 13)، [TASK-M05-017](../tasks/M05/TASK-M05-017.md) (M، 13) | 12 |
| 5 | [TASK-M05-010](../tasks/M05/TASK-M05-010.md) (M، 14)، [TASK-M05-012](../tasks/M05/TASK-M05-012.md) (S، 14) | 3 |

### M06

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M06-001](../tasks/M06/TASK-M06-001.md) (M، 15)، [TASK-M06-002](../tasks/M06/TASK-M06-002.md) (S، 6)، [TASK-M06-004](../tasks/M06/TASK-M06-004.md) (S، 14)، [TASK-M06-005](../tasks/M06/TASK-M06-005.md) (M، 14)، [TASK-M06-006](../tasks/M06/TASK-M06-006.md) (M، 13)، [TASK-M06-007](../tasks/M06/TASK-M06-007.md) (S، 0) | 9 |
| 2 | [TASK-M06-003](../tasks/M06/TASK-M06-003.md) (M، 9) | 2 |
| 3 | [TASK-M06-008](../tasks/M06/TASK-M06-008.md) (M، 16) | 2 |
| 4 | [TASK-M06-009](../tasks/M06/TASK-M06-009.md) (S، 17) | 1 |

### M07

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M07-001](../tasks/M07/TASK-M07-001.md) (M، 18)، [TASK-M07-002](../tasks/M07/TASK-M07-002.md) (M، 18)، [TASK-M07-003](../tasks/M07/TASK-M07-003.md) (M، 18) | 6 |
| 2 | [TASK-M07-004](../tasks/M07/TASK-M07-004.md) (L، 19)، [TASK-M07-007](../tasks/M07/TASK-M07-007.md) (M، 19)، [TASK-M07-016](../tasks/M07/TASK-M07-016.md) (S، 19) | 7 |
| 3 | [TASK-M07-005](../tasks/M07/TASK-M07-005.md) (S، 20)، [TASK-M07-006](../tasks/M07/TASK-M07-006.md) (M، 20)، [TASK-M07-008](../tasks/M07/TASK-M07-008.md) (M، 20)، [TASK-M07-011](../tasks/M07/TASK-M07-011.md) (M، 20)، [TASK-M07-012](../tasks/M07/TASK-M07-012.md) (S، 20)، [TASK-M07-017](../tasks/M07/TASK-M07-017.md) (L، 20) | 12 |
| 4 | [TASK-M07-009](../tasks/M07/TASK-M07-009.md) (M، 21)، [TASK-M07-010](../tasks/M07/TASK-M07-010.md) (M، 21)، [TASK-M07-013](../tasks/M07/TASK-M07-013.md) (S، 21) | 5 |
| 5 | [TASK-M07-014](../tasks/M07/TASK-M07-014.md) (M، 22)، [TASK-M07-015](../tasks/M07/TASK-M07-015.md) (S، 22)، [TASK-M07-018](../tasks/M07/TASK-M07-018.md) (M، 22) | 5 |
| 6 | [TASK-M07-019](../tasks/M07/TASK-M07-019.md) (M، 23) | 2 |

### M08

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M08-001](../tasks/M08/TASK-M08-001.md) (M، 4)، [TASK-M08-002](../tasks/M08/TASK-M08-002.md) (M، 7)، [TASK-M08-003](../tasks/M08/TASK-M08-003.md) (S، 7)، [TASK-M08-007](../tasks/M08/TASK-M08-007.md) (M، 8)، [TASK-M08-008](../tasks/M08/TASK-M08-008.md) (M، 7) | 9 |
| 2 | [TASK-M08-004](../tasks/M08/TASK-M08-004.md) (L، 8)، [TASK-M08-009](../tasks/M08/TASK-M08-009.md) (S، 9)، [TASK-M08-010](../tasks/M08/TASK-M08-010.md) (S، 8) | 6 |
| 3 | [TASK-M08-005](../tasks/M08/TASK-M08-005.md) (M، 9) | 2 |
| 4 | [TASK-M08-006](../tasks/M08/TASK-M08-006.md) (M، 10) | 2 |
| 5 | [TASK-M08-011](../tasks/M08/TASK-M08-011.md) (M، 11) | 2 |

### M09

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M09-001](../tasks/M09/TASK-M09-001.md) (S، 22)، [TASK-M09-004](../tasks/M09/TASK-M09-004.md) (M، 13) | 3 |
| 2 | [TASK-M09-002](../tasks/M09/TASK-M09-002.md) (M، 23)، [TASK-M09-005](../tasks/M09/TASK-M09-005.md) (M، 21) | 4 |
| 3 | [TASK-M09-003](../tasks/M09/TASK-M09-003.md) (M، 24)، [TASK-M09-006](../tasks/M09/TASK-M09-006.md) (S، 22)، [TASK-M09-007](../tasks/M09/TASK-M09-007.md) (M، 22)، [TASK-M09-009](../tasks/M09/TASK-M09-009.md) (S، 24) | 6 |
| 4 | [TASK-M09-008](../tasks/M09/TASK-M09-008.md) (S، 25) | 1 |

### M10

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M10-001](../tasks/M10/TASK-M10-001.md) (M، 8)، [TASK-M10-006](../tasks/M10/TASK-M10-006.md) (M، 2)، [TASK-M10-010](../tasks/M10/TASK-M10-010.md) (M، 4)، [TASK-M10-011](../tasks/M10/TASK-M10-011.md) (M، 8)، [TASK-M10-012](../tasks/M10/TASK-M10-012.md) (M، 24) | 10 |
| 2 | [TASK-M10-002](../tasks/M10/TASK-M10-002.md) (M، 9)، [TASK-M10-003](../tasks/M10/TASK-M10-003.md) (S، 9)، [TASK-M10-004](../tasks/M10/TASK-M10-004.md) (M، 9)، [TASK-M10-007](../tasks/M10/TASK-M10-007.md) (XL، 4)، [TASK-M10-008](../tasks/M10/TASK-M10-008.md) (XL، 3) | 21 |
| 3 | [TASK-M10-005](../tasks/M10/TASK-M10-005.md) (M، 9)، [TASK-M10-009](../tasks/M10/TASK-M10-009.md) (M، 5)، [TASK-M10-013](../tasks/M10/TASK-M10-013.md) (S، 10)، [TASK-M10-014](../tasks/M10/TASK-M10-014.md) (S، 21) | 6 |

### M11

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M11-001](../tasks/M11/TASK-M11-001.md) (M، 21) | 2 |
| 2 | [TASK-M11-002](../tasks/M11/TASK-M11-002.md) (L، 25) | 4 |
| 3 | [TASK-M11-003](../tasks/M11/TASK-M11-003.md) (M، 26)، [TASK-M11-004](../tasks/M11/TASK-M11-004.md) (M، 26)، [TASK-M11-005](../tasks/M11/TASK-M11-005.md) (S، 26) | 5 |
| 4 | [TASK-M11-006](../tasks/M11/TASK-M11-006.md) (M، 27)، [TASK-M11-008](../tasks/M11/TASK-M11-008.md) (S، 27) | 3 |
| 5 | [TASK-M11-007](../tasks/M11/TASK-M11-007.md) (M، 28) | 2 |
| 6 | [TASK-M11-009](../tasks/M11/TASK-M11-009.md) (S، 29) | 1 |

### M12

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M12-001](../tasks/M12/TASK-M12-001.md) (L، 30)، [TASK-M12-009](../tasks/M12/TASK-M12-009.md) (L، 30)، [TASK-M12-010](../tasks/M12/TASK-M12-010.md) (L، 11)، [TASK-M12-011](../tasks/M12/TASK-M12-011.md) (L، 11)، [TASK-M12-012](../tasks/M12/TASK-M12-012.md) (L، 11)، [TASK-M12-013](../tasks/M12/TASK-M12-013.md) (M، 25) | 22 |
| 2 | [TASK-M12-002](../tasks/M12/TASK-M12-002.md) (XL، 31)، [TASK-M12-003](../tasks/M12/TASK-M12-003.md) (L، 31)، [TASK-M12-016](../tasks/M12/TASK-M12-016.md) (M، 31) | 14 |
| 3 | [TASK-M12-004](../tasks/M12/TASK-M12-004.md) (M، 32)، [TASK-M12-005](../tasks/M12/TASK-M12-005.md) (M، 32)، [TASK-M12-006](../tasks/M12/TASK-M12-006.md) (M، 32)، [TASK-M12-007](../tasks/M12/TASK-M12-007.md) (M، 32)، [TASK-M12-008](../tasks/M12/TASK-M12-008.md) (M، 32)، [TASK-M12-014](../tasks/M12/TASK-M12-014.md) (XL، 32)، [TASK-M12-015](../tasks/M12/TASK-M12-015.md) (XL، 32)، [TASK-M12-019](../tasks/M12/TASK-M12-019.md) (M، 32) | 28 |
| 4 | [TASK-M12-017](../tasks/M12/TASK-M12-017.md) (XL، 33)، [TASK-M12-018](../tasks/M12/TASK-M12-018.md) (L، 33) | 12 |

### M13

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M13-001](../tasks/M13/TASK-M13-001.md) (M، 31)، [TASK-M13-002](../tasks/M13/TASK-M13-002.md) (L، 32)، [TASK-M13-003](../tasks/M13/TASK-M13-003.md) (L، 34)، [TASK-M13-004](../tasks/M13/TASK-M13-004.md) (XL، 34)، [TASK-M13-009](../tasks/M13/TASK-M13-009.md) (S، 30) | 19 |
| 2 | [TASK-M13-005](../tasks/M13/TASK-M13-005.md) (S، 35)، [TASK-M13-006](../tasks/M13/TASK-M13-006.md) (L، 35) | 5 |
| 3 | [TASK-M13-007](../tasks/M13/TASK-M13-007.md) (L، 36) | 4 |
| 4 | [TASK-M13-008](../tasks/M13/TASK-M13-008.md) (M، 37) | 2 |
| 5 | [TASK-M13-010](../tasks/M13/TASK-M13-010.md) (S، 38) | 1 |

### M14

| الموجة | المهام (الحجم، عمق عام) | النقاط |
|---|---|---|
| 1 | [TASK-M14-001](../tasks/M14/TASK-M14-001.md) (S، 38)، [TASK-M14-004](../tasks/M14/TASK-M14-004.md) (S، 38)، [TASK-M14-005](../tasks/M14/TASK-M14-005.md) (S، 38) | 3 |
| 2 | [TASK-M14-002](../tasks/M14/TASK-M14-002.md) (M، 39)، [TASK-M14-003](../tasks/M14/TASK-M14-003.md) (M، 39) | 4 |

## (هـ) أكبر المهام فتحاً لغيرها (Top 15)

مرتبة بعدد المعتمدين المباشرين ثم غير المباشرين. تُستخدم كمعيار ترجيح أخير في اختيار المهمة التالية (AGENTS.md §3، [PRIORITIES](PRIORITIES.md)).

| # | المهمة | العنوان | الأولوية | الحالة | مباشر | كل اللاحقين |
|---|---|---|---|---|---|---|
| 1 | [TASK-M12-003](../tasks/M12/TASK-M12-003.md) | إعداد الأدوار الإحدى عشرة بسماتها وجداولها وأسرها | Critical | Todo | 10 | 23 |
| 2 | [TASK-M02-005](../tasks/M02/TASK-M02-005.md) | مخطط السوق الرمادي (دكان اللاعب والمنافس والميزان العام والبئر) | Critical | Todo | 8 | 110 |
| 3 | [TASK-M01-025](../tasks/M01/TASK-M01-025.md) | مخططات المحتوى JSON (Line وStorySegment والمصادر الدينية) | Critical | Todo | 7 | 141 |
| 4 | [TASK-M01-013](../tasks/M01/TASK-M01-013.md) | لقطة الحفظ وSaveManager وISaveStorage المحلي | Critical | Todo | 7 | 111 |
| 5 | [TASK-M05-005](../tasks/M05/TASK-M05-005.md) | دورة الشائعات (FR-E6 وFR-M3) | Critical | Todo | 7 | 80 |
| 6 | [TASK-M01-003](../tasks/M01/TASK-M01-003.md) | تثبيت الحزم الأساسية (Input System وCinemachine وAI Navigation وLocalization وYarn Spinner وNewtonsoft وTest Framework) | Critical | Todo | 6 | 168 |
| 7 | [TASK-M01-006](../tasks/M01/TASK-M01-006.md) | ساعة اللعبة GameClock (يوم ووقت وفواصل ثابتة) | Critical | Todo | 6 | 121 |
| 8 | [TASK-M03-001](../tasks/M03/TASK-M03-001.md) | تعريف بيانات الشخصيات (المعرّف والدور والسمات) | Critical | Todo | 6 | 113 |
| 9 | [TASK-M04-010](../tasks/M04/TASK-M04-010.md) | الغش بالكيل والصنجات CHEAT_SCALE | Critical | Todo | 6 | 80 |
| 10 | [TASK-M05-008](../tasks/M05/TASK-M05-008.md) | الثقة والمودة لكل شخصية ومعالج العلاقات | Critical | Todo | 6 | 79 |
| 11 | [TASK-M01-002](../tasks/M01/TASK-M01-002.md) | هيكل المجلدات وملفات Assembly Definition | Critical | Todo | 5 | 157 |
| 12 | [TASK-M01-007](../tasks/M01/TASK-M01-007.md) | مولد عشوائي ببذرة وحالة قابلة للحفظ SeededRng | Critical | Todo | 5 | 119 |
| 13 | [TASK-M01-011](../tasks/M01/TASK-M01-011.md) | طابور الأحداث المؤجلة ScheduledEventQueue (FR-E5) | Critical | Todo | 5 | 112 |
| 14 | [TASK-M02-008](../tasks/M02/TASK-M02-008.md) | نظام التفاعل (اكتشاف وتلميح وتنفيذ) | Critical | Todo | 5 | 101 |
| 15 | [TASK-M05-003](../tasks/M05/TASK-M05-003.md) | معالج الذاكرة: معتقدات للشهود والضحايا | Critical | Todo | 5 | 89 |

## طريقة إعادة التوليد

الملف مولَّد بسكربت Python يقرأ [TASKS.csv](TASKS.csv) فقط (لا يعدّله). الخوارزمية:

1. تحليل `dependencies` (مفصولة بـ `;`) مع حذف التكرار (المزامنة تكتب كل معرّف مرتين: نص الرابط وعنوانه)، والتحقق أن كل معرّف موجود. عدد الحواف = عدد الأزواج الفريدة.
2. فرز طوبولوجي (Kahn)؛ فشله يعني دورة ويجب إصلاحها في ملفات المهام.
3. المسار الحرج: `best[n] = w[n] + max(best[d] for d in deps)` بالترتيب الطوبولوجي، ثم تتبع `prev` من TASK-M13-010.
4. الموجات: `wave[n] = 1 + max(wave[d] for d in deps if same milestone)`؛ العمق العام بالمثل على كل الاعتمادات.
5. أكبر الفاتحين: عدد الأبناء المباشرين، ثم حجم مجموعة اللاحقين بالبحث في الرسم.

```python
import csv
W={'S':1,'M':2,'L':4,'XL':8}
R={r['id']:r for r in csv.DictReader(open('planning/TASKS.csv',encoding='utf-8'))}
D={i:list(dict.fromkeys(d for d in r['dependencies'].split(';') if d)) for i,r in R.items()}
order,seen=[],set()
def visit(n):
    if n in seen: return
    seen.add(n); [visit(d) for d in D[n]]; order.append(n)
for n in sorted(R): visit(n)
best,prev={},{}
for n in order:
    p=max(D[n],key=lambda d:best[d],default=None)
    best[n]=W[R[n]['complexity']]+(best[p] if p else 0); prev[n]=p
n,path='TASK-M13-010',[]
while n: path.append(n); n=prev[n]
print(best['TASK-M13-010'],path[::-1])
```

إذا أُضيف أمر توليد إلى `tools/plan.py` لاحقاً، يصبح هو الطريقة المعتمدة ويُذكر هنا.
