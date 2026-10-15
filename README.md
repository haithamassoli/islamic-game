# اللعبة الإسلامية ثلاثية الأبعاد (اسم العمل: IslamicGame)

لعبة مغامرات ثلاثية الأبعاد للمسلمين من 10 إلى 18 سنة والعائلات. يعيش اللاعب تاجراً في بلدة خيالية مستوحاة من بيئة مدين، ويتعلم الأمانة من قراراته وعواقبها لا من الدروس. قصة شعيب عليه السلام تُروى سرداً قرآنياً ثابتاً، دون تجسيد الأنبياء.

- **التقنية:** Unity 6 + URP + C#، والتطوير على macOS.
- **النسخة الأولى (MVP):** بالعربية فقط على macOS، مجانية، بلا إعلانات ولا جمع بيانات.
- **الحالة:** مرحلة التخطيط. لا يوجد كود بعد. التفاصيل في [PROJECT_STATUS.md](PROJECT_STATUS.md).

## ابدأ من هنا
| أريد أن أعرف… | اقرأ |
|---|---|
| ما الذي نبنيه ولماذا | [docs/VISION.md](docs/VISION.md)، ثم [docs/PRD.md](docs/PRD.md) (مصدر الحقيقة) |
| كيف تُلعب اللعبة | [docs/GDD.md](docs/GDD.md)، [docs/GAMEPLAY_LOOP.md](docs/GAMEPLAY_LOOP.md) |
| الأنظمة وكيف تتواصل | [docs/TECHNICAL_ARCHITECTURE.md](docs/TECHNICAL_ARCHITECTURE.md)، [docs/systems/](docs/systems/README.md) |
| الضوابط الشرعية | [docs/ISLAMIC_CONTENT_GUIDELINES.md](docs/ISLAMIC_CONTENT_GUIDELINES.md) |
| المرحلة الحالية والتقدم | [PROJECT_STATUS.md](PROJECT_STATUS.md) |
| المهمة التالية | [NEXT_STEPS.md](NEXT_STEPS.md) |
| كل المهام | [planning/TASK_INDEX.md](planning/TASK_INDEX.md)، [planning/TASKS.csv](planning/TASKS.csv) |
| المراحل وخارطة الطريق | [planning/MILESTONES.md](planning/MILESTONES.md)، [planning/ROADMAP.md](planning/ROADMAP.md) |
| ما يمكن تنفيذه بالتوازي | [planning/DEPENDENCIES.md](planning/DEPENDENCIES.md) |
| تعليمات وكلاء الذكاء الاصطناعي | [AGENTS.md](AGENTS.md) |

## بنية المستودع
```
docs/        الرؤية والمتطلبات والتصميم والبنية (docs/systems/ وثيقة لكل نظام)
planning/    خارطة الطريق والمراحل والمهام والمخاطر والقرارات والاختبار
milestones/  ملف لكل مرحلة M00–M14
tasks/       ملف لكل مهمة: tasks/Mxx/TASK-Mxx-NNN.md (مصدر الحقيقة لحالة المهمة)
content/     المصادر الدينية وسجل المسائل الشرعية المعلقة (للمراجع الشرعي)
tools/       plan.py: مزامنة الفهارس وفحص الاتساق
unity/       مشروع Unity (يُنشأ في TASK-M01-001)
```

## سير العمل
1. اختر مهمة حالتها `Ready` من [PROJECT_STATUS.md](PROJECT_STATUS.md) أو [NEXT_STEPS.md](NEXT_STEPS.md).
2. نفّذها حسب ملفها، واختبرها، وحقق معايير قبولها.
3. حدّث ملف المهمة، ثم شغّل:
   ```
   python3 tools/plan.py sync    # يحدّث TASKS.csv وTASK_INDEX.md وجداول المراحل والتقدم ويرقّي المهام الجاهزة
   python3 tools/plan.py check   # يفحص المعرفات والاعتمادات والدورات والروابط
   ```
4. أضف سطراً في [CHANGELOG.md](CHANGELOG.md).

القواعد الكاملة في [AGENTS.md](AGENTS.md) و[planning/DEFINITION_OF_DONE.md](planning/DEFINITION_OF_DONE.md).
