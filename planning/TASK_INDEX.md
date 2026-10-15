# فهرس المهام

> مولَّد آلياً بواسطة `python3 tools/plan.py sync` من ملفات `tasks/`. لا تعدّله يدوياً.

**الإجمالي:** 199 مهمة. **المكتمل:** 1 (0.5% بالعدد، 0.5% بالجهد).

| الحالة | العدد |
|---|---|
| Todo | 191 |
| Ready | 7 |
| In Progress | 0 |
| Blocked | 0 |
| In Review | 0 |
| Done | 1 |

## جاهزة للبدء الآن

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M00-002](../tasks/M00/TASK-M00-002.md) | إكمال إعداد مستودع git (.gitignore لـ Unity وGit LFS وأول commit) | Ready | Critical | DevOps | S | TASK-M00-001 | No |
| [TASK-M00-004](../tasks/M00/TASK-M00-004.md) | اعتماد المراجع الشرعي وتحديد آلية المراجعة على دفعات | Ready | Critical | Religious Review | M | — | Yes |
| [TASK-M00-003](../tasks/M00/TASK-M00-003.md) | سجل تراخيص الطرف الثالث (الحزم والخطوط والمصحف والأصول) | Ready | High | DevOps | S | — | No |
| [TASK-M00-006](../tasks/M00/TASK-M00-006.md) | ملف سجل المصادر الدينية من PRD 9.1 | Ready | High | Writing | S | — | Yes |
| [TASK-M00-007](../tasks/M00/TASK-M00-007.md) | ملف سجل المسائل الشرعية المعلقة SR-01 إلى SR-13 | Ready | High | Writing | S | — | Yes |
| [TASK-M00-008](../tasks/M00/TASK-M00-008.md) | مصفوفة الأجهزة والمتصفحات المستهدفة للاختبار | Ready | Medium | QA | S | — | No |
| [TASK-M06-007](../tasks/M06/TASK-M06-007.md) | بروتوكول اختبار اللعب مع الأطفال واستبيانه وموافقة الأهل | Ready | High | QA | S | — | No |

## [M00](../milestones/M00.md) — 1/8 (12.5% بالعدد، 20.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M00-001](../tasks/M00/TASK-M00-001.md) | إنشاء نظام التخطيط والتتبع ومدقق الاتساق tools/plan.py | Done | Critical | DevOps | M | — | No |
| [TASK-M00-002](../tasks/M00/TASK-M00-002.md) | إكمال إعداد مستودع git (.gitignore لـ Unity وGit LFS وأول commit) | Ready | Critical | DevOps | S | TASK-M00-001 | No |
| [TASK-M00-003](../tasks/M00/TASK-M00-003.md) | سجل تراخيص الطرف الثالث (الحزم والخطوط والمصحف والأصول) | Ready | High | DevOps | S | — | No |
| [TASK-M00-004](../tasks/M00/TASK-M00-004.md) | اعتماد المراجع الشرعي وتحديد آلية المراجعة على دفعات | Ready | Critical | Religious Review | M | — | Yes |
| [TASK-M00-005](../tasks/M00/TASK-M00-005.md) | اسم البلدة الخيالية ووثيقة إعدادها (F1) | Todo | High | Writing | S | TASK-M00-004 | Yes |
| [TASK-M00-006](../tasks/M00/TASK-M00-006.md) | ملف سجل المصادر الدينية من PRD 9.1 | Ready | High | Writing | S | — | Yes |
| [TASK-M00-007](../tasks/M00/TASK-M00-007.md) | ملف سجل المسائل الشرعية المعلقة SR-01 إلى SR-13 | Ready | High | Writing | S | — | Yes |
| [TASK-M00-008](../tasks/M00/TASK-M00-008.md) | مصفوفة الأجهزة والمتصفحات المستهدفة للاختبار | Ready | Medium | QA | S | — | No |

