from django.core.management.base import BaseCommand
from accounts.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with sample users (10 instructors, 15 students)"

    def handle(self, *args, **kwargs):
        fake = Faker()

        created_users = []

        # Create 10 instructors
        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 99)}"
            email = f"{username}@lmsapp.com"
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password="Password123!",
                is_instructor=True,
                is_student=False,
                bio=fake.sentence(nb_words=12),
                linkedin_url=f"https://linkedin.com/in/{username}",
                twitter_url=f"https://twitter.com/{username}"
            )
            created_users.append(user)

        # Create 15 students
        for _ in range(15):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 99)}"
            email = f"{username}@lmsapp.com"
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password="Password123!",
                is_instructor=False,
                is_student=True,
                bio=fake.sentence(nb_words=12),
                linkedin_url=f"https://linkedin.com/in/{username}",
                twitter_url=f"https://twitter.com/{username}"
            )
            created_users.append(user)

        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(created_users)} users successfully!"))
