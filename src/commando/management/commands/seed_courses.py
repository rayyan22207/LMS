from django.core.management.base import BaseCommand
from courses.models import Category, Course, Module, Lesson
from accounts.models import User
from faker import Faker
import random
from django.utils.text import slugify
from decimal import Decimal

class Command(BaseCommand):
    help = "Seed the database with categories, courses, modules, and lessons"

    def handle(self, *args, **kwargs):
        fake = Faker()
        instructors = User.objects.filter(is_instructor=True)

        if not instructors.exists():
            self.stdout.write(self.style.ERROR("❌ No instructors found. Seed users first."))
            return

        # Create Categories
        categories = []
        for _ in range(7):
            title = fake.unique.word().capitalize()
            slug = slugify(title)
            category = Category.objects.create(title=title, slug=slug)
            categories.append(category)

        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(categories)} categories."))

        # Create Courses
        courses = []
        for _ in range(15):
            title = fake.sentence(nb_words=4).rstrip(".")
            slug = slugify(title + str(random.randint(10, 999)))
            course = Course.objects.create(
                title=title,
                slug=slug,
                description=fake.paragraph(nb_sentences=3),
                instructor=random.choice(instructors),
                category=random.choice(categories),
                price=Decimal(random.randint(10, 99)),
                is_published=True,  # make them visible in listings
                thumbnail="C:/Users/Rayyan/Downloads/default.jpg"  # replace with a real file in prod
            )
            courses.append(course)

        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(courses)} courses."))

        # Create Modules and Lessons
        total_modules, total_lessons = 0, 0
        for course in courses:
            for m in range(random.randint(2, 5)):
                module = Module.objects.create(
                    course=course,
                    title=fake.sentence(nb_words=3),
                    order=m + 1
                )
                total_modules += 1
                for l in range(random.randint(2, 4)):
                    Lesson.objects.create(
                        module=module,
                        title=fake.sentence(nb_words=4),
                        video_url=f"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        content=fake.paragraph(nb_sentences=2),
                        order=l + 1
                    )
                    total_lessons += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {total_modules} modules and {total_lessons} lessons."))