## [M01](../milestones/M01.md) — 0/30 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M01-001](../tasks/M01/TASK-M01-001.md) | إنشاء مشروع Unity 6 بقالب URP وإعداداته الأساسية | Todo | Critical | Programming | S | TASK-M00-002 | No |
| [TASK-M01-002](../tasks/M01/TASK-M01-002.md) | هيكل المجلدات وملفات Assembly Definition | Todo | Critical | Programming | S | TASK-M01-001 | No |
| [TASK-M01-003](../tasks/M01/TASK-M01-003.md) | تثبيت الحزم الأساسية (Input System وCinemachine وAI Navigation وLocalization وYarn Spinner وNewtonsoft وTest Framework) | Todo | Critical | Programming | S | TASK-M01-001, TASK-M00-003 | No |
| [TASK-M01-004](../tasks/M01/TASK-M01-004.md) | تشغيل اختبارات EditMode آلياً في CI | Todo | Critical | DevOps | M | TASK-M01-002 | No |
| [TASK-M01-005](../tasks/M01/TASK-M01-005.md) | سكربت بناء macOS من سطر الأوامر | Todo | High | DevOps | S | TASK-M01-001 | No |
| [TASK-M01-006](../tasks/M01/TASK-M01-006.md) | ساعة اللعبة GameClock (يوم ووقت وفواصل ثابتة) | Todo | Critical | Programming | S | TASK-M01-002 | No |
| [TASK-M01-007](../tasks/M01/TASK-M01-007.md) | مولد عشوائي ببذرة وحالة قابلة للحفظ SeededRng | Todo | Critical | Programming | S | TASK-M01-002 | No |
| [TASK-M01-008](../tasks/M01/TASK-M01-008.md) | نموذج GameEvent وأنواع الأحداث | Todo | Critical | Programming | S | TASK-M01-002 | No |
| [TASK-M01-009](../tasks/M01/TASK-M01-009.md) | سجل القرارات DecisionLog وخط المعالجة FR-E4 | Todo | Critical | Programming | L | TASK-M01-006, TASK-M01-008 | No |
| [TASK-M01-010](../tasks/M01/TASK-M01-010.md) | منع التكرار عبر lastProcessedSeq لكل معالج (FR-E7) | Todo | Critical | Programming | S | TASK-M01-009 | No |
| [TASK-M01-011](../tasks/M01/TASK-M01-011.md) | طابور الأحداث المؤجلة ScheduledEventQueue (FR-E5) | Todo | Critical | Programming | M | TASK-M01-009 | No |
| [TASK-M01-012](../tasks/M01/TASK-M01-012.md) | تسلسل JSON قانوني بترتيب مفاتيح ثابت | Todo | Critical | Programming | S | TASK-M01-003 | No |
| [TASK-M01-013](../tasks/M01/TASK-M01-013.md) | لقطة الحفظ وSaveManager وISaveStorage المحلي | Todo | Critical | Programming | L | TASK-M01-007, TASK-M01-010, TASK-M01-011, TASK-M01-012 | No |
| [TASK-M01-014](../tasks/M01/TASK-M01-014.md) | ترقيم إصدار المخطط والترحيل (T7) | Todo | High | Programming | M | TASK-M01-013 | No |
| [TASK-M01-015](../tasks/M01/TASK-M01-015.md) | اختبارات الحفظ T1 وT7 وT8 في CI | Todo | Critical | QA | M | TASK-M01-014, TASK-M01-004 | No |
| [TASK-M01-016](../tasks/M01/TASK-M01-016.md) | مشهد اختبار النقل (شخصية متحركة بسيطة) | Todo | High | Programming | S | TASK-M01-003 | No |
| [TASK-M01-017](../tasks/M01/TASK-M01-017.md) | بناء WebGL تجريبي وقياس الأداء والحجم | Todo | High | DevOps | M | TASK-M01-016, TASK-M01-005, TASK-M00-008 | No |
| [TASK-M01-018](../tasks/M01/TASK-M01-018.md) | بناء جوال تجريبي على جهاز واحد وقياسه | Todo | High | DevOps | M | TASK-M01-016, TASK-M01-005, TASK-M00-008 | No |
| [TASK-M01-019](../tasks/M01/TASK-M01-019.md) | التحقق من تراخيص الخطوط العربية والعثمانية | Todo | High | DevOps | S | TASK-M00-003 | No |
| [TASK-M01-020](../tasks/M01/TASK-M01-020.md) | اختبار العربية A: UI Toolkit مع Advanced Text Generator | Todo | Critical | Programming | M | TASK-M01-017, TASK-M01-018, TASK-M01-019 | Yes |
| [TASK-M01-021](../tasks/M01/TASK-M01-021.md) | اختبار العربية B: TextMeshPro مع RTLTMPro | Todo | Critical | Programming | M | TASK-M01-017, TASK-M01-018, TASK-M01-019 | Yes |
| [TASK-M01-022](../tasks/M01/TASK-M01-022.md) | قرار عرض العربية المكتوب (الواجهة والنص في العالم والآيات) | Todo | Critical | Design | S | TASK-M01-020, TASK-M01-021, TASK-M00-004 | Yes |
| [TASK-M01-023](../tasks/M01/TASK-M01-023.md) | تقرير قابلية النقل للويب والجوال | Todo | Critical | QA | S | TASK-M01-017, TASK-M01-018 | No |
| [TASK-M01-024](../tasks/M01/TASK-M01-024.md) | إعداد Unity Localization ولغة العربية واصطلاح المفاتيح | Todo | High | Programming | S | TASK-M01-003 | No |
| [TASK-M01-025](../tasks/M01/TASK-M01-025.md) | مخططات المحتوى JSON (Line وStorySegment والمصادر الدينية) | Todo | Critical | Programming | M | TASK-M01-002, TASK-M00-006, TASK-M01-012 | Yes |
| [TASK-M01-026](../tasks/M01/TASK-M01-026.md) | بوابة البناء لفحص المحتوى الديني (FR-Q1 وFR-Q2 وFR-Q3) | Todo | Critical | Programming | M | TASK-M01-025, TASK-M01-004 | Yes |
| [TASK-M01-027](../tasks/M01/TASK-M01-027.md) | استيراد مصحف Tanzil واستخراج الآيات بالإحالة (FR-N2) | Todo | High | Programming | M | TASK-M01-025, TASK-M00-003 | Yes |
| [TASK-M01-028](../tasks/M01/TASK-M01-028.md) | هيكل Yarn Spinner مع مفاتيح الترجمة | Todo | High | Programming | M | TASK-M01-003, TASK-M01-024 | No |
| [TASK-M01-029](../tasks/M01/TASK-M01-029.md) | محدد السطور بالقواعد (الشروط والأولوية والمهلة وonce) | Todo | Critical | Programming | M | TASK-M01-025, TASK-M01-007 | No |
| [TASK-M01-030](../tasks/M01/TASK-M01-030.md) | واجهة IDialogueProvider ومزود القواعد | Todo | High | Programming | S | TASK-M01-029 | No |

## [M02](../milestones/M02.md) — 0/12 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M02-001](../tasks/M02/TASK-M02-001.md) | ملف Input Actions (حركة ونظر وتفاعل وقائمة) قابل لإعادة التعيين | Todo | Critical | Programming | S | TASK-M01-003 | No |
| [TASK-M02-002](../tasks/M02/TASK-M02-002.md) | متحكم الشخصية بالشخص الثالث | Todo | Critical | Programming | M | TASK-M02-001 | No |
| [TASK-M02-003](../tasks/M02/TASK-M02-003.md) | كاميرا Cinemachine بالشخص الثالث مع تفادي التصادم | Todo | High | Programming | S | TASK-M02-002 | No |
| [TASK-M02-004](../tasks/M02/TASK-M02-004.md) | شخصية لاعب مؤقتة مع حركات أساسية | Todo | Medium | Art | S | TASK-M02-002, TASK-M00-003 | No |
| [TASK-M02-005](../tasks/M02/TASK-M02-005.md) | مخطط السوق الرمادي (دكان اللاعب والمنافس والميزان العام والبئر) | Todo | Critical | Design | M | TASK-M01-001 | No |
| [TASK-M02-006](../tasks/M02/TASK-M02-006.md) | بيت اللاعب وحي سكني رمادي | Todo | Medium | Design | S | TASK-M02-005 | No |
| [TASK-M02-007](../tasks/M02/TASK-M02-007.md) | خبز NavMesh للمنطقة الرمادية | Todo | High | Programming | S | TASK-M02-005, TASK-M01-003, TASK-M02-006 | No |
| [TASK-M02-008](../tasks/M02/TASK-M02-008.md) | نظام التفاعل (اكتشاف وتلميح وتنفيذ) | Todo | Critical | Programming | M | TASK-M02-002 | No |
| [TASK-M02-009](../tasks/M02/TASK-M02-009.md) | تلميح التفاعل بالعربية داخل العالم | Todo | Medium | Programming | S | TASK-M02-008, TASK-M01-022, TASK-M01-024 | No |
| [TASK-M02-010](../tasks/M02/TASK-M02-010.md) | إضاءة الليل والنهار مرتبطة بساعة اللعبة | Todo | Low | Programming | S | TASK-M02-005, TASK-M01-006 | No |
| [TASK-M02-011](../tasks/M02/TASK-M02-011.md) | سجل الأماكن locationId | Todo | High | Programming | S | TASK-M02-005, TASK-M01-008 | No |
| [TASK-M02-012](../tasks/M02/TASK-M02-012.md) | جذر التركيب GameRoot لربط أنظمة المحاكاة بالمشهد | Todo | Critical | Programming | M | TASK-M01-013, TASK-M02-005 | No |

