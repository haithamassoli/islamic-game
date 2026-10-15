# فهرس وثائق الأنظمة (docs/systems)

وثيقة لكل نظام. المرجع الملزم: [PRD القسم 7 و8](../PRD.md)، والبنية العامة في [TECHNICAL_ARCHITECTURE.md](../TECHNICAL_ARCHITECTURE.md). هذه الوثائق تشرح **كيف** يُبنى كل نظام، ولا تضيف متطلبات. عند التعارض يفوز PRD ثم TECHNICAL_ARCHITECTURE.

## هيكل كل وثيقة (ثابت)
المسؤوليات، البيانات التي يمتلكها، الواجهة العامة (تخطيط تواقيع C#)، الأحداث التي يستقبلها ويصدرها، الاعتمادات، الملفات البرمجية المقترحة، الاختبار المنفرد، حفظ الحالة (FR-S1)، التوسع المستقبلي، المهام المرتبطة.

التواقيع **تخطيطية**: الاسم والدور ملزمان، والتفاصيل الدقيقة تُثبت في المهمة المنفذة.

## الأنظمة
| النظام | الوثيقة | الطبقة | موقعه في FR-E4 | المرحلة الأولى |
|---|---|---|---|---|
| سجل القرارات والنواة | [EVENT_PIPELINE.md](EVENT_PIPELINE.md) | Simulation/Core | يملك الخط | M01 |
| الإدراك والشهود | [PERCEPTION.md](PERCEPTION.md) | Simulation/Perception | الخطوة 2 | M05 |
| الذاكرة والشائعات | [MEMORY_AND_RUMORS.md](MEMORY_AND_RUMORS.md) | Simulation/Memory، Rumors | المعالج 5.1 + دورة زمنية | M05 |
| العلاقات والسمعة | [RELATIONSHIPS_AND_REPUTATION.md](RELATIONSHIPS_AND_REPUTATION.md) | Simulation/Social | المعالج 5.4 | M05 |
| الاقتصاد والتجارة | [ECONOMY_AND_TRADE.md](ECONOMY_AND_TRADE.md) | Simulation/Economy + Runtime/Trade | الخطوة 3 | M04 |
| السجل الأخلاقي | [MORAL_LEDGER.md](MORAL_LEDGER.md) | Simulation/Moral | المعالج 5.2 | M07 |
| العواقب وأحداث الحياة | [CONSEQUENCES_AND_LIFE_EVENTS.md](CONSEQUENCES_AND_LIFE_EVENTS.md) | Simulation/Consequences | المعالج 5.5 + لفة يومية | M07 |
| الصوتان الداخليان | [INNER_VOICE.md](INNER_VOICE.md) | Simulation/InnerVoice + Runtime/UI | عرض فقط (`OnRecorded`) | M06 |
| التوبة ورد الحقوق | [REPENTANCE.md](REPENTANCE.md) | Simulation/Repentance | المعالج 5.3 | M07 |
| الحوار | [DIALOGUE.md](DIALOGUE.md) | Simulation/Dialogue + Runtime | مصدر أحداث + عرض | M01 |
| التفاعل | [INTERACTION.md](INTERACTION.md) | Runtime/Interaction | مصدر أفعال فقط | M02 |
| وكلاء الشخصيات | [NPC_AGENTS.md](NPC_AGENTS.md) | Simulation/Core + Runtime/NPC | يزوّد الإدراك بالمواقع | M03 |
| السرد ومقاطع القصة | [NARRATIVE.md](NARRATIVE.md) | Simulation/Narrative + Runtime/Story | المعالج 5.6 | M08 |
| النهايات ومراجعة الرحلة | [ENDINGS_AND_JOURNEY_REVIEW.md](ENDINGS_AND_JOURNEY_REVIEW.md) | Simulation/Endings، Journey | دوال نقية عند النهاية | M09 |
| خط المحتوى والتحقق الشرعي | [CONTENT_PIPELINE.md](CONTENT_PIPELINE.md) | Editor + content/ | قبل البناء | M01 |

وثائق عابرة للأنظمة: [DATA_ARCHITECTURE.md](../DATA_ARCHITECTURE.md) (المخططات والمعرّفات)، [SAVE_SYSTEM.md](../SAVE_SYSTEM.md) (الحفظ وT1–T9)، [LOCALIZATION.md](../LOCALIZATION.md) (العربية والمفاتيح)، [PERFORMANCE_TARGETS.md](../PERFORMANCE_TARGETS.md) (الميزانيات).

## الترتيب الثابت لمعالجات المحاكاة (FR-E4 الخطوة 5)
| # | المعالج | `HandlerId` | الوثيقة |
|---|---|---|---|
| 5.1 | `MemoryHandler` | `memory` | [MEMORY_AND_RUMORS](MEMORY_AND_RUMORS.md) |
| 5.2 | `MoralLedgerHandler` | `moral` | [MORAL_LEDGER](MORAL_LEDGER.md) |
| 5.3 | `RepentanceHandler` | `repentance` | [REPENTANCE](REPENTANCE.md) |
| 5.4 | `RelationshipsHandler` | `relationships` | [RELATIONSHIPS_AND_REPUTATION](RELATIONSHIPS_AND_REPUTATION.md) |
| 5.5 | `SchedulingHandler` | `scheduling` | [CONSEQUENCES_AND_LIFE_EVENTS](CONSEQUENCES_AND_LIFE_EVENTS.md) |
| 5.6 | `StoryStateHandler` | `story` | [NARRATIVE](NARRATIVE.md) |

مشتركو `OnRecorded` (عرض فقط، بلا ترتيب مضمون ولا أثر على اللقطة): الصوتان الداخليان، barks، الواجهة، الصوت، لوحة التطوير.

## الثوابت الثلاثة (تُفحص في المراجعة)
1. **السمعة لا ترى الأفعال السرية أبداً**؛ ترى المعتقدات فقط (FR-R2).
2. **السجل الأخلاقي يرى كل شيء ولا يُعرض أبداً** كرقم أو شريط أو عداد (FR-L2، S9).
3. **الصوتان الداخليان عرض**؛ لا يحفظان إلا السطور المقولة ومهلاتها (FR-E4 الخطوة 6، FR-S1).

## قواعد مشتركة لكل نظام محاكاة
- C# عادي في `IslamicGame.Simulation` بلا `UnityEngine`، ويتلقى `GameClock` و`RngStreams` في المُنشئ.
- أعداد صحيحة للحالة (المال `long`، النسب بالألف `0..1000`)، وترتيب تكرار صريح (Ordinal)، و`InvariantCulture`.
- الحالة القابلة للحفظ صنف `*State` يُسلسل JSON قانونياً ([SAVE_SYSTEM.md](../SAVE_SYSTEM.md)).
- كل نص للاعب بمفتاح ترجمة ([LOCALIZATION.md](../LOCALIZATION.md)).
- اختبار EditMode ببذرة ثابتة عبر `SimulationWorld` أو بإنشاء النظام منفرداً مع `GameClock` و`RngStreams` مبرمجين.