## [M03](../milestones/M03.md) — 0/11 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M03-001](../tasks/M03/TASK-M03-001.md) | تعريف بيانات الشخصيات (المعرّف والدور والسمات) | Todo | Critical | Programming | S | TASK-M01-025 | No |
| [TASK-M03-002](../tasks/M03/TASK-M03-002.md) | وكيل NPC بالحركة على NavMesh ونموذج مؤقت | Todo | Critical | Programming | M | TASK-M02-007, TASK-M03-001 | No |
| [TASK-M03-003](../tasks/M03/TASK-M03-003.md) | جداول يومية للشخصيات مرتبطة بالساعة | Todo | High | Programming | M | TASK-M03-002, TASK-M01-006, TASK-M02-011, TASK-M01-013 | No |
| [TASK-M03-004](../tasks/M03/TASK-M03-004.md) | كثافة الزحام لكل مكان حسب الوقت | Todo | Medium | Programming | S | TASK-M03-003 | No |
| [TASK-M03-005](../tasks/M03/TASK-M03-005.md) | بدء حوار Yarn عند التحدث مع شخصية | Todo | Critical | Programming | M | TASK-M02-008, TASK-M01-028, TASK-M03-002 | No |
| [TASK-M03-006](../tasks/M03/TASK-M03-006.md) | واجهة الحوار RTL (المتحدث والخيارات والترجمة النصية) | Todo | High | Programming | M | TASK-M03-005, TASK-M01-022 | No |
| [TASK-M03-007](../tasks/M03/TASK-M03-007.md) | جسر Yarn مع المحاكاة (قراءة الحقائق وتسجيل الأحداث) | Todo | Critical | Programming | M | TASK-M03-005, TASK-M01-009, TASK-M03-008 | No |
| [TASK-M03-008](../tasks/M03/TASK-M03-008.md) | مزود الحقائق facts لمحدد السطور (FR-D3) | Todo | High | Programming | M | TASK-M01-029, TASK-M01-006, TASK-M03-001 | No |
| [TASK-M03-009](../tasks/M03/TASK-M03-009.md) | الجمل العابرة barks بالقرب من الشخصيات | Todo | Medium | Programming | M | TASK-M03-008, TASK-M03-002, TASK-M01-030 | No |
| [TASK-M03-010](../tasks/M03/TASK-M03-010.md) | حفظ السطور المقولة ومهلاتها في اللقطة | Todo | High | Programming | S | TASK-M01-029, TASK-M01-013 | No |
| [TASK-M03-011](../tasks/M03/TASK-M03-011.md) | إعداد 3 شخصيات للنموذج (المنافس وكبير السوق والزبونة) | Todo | High | Design | S | TASK-M03-001, TASK-M03-003, TASK-M03-005 | No |

## [M04](../milestones/M04.md) — 0/16 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M04-001](../tasks/M04/TASK-M04-001.md) | تعريف البضائع السبع (الجودة والسعر) | Todo | Critical | Design | S | TASK-M01-025 | No |
| [TASK-M04-002](../tasks/M04/TASK-M04-002.md) | المخزون والمال Inventory | Todo | Critical | Programming | M | TASK-M04-001, TASK-M01-013 | No |
| [TASK-M04-003](../tasks/M04/TASK-M04-003.md) | اقتصاد الأسر (الرصيد والمخزون والحاجات) | Todo | High | Programming | M | TASK-M04-001, TASK-M03-001 | No |
| [TASK-M04-004](../tasks/M04/TASK-M04-004.md) | الطلب اليومي وتقلب الأسعار ببذرة ثابتة | Todo | Medium | Programming | S | TASK-M04-001, TASK-M01-007, TASK-M01-006 | No |
| [TASK-M04-005](../tasks/M04/TASK-M04-005.md) | الشراء من المورد | Todo | High | Programming | M | TASK-M04-002, TASK-M02-008 | No |
| [TASK-M04-006](../tasks/M04/TASK-M04-006.md) | تفاعل الميزان (وضع الصنجات والبضاعة وقراءة الكفتين) | Todo | Critical | Programming | L | TASK-M02-008, TASK-M04-001 | No |
| [TASK-M04-007](../tasks/M04/TASK-M04-007.md) | الصنجات السليمة والمغشوشة | Todo | High | Programming | S | TASK-M04-006 | No |
| [TASK-M04-008](../tasks/M04/TASK-M04-008.md) | وصول الزبائن حسب الوقت ومدخل السمعة | Todo | High | Programming | M | TASK-M03-003, TASK-M04-002, TASK-M03-004 | No |
| [TASK-M04-009](../tasks/M04/TASK-M04-009.md) | صفقة البيع الأمينة عبر خط المعالجة TRADE_HONEST | Todo | Critical | Programming | M | TASK-M04-006, TASK-M04-002, TASK-M04-003, TASK-M01-010 | No |
| [TASK-M04-010](../tasks/M04/TASK-M04-010.md) | الغش بالكيل والصنجات CHEAT_SCALE | Todo | Critical | Programming | M | TASK-M04-009, TASK-M04-007 | Yes |
| [TASK-M04-011](../tasks/M04/TASK-M04-011.md) | الغش بخلط الرديء بالجيد CHEAT_MIXING | Todo | High | Programming | S | TASK-M04-009 | Yes |
| [TASK-M04-012](../tasks/M04/TASK-M04-012.md) | الوصف الكاذب مع اكتشاف مؤجل FALSE_DESCRIPTION | Todo | High | Programming | M | TASK-M04-009, TASK-M01-011 | Yes |
| [TASK-M04-013](../tasks/M04/TASK-M04-013.md) | اكتشاف الضحية عند الوزن في البيت (حدث مؤجل) | Todo | High | Programming | M | TASK-M04-010, TASK-M01-011, TASK-M04-012 | No |
| [TASK-M04-014](../tasks/M04/TASK-M04-014.md) | واجهة التسعير والبيع RTL | Todo | High | Programming | M | TASK-M04-009, TASK-M01-022 | No |
| [TASK-M04-015](../tasks/M04/TASK-M04-015.md) | اختبار محاكاة الموازنة FR-T5 بلا واجهة | Todo | High | Programming | M | TASK-M04-010, TASK-M04-008, TASK-M04-004 | No |
| [TASK-M04-016](../tasks/M04/TASK-M04-016.md) | مراجعة S10: طرق الغش لا تعلّم أساليب واقعية | Todo | High | Religious Review | S | TASK-M04-010, TASK-M04-011, TASK-M04-012, TASK-M00-004 | Yes |

## [M05](../milestones/M05.md) — 0/17 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M05-001](../tasks/M05/TASK-M05-001.md) | حساب الشهود (المدى والرؤية والانتباه والزحام وobservant) | Todo | Critical | Programming | M | TASK-M01-009, TASK-M03-004 | No |
| [TASK-M05-002](../tasks/M05/TASK-M05-002.md) | نموذج Belief وذاكرة مستقلة لكل شخصية | Todo | Critical | Programming | M | TASK-M01-008, TASK-M03-001 | No |
| [TASK-M05-003](../tasks/M05/TASK-M05-003.md) | معالج الذاكرة: معتقدات للشهود والضحايا | Todo | Critical | Programming | M | TASK-M05-001, TASK-M05-002, TASK-M01-010 | No |
| [TASK-M05-004](../tasks/M05/TASK-M05-004.md) | شبكة العلاقات الاجتماعية بين الشخصيات | Todo | High | Design | S | TASK-M03-001 | No |
| [TASK-M05-005](../tasks/M05/TASK-M05-005.md) | دورة الشائعات (FR-E6 وFR-M3) | Todo | Critical | Programming | L | TASK-M05-003, TASK-M05-004, TASK-M01-007, TASK-M01-006 | No |
| [TASK-M05-006](../tasks/M05/TASK-M05-006.md) | تقييم السامع للخبر (skeptic والثقة) | Todo | High | Programming | S | TASK-M05-005, TASK-M05-008 | No |
| [TASK-M05-007](../tasks/M05/TASK-M05-007.md) | تلاشي الذكريات وسمة grudge (FR-M5) | Todo | Medium | Programming | S | TASK-M05-003 | No |
| [TASK-M05-008](../tasks/M05/TASK-M05-008.md) | الثقة والمودة لكل شخصية ومعالج العلاقات | Todo | Critical | Programming | M | TASK-M05-003 | No |
| [TASK-M05-009](../tasks/M05/TASK-M05-009.md) | اشتقاق السمعة من المعتقدات (FR-R2) | Todo | Critical | Programming | M | TASK-M05-008 | No |
| [TASK-M05-010](../tasks/M05/TASK-M05-010.md) | آثار السمعة على الزبائن والأسعار والموردين | Todo | High | Programming | M | TASK-M05-009, TASK-M04-008, TASK-M04-005 | No |
| [TASK-M05-011](../tasks/M05/TASK-M05-011.md) | بطء استعادة الثقة وعدم المسامحة (FR-R4) | Todo | Medium | Programming | S | TASK-M05-008 | No |
| [TASK-M05-012](../tasks/M05/TASK-M05-012.md) | دفاع من أحسن إليهم اللاعب عنه (FR-M6) | Todo | Medium | Programming | S | TASK-M05-005, TASK-M05-008, TASK-M05-006 | No |
| [TASK-M05-013](../tasks/M05/TASK-M05-013.md) | مصادر المعتقد الخاطئ MISTAKE (ميزان معيب وتلف وخلط الفاعل) | Todo | High | Programming | L | TASK-M05-003, TASK-M04-013 | No |
| [TASK-M05-014](../tasks/M05/TASK-M05-014.md) | البهتان المتعمد من المنافس SLANDER | Todo | High | Programming | M | TASK-M05-005 | No |
| [TASK-M05-015](../tasks/M05/TASK-M05-015.md) | تصحيح المعتقد والتبرئة (FR-M7 وCLEARED) | Todo | High | Programming | L | TASK-M05-013, TASK-M05-005, TASK-M04-006, TASK-M03-007, TASK-M05-016 | No |
| [TASK-M05-016](../tasks/M05/TASK-M05-016.md) | حدث الاتهام ACCUSED وحوار المواجهة | Todo | High | Programming | M | TASK-M05-003, TASK-M03-007 | No |
| [TASK-M05-017](../tasks/M05/TASK-M05-017.md) | حفظ الذاكرة والعلاقات والشائعات واختبارا T2 وT5 | Todo | Critical | QA | M | TASK-M05-005, TASK-M05-008, TASK-M04-010, TASK-M01-015 | No |

## [M06](../milestones/M06.md) — 0/9 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M06-001](../tasks/M06/TASK-M06-001.md) | حلقة يوم النموذج (شراء ثم بيع ثم مساء ثم نوم وحفظ تلقائي) | Todo | Critical | Programming | M | TASK-M04-009, TASK-M04-005, TASK-M05-010, TASK-M02-012, TASK-M04-010 | No |
| [TASK-M06-002](../tasks/M06/TASK-M06-002.md) | كتابة 30 سطراً مؤقتاً للضمير والإغراء بلا نصوص دينية | Todo | High | Writing | S | TASK-M01-025 | No |
| [TASK-M06-003](../tasks/M06/TASK-M06-003.md) | محفزات الصوتين الداخليين في النموذج | Todo | High | Programming | M | TASK-M06-002, TASK-M03-008, TASK-M01-030, TASK-M04-007 | No |
| [TASK-M06-004](../tasks/M06/TASK-M06-004.md) | سيناريو اتهام باطل واحد | Todo | High | Design | S | TASK-M05-013, TASK-M05-016, TASK-M05-015 | No |
| [TASK-M06-005](../tasks/M06/TASK-M06-005.md) | اختبارات الحفظ T3 وT4 وT6 في CI | Todo | Critical | QA | M | TASK-M05-017, TASK-M03-010, TASK-M04-013 | No |
| [TASK-M06-006](../tasks/M06/TASK-M06-006.md) | لوحة تطوير لعرض السجل والمعتقدات والشائعات | Todo | Medium | Programming | M | TASK-M05-005 | No |
| [TASK-M06-007](../tasks/M06/TASK-M06-007.md) | بروتوكول اختبار اللعب مع الأطفال واستبيانه وموافقة الأهل | Ready | High | QA | S | — | No |
| [TASK-M06-008](../tasks/M06/TASK-M06-008.md) | اختبار النموذج مع 5 أطفال أو أكثر وتقريره | Todo | Critical | QA | M | TASK-M06-001, TASK-M06-003, TASK-M06-004, TASK-M06-007, TASK-M06-005, TASK-M06-006 | No |
| [TASK-M06-009](../tasks/M06/TASK-M06-009.md) | مراجعة الاستمرار وتعديل الخطة بعد النموذج | Todo | Critical | Design | S | TASK-M06-008, TASK-M06-005 | No |

## [M07](../milestones/M07.md) — 0/19 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M07-001](../tasks/M07/TASK-M07-001.md) | معالج السجل الأخلاقي المخفي (FR-L1 إلى FR-L4) | Todo | Critical | Programming | M | TASK-M01-010, TASK-M06-009 | No |
| [TASK-M07-002](../tasks/M07/TASK-M07-002.md) | سلسلة العواقب السببية مع causeEventIds (FR-K1) | Todo | High | Programming | M | TASK-M05-010, TASK-M01-011, TASK-M06-009 | No |
| [TASK-M07-003](../tasks/M07/TASK-M07-003.md) | أحداث الحياة بمعدل واحد للجميع (FR-K2 وFR-K3 وSR-09) | Todo | High | Programming | M | TASK-M01-011, TASK-M01-007, TASK-M04-002, TASK-M06-009 | Yes |
| [TASK-M07-004](../tasks/M07/TASK-M07-004.md) | نظام الصوتين الداخليين ومحفزاته وتطور النبرة (SR-01 معطل) | Todo | Critical | Programming | L | TASK-M06-003, TASK-M07-001 | Yes |
| [TASK-M07-005](../tasks/M07/TASK-M07-005.md) | متغيرات الضمير المرتبطة بأحداث فعلية (FR-C2) | Todo | High | Programming | S | TASK-M07-004 | No |
| [TASK-M07-006](../tasks/M07/TASK-M07-006.md) | عرض الصوتين (مؤثر بصري وترجمة ومدخل صوتي) | Todo | High | Programming | M | TASK-M07-004, TASK-M03-006 | No |
| [TASK-M07-007](../tasks/M07/TASK-M07-007.md) | آلة حالة التوبة (REPENT_REMORSE وREPENT_QUIT وRELAPSE) | Todo | Critical | Programming | M | TASK-M07-001 | Yes |
| [TASK-M07-008](../tasks/M07/TASK-M07-008.md) | دفتر الحقوق: المستحق لكل ضحية (FR-W3) | Todo | Critical | Programming | M | TASK-M07-007, TASK-M04-010 | No |
| [TASK-M07-009](../tasks/M07/TASK-M07-009.md) | رد الحق المباشر بما فيه الضحية التي لم تعلم (FR-W4) | Todo | Critical | Programming | M | TASK-M07-008, TASK-M03-007 | Yes |
| [TASK-M07-010](../tasks/M07/TASK-M07-010.md) | التصدق عن الضحية المتعذر الوصول إليها ومغادرة تاجر القافلة | Todo | High | Programming | M | TASK-M07-008, TASK-M03-003 | Yes |
| [TASK-M07-011](../tasks/M07/TASK-M07-011.md) | خيارات الندم والإقلاع في التأمل ولقاء الضحية (FR-W1 وFR-W2) | Todo | High | Programming | M | TASK-M07-007, TASK-M07-004 | Yes |
| [TASK-M07-012](../tasks/M07/TASK-M07-012.md) | الصفقات الأمينة بعد الإقلاع ترفع الثقة تدريجياً (FR-W5) | Todo | Medium | Programming | S | TASK-M07-007, TASK-M05-008 | No |
| [TASK-M07-013](../tasks/M07/TASK-M07-013.md) | اشتقاق حالة محور الحقيقة (الحالات الأربع) | Todo | Critical | Programming | S | TASK-M07-007, TASK-M07-008 | No |
| [TASK-M07-014](../tasks/M07/TASK-M07-014.md) | مدقق الاتساق في نسخ التطوير (FR-S7) | Todo | High | Programming | M | TASK-M07-001, TASK-M07-013, TASK-M01-013 | No |
| [TASK-M07-015](../tasks/M07/TASK-M07-015.md) | اختبار الحفظ T9 (رد حق جزئي) | Todo | Critical | QA | S | TASK-M07-009, TASK-M01-015, TASK-M07-010 | No |
| [TASK-M07-016](../tasks/M07/TASK-M07-016.md) | أحداث المساعدة والصدقة السرية وأثرها على الحاجات | Todo | Medium | Programming | S | TASK-M07-001, TASK-M04-003 | No |
| [TASK-M07-017](../tasks/M07/TASK-M07-017.md) | كتابة مجموعة سطور الضمير والإغراء v1 | Todo | High | Writing | L | TASK-M07-004, TASK-M00-006 | Yes |
| [TASK-M07-018](../tasks/M07/TASK-M07-018.md) | مسودات نصوص رد الحقوق والتصدق عن الضحية (SR-02 وSR-03) | Todo | High | Writing | M | TASK-M07-009, TASK-M07-010 | Yes |
| [TASK-M07-019](../tasks/M07/TASK-M07-019.md) | دفعة مراجعة شرعية: الصوتان الداخليان ونمذجة التوبة | Todo | Critical | Religious Review | M | TASK-M07-017, TASK-M07-018, TASK-M07-011, TASK-M00-004, TASK-M07-003 | Yes |

## [M08](../milestones/M08.md) — 0/11 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M08-001](../tasks/M08/TASK-M08-001.md) | أسلوب العرض المميز لطبقة القصة | Todo | High | Design | M | TASK-M02-005 | Yes |
| [TASK-M08-002](../tasks/M08/TASK-M08-002.md) | نقاط السرد في العالم ومشغل مقاطع القصة بالترتيب الثابت (FR-N1) | Todo | Critical | Programming | M | TASK-M01-025, TASK-M02-008 | No |
| [TASK-M08-003](../tasks/M08/TASK-M08-003.md) | بيانات مقطع الفصل الأول بالإحالات القرآنية | Todo | Critical | Writing | S | TASK-M01-027, TASK-M00-006 | Yes |
| [TASK-M08-004](../tasks/M08/TASK-M08-004.md) | نص سرد الفصل الأول من القرآن والتفاسير المعتبرة مع وسم غير الثابت | Todo | Critical | Writing | L | TASK-M08-003 | Yes |
| [TASK-M08-005](../tasks/M08/TASK-M08-005.md) | تحقق مصادر الفصل الأول sourceCheck | Todo | Critical | Religious Review | M | TASK-M08-004 | Yes |
| [TASK-M08-006](../tasks/M08/TASK-M08-006.md) | المراجعة الشرعية واعتماد مقطع الفصل الأول | Todo | Critical | Religious Review | M | TASK-M08-005, TASK-M00-004 | Yes |
| [TASK-M08-007](../tasks/M08/TASK-M08-007.md) | مكوّن عرض الآيات بالرسم العثماني من النص المستخرج فقط | Todo | Critical | Programming | M | TASK-M01-022, TASK-M01-027 | Yes |
| [TASK-M08-008](../tasks/M08/TASK-M08-008.md) | تصدير المحتوى للمراجع واستيراد ملاحظاته (FR-Q4) | Todo | High | Programming | M | TASK-M01-026 | No |
| [TASK-M08-009](../tasks/M08/TASK-M08-009.md) | وسم الروايات غير الثابتة في العرض (S4) | Todo | High | Programming | S | TASK-M08-007, TASK-M08-002 | Yes |
| [TASK-M08-010](../tasks/M08/TASK-M08-010.md) | بطاقة الانتقال ومؤشر الطبقة (F5) | Todo | High | Programming | S | TASK-M08-002 | Yes |
| [TASK-M08-011](../tasks/M08/TASK-M08-011.md) | تسجيل عينة الراوي العربي لمقطع الفصل الأول | Todo | High | Audio | M | TASK-M08-006 | Yes |

## [M09](../milestones/M09.md) — 0/9 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M09-001](../tasks/M09/TASK-M09-001.md) | محدد النهاية من مصفوفة المحورين (8 نهايات) وعتبة السمعة | Todo | Critical | Programming | S | TASK-M07-013, TASK-M05-009 | Yes |
| [TASK-M09-002](../tasks/M09/TASK-M09-002.md) | تسلسل النهاية F5 (النهاية الشخصية ثم الانتقال ثم خاتمة القوم ثم المراجعة ثم اللعب الحر) | Todo | Critical | Programming | M | TASK-M09-001, TASK-M08-010 | No |
| [TASK-M09-003](../tasks/M09/TASK-M09-003.md) | محتوى نهايتين للشريحة العمودية | Todo | High | Writing | M | TASK-M09-002 | Yes |
| [TASK-M09-004](../tasks/M09/TASK-M09-004.md) | نموذج بطاقة المراجعة مع evidenceEventIds | Todo | Critical | Programming | M | TASK-M01-008, TASK-M05-005 | No |
| [TASK-M09-005](../tasks/M09/TASK-M09-005.md) | قوالب بطاقات المراجعة (الغش الخفي والصدقة السرية والاتهام الباطل وسلاسل الشائعات والعواقب) | Todo | High | Programming | M | TASK-M09-004, TASK-M07-002, TASK-M07-008, TASK-M07-016 | No |
| [TASK-M09-006](../tasks/M09/TASK-M09-006.md) | اختبار FR-J8 الآلي للأدلة والأرقام | Todo | Critical | QA | S | TASK-M09-005 | No |
| [TASK-M09-007](../tasks/M09/TASK-M09-007.md) | واجهة مراجعة الرحلة | Todo | High | Programming | M | TASK-M09-005, TASK-M10-001 | No |
| [TASK-M09-008](../tasks/M09/TASK-M09-008.md) | مراجعة شرعية لنصوص المراجعة والدروس (FR-J7) | Todo | High | Religious Review | S | TASK-M09-005, TASK-M09-003 | Yes |
| [TASK-M09-009](../tasks/M09/TASK-M09-009.md) | العودة للعب الحر بعد النهاية | Todo | Medium | Programming | S | TASK-M09-002 | No |

## [M10](../milestones/M10.md) — 0/14 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M10-001](../tasks/M10/TASK-M10-001.md) | دليل أسلوب الواجهة ونظام التخطيط من اليمين لليسار | Todo | High | Design | M | TASK-M01-022 | No |
| [TASK-M10-002](../tasks/M10/TASK-M10-002.md) | القائمة الرئيسية وخانات الحفظ الثلاث | Todo | High | Programming | M | TASK-M10-001, TASK-M01-013 | No |
| [TASK-M10-003](../tasks/M10/TASK-M10-003.md) | واجهة HUD مختصرة بلا عدادات أخلاقية (S9) | Todo | Medium | Programming | S | TASK-M10-001 | No |
| [TASK-M10-004](../tasks/M10/TASK-M10-004.md) | الإعدادات (الصوت والترجمة وإعادة التعيين وعمى الألوان والجودة) | Todo | High | Programming | M | TASK-M10-001, TASK-M02-001, TASK-M10-011 | No |
| [TASK-M10-005](../tasks/M10/TASK-M10-005.md) | إنشاء الشخصية (ذكر وأنثى ولباس محتشم والأنثى مقيدة بـ SR-08) | Todo | Medium | Programming | M | TASK-M10-001, TASK-M10-008 | Yes |
| [TASK-M10-006](../tasks/M10/TASK-M10-006.md) | وثيقة الاتجاه الفني ولوحة المراجع (تصور فني) | Todo | High | Art | M | TASK-M00-005 | Yes |
| [TASK-M10-007](../tasks/M10/TASK-M10-007.md) | أصول منطقة السوق النهائية (دكاكين ومبانٍ وأدوات) | Todo | Critical | Art | XL | TASK-M10-006, TASK-M02-005 | No |
| [TASK-M10-008](../tasks/M10/TASK-M10-008.md) | نماذج الشخصيات وملابس محتشمة | Todo | High | Art | XL | TASK-M10-006 | Yes |
| [TASK-M10-009](../tasks/M10/TASK-M10-009.md) | الإضاءة والمعالجة اللاحقة للسوق (URP) | Todo | High | Art | M | TASK-M10-007 | No |
| [TASK-M10-010](../tasks/M10/TASK-M10-010.md) | البيئة الصوتية للسوق بلا معازف (S11) | Todo | High | Audio | M | TASK-M02-005 | Yes |
| [TASK-M10-011](../tasks/M10/TASK-M10-011.md) | مجموعات المكسر والمؤثرات الصوتية (الميزان والنقود والخطوات) | Todo | Medium | Audio | M | TASK-M04-006 | No |
| [TASK-M10-012](../tasks/M10/TASK-M10-012.md) | عينة تسجيل الصوتين الداخليين | Todo | High | Audio | M | TASK-M07-019 | Yes |
| [TASK-M10-013](../tasks/M10/TASK-M10-013.md) | قائمة الإيقاف ومؤشر الحفظ التلقائي | Todo | Medium | Programming | S | TASK-M10-002 | No |
| [TASK-M10-014](../tasks/M10/TASK-M10-014.md) | مراجعة إمكانية الوصول (حجم النص والترجمة الدائمة والتباين) | Todo | Medium | QA | S | TASK-M10-004, TASK-M07-006 | No |

## [M11](../milestones/M11.md) — 0/9 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M11-001](../tasks/M11/TASK-M11-001.md) | سيناريو الشريحة العمودية (10 إلى 15 دقيقة) | Todo | Critical | Design | M | TASK-M07-011, TASK-M05-015 | Yes |
| [TASK-M11-002](../tasks/M11/TASK-M11-002.md) | دمج محتوى الشريحة (يوم كامل ومسار توبة ومقطع قصة ونهايتان ومراجعة) | Todo | Critical | Programming | L | TASK-M11-001, TASK-M08-006, TASK-M08-007, TASK-M09-003, TASK-M09-007, TASK-M10-009 | No |
| [TASK-M11-003](../tasks/M11/TASK-M11-003.md) | قياس الأداء على Mac M1 (60 إطاراً) | Todo | Critical | QA | M | TASK-M11-002 | No |
| [TASK-M11-004](../tasks/M11/TASK-M11-004.md) | إعادة قياس الأداء على الويب والجوال (P2) | Todo | High | QA | M | TASK-M11-002, TASK-M01-023 | No |
| [TASK-M11-005](../tasks/M11/TASK-M11-005.md) | تدقيق المحتوى الديني في بناء الشريحة | Todo | Critical | Religious Review | S | TASK-M11-002, TASK-M01-026, TASK-M07-019, TASK-M09-008 | Yes |
| [TASK-M11-006](../tasks/M11/TASK-M11-006.md) | اختبار لعب الشريحة مع أطفال وأولياء أمور وتقريره | Todo | Critical | QA | M | TASK-M11-002, TASK-M06-007, TASK-M11-005 | No |
| [TASK-M11-007](../tasks/M11/TASK-M11-007.md) | تقدير كلفة إنتاج MVP | Todo | High | Design | M | TASK-M11-006 | No |
| [TASK-M11-008](../tasks/M11/TASK-M11-008.md) | بناء الشريحة الداخلي وقائمة فحصه | Todo | High | DevOps | S | TASK-M11-003, TASK-M11-005 | No |
| [TASK-M11-009](../tasks/M11/TASK-M11-009.md) | قرار الاستمرار وتثبيت نطاق MVP | Todo | Critical | Design | S | TASK-M11-004, TASK-M11-006, TASK-M11-007, TASK-M11-008, TASK-M09-006 | No |

## [M12](../milestones/M12.md) — 0/19 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M12-001](../tasks/M12/TASK-M12-001.md) | مخطط البلدة الكامل (الأحياء وطريق القوافل والبئر والمراعي ونقاط السرد) | Todo | Critical | Design | L | TASK-M11-009 | No |
| [TASK-M12-002](../tasks/M12/TASK-M12-002.md) | أصول البلدة النهائية خارج السوق | Todo | High | Art | XL | TASK-M12-001, TASK-M10-007 | No |
| [TASK-M12-003](../tasks/M12/TASK-M12-003.md) | إعداد الأدوار الإحدى عشرة بسماتها وجداولها وأسرها | Todo | Critical | Design | L | TASK-M12-001, TASK-M03-011 | No |
| [TASK-M12-004](../tasks/M12/TASK-M12-004.md) | تاجر القافلة: الصفقة المغرية لمرة واحدة والمغادرة | Todo | High | Design | M | TASK-M12-003, TASK-M07-010 | No |
| [TASK-M12-005](../tasks/M12/TASK-M12-005.md) | سيناريوهات الرحمة مع الأرملة وأطفالها | Todo | High | Writing | M | TASK-M12-003, TASK-M07-016 | No |
| [TASK-M12-006](../tasks/M12/TASK-M12-006.md) | علاقة الصبي الحمّال اليتيم المتطورة | Todo | Medium | Writing | M | TASK-M12-003 | No |
| [TASK-M12-007](../tasks/M12/TASK-M12-007.md) | اللص والعشّاب في أحداث الحياة (السرقة والمرض والنفقات) | Todo | Medium | Design | M | TASK-M12-003, TASK-M07-003 | Yes |
| [TASK-M12-008](../tasks/M12/TASK-M12-008.md) | أسرة اللاعب وحاجاتها كدافع (5.3) | Todo | High | Design | M | TASK-M12-003, TASK-M04-003 | No |
| [TASK-M12-009](../tasks/M12/TASK-M12-009.md) | هيكل الفصول 1 إلى 3 ومعالج حالة القصة والقصة الرئيسية | Todo | Critical | Programming | L | TASK-M11-009, TASK-M08-002 | No |
| [TASK-M12-010](../tasks/M12/TASK-M12-010.md) | مقطع الفصل الثاني (هود 87–92): كتابة وتحقق واعتماد | Todo | Critical | Writing | L | TASK-M08-006, TASK-M08-008 | Yes |
| [TASK-M12-011](../tasks/M12/TASK-M12-011.md) | مقطع الفصل الثالث (الأعراف 88–90): كتابة وتحقق واعتماد | Todo | Critical | Writing | L | TASK-M08-006, TASK-M08-008 | Yes |
| [TASK-M12-012](../tasks/M12/TASK-M12-012.md) | مقطع الخاتمة (الأعراف 91–93 وهود 94–95 والشعراء 189) بالعرض الافتراضي SR-04 | Todo | Critical | Writing | L | TASK-M08-006, TASK-M08-008 | Yes |
| [TASK-M12-013](../tasks/M12/TASK-M12-013.md) | محتوى النهايات الست المتبقية | Todo | High | Writing | M | TASK-M09-003 | Yes |
| [TASK-M12-014](../tasks/M12/TASK-M12-014.md) | حوارات Yarn الكاملة لكل الشخصيات (لا كلام في الدين SR-10) | Todo | Critical | Writing | XL | TASK-M12-003 | Yes |
| [TASK-M12-015](../tasks/M12/TASK-M12-015.md) | مجموعات barks والصوتين الداخليين الكاملة | Todo | High | Writing | XL | TASK-M07-019, TASK-M12-003 | Yes |
| [TASK-M12-016](../tasks/M12/TASK-M12-016.md) | التعليم المدمج للميزان والبيع | Todo | High | Design | M | TASK-M12-009 | No |
| [TASK-M12-017](../tasks/M12/TASK-M12-017.md) | التسجيل العربي الكامل (الراوي والصوتان والسطور الرئيسية) | Todo | High | Audio | XL | TASK-M12-010, TASK-M12-011, TASK-M12-012, TASK-M12-015, TASK-M12-014 | Yes |
| [TASK-M12-018](../tasks/M12/TASK-M12-018.md) | موازنة الاقتصاد والسمعة عبر الحلقة الكاملة | Todo | High | Design | L | TASK-M12-009, TASK-M12-003, TASK-M12-004, TASK-M12-008, TASK-M12-019 | No |
| [TASK-M12-019](../tasks/M12/TASK-M12-019.md) | سلوك التاجر المنافس المتقدم (الغش والإغراء والبهتان) | Todo | Medium | Programming | M | TASK-M12-003, TASK-M05-014 | No |

## [M13](../milestones/M13.md) — 0/10 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M13-001](../tasks/M13/TASK-M13-001.md) | مجموعة اختبارات الحفظ T1 إلى T9 على محتوى MVP واختبار تحمل | Todo | Critical | QA | M | TASK-M12-009, TASK-M07-015, TASK-M06-005 | No |
| [TASK-M13-002](../tasks/M13/TASK-M13-002.md) | تحسين الأداء (60 إطاراً على M1 والذاكرة) | Todo | Critical | Programming | L | TASK-M12-002, TASK-M12-003 | No |
| [TASK-M13-003](../tasks/M13/TASK-M13-003.md) | اختبار انحدار شامل وجلسة صيد أخطاء | Todo | Critical | QA | L | TASK-M12-009, TASK-M12-014, TASK-M12-016, TASK-M12-002, TASK-M12-013, TASK-M12-017, TASK-M12-018 | No |
| [TASK-M13-004](../tasks/M13/TASK-M13-004.md) | المراجعة الشرعية النهائية لكل المحتوى | Todo | Critical | Religious Review | XL | TASK-M12-010, TASK-M12-011, TASK-M12-012, TASK-M12-013, TASK-M12-014, TASK-M12-015, TASK-M12-017, TASK-M12-007 | Yes |
| [TASK-M13-005](../tasks/M13/TASK-M13-005.md) | تدقيق سجل المسائل المعلقة: لا ميزة مفعّلة دون حسم | Todo | Critical | Religious Review | S | TASK-M13-004 | Yes |
| [TASK-M13-006](../tasks/M13/TASK-M13-006.md) | اختبار لعب MVP وقياس معايير القسم 12 | Todo | Critical | QA | L | TASK-M13-003, TASK-M13-004 | No |
| [TASK-M13-007](../tasks/M13/TASK-M13-007.md) | إصلاحات ما بعد اختبار اللعب | Todo | High | Programming | L | TASK-M13-006 | No |
| [TASK-M13-008](../tasks/M13/TASK-M13-008.md) | بناء إصدار macOS (التوقيع والتوثيق والتوزيع المجاني) | Todo | Critical | DevOps | M | TASK-M13-007, TASK-M13-005, TASK-M13-002, TASK-M13-001, TASK-M13-009 | No |
| [TASK-M13-009](../tasks/M13/TASK-M13-009.md) | صفحة التعريف وبيان الخصوصية (لا جمع بيانات) | Todo | Medium | Writing | S | TASK-M11-009 | Yes |
| [TASK-M13-010](../tasks/M13/TASK-M13-010.md) | الإطلاق وفرز الأعطال بعده | Todo | High | DevOps | S | TASK-M13-008, TASK-M13-009 | No |

## [M14](../milestones/M14.md) — 0/5 (0.0% بالعدد، 0.0% بالجهد)

| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |
|---|---|---|---|---|---|---|---|
| [TASK-M14-001](../tasks/M14/TASK-M14-001.md) | قرار المنصة التالية (الويب أو الجوال) من تقارير P0 وP2 | Todo | Medium | Design | S | TASK-M13-008, TASK-M11-004 | No |
| [TASK-M14-002](../tasks/M14/TASK-M14-002.md) | تصميم مخطط التحكم باللمس | Todo | Low | Design | M | TASK-M14-001 | No |
| [TASK-M14-003](../tasks/M14/TASK-M14-003.md) | التحقق من عرض العربية وحجم ICU على المنصة المختارة | Todo | Low | Programming | M | TASK-M14-001 | No |
| [TASK-M14-004](../tasks/M14/TASK-M14-004.md) | مذكرة تصميم الحفظ السحابي Convex بموافقة ولي الأمر | Todo | Low | Design | S | TASK-M13-008 | No |
| [TASK-M14-005](../tasks/M14/TASK-M14-005.md) | تدقيق جاهزية الترجمة الإنجليزية (لا نصوص ثابتة في الكود) | Todo | Low | QA | S | TASK-M13-008 | No |
