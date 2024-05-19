import random
from faker import Faker
from django.core.management.base import BaseCommand
from stories.models import Story
from users.models import CustomUser
from django.utils import timezone
from rating.models import Rating
from django.db import IntegrityError

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with 50k posts and more than 20k reviews'

    def handle(self, *args, **kwargs):
        users = CustomUser.objects.exclude(is_superuser=True)
        # Seed 50k posts
        for _ in range(50000):
            title = fake.sentence()
            body = fake.paragraph()
            author = random.choice(users)
            created_at = fake.date_time_this_year()

            Story.objects.create(
                title=title,
                body=body,
                author=author,
                created_at=created_at
            )
        self.stdout.write(self.style.SUCCESS('50k posts seeded successfully'))
        
        #seed more than 20k ratings
        stories = Story.objects.exclude()
            
        i=0
        while i < 20100:
            value = random.randint(1, 5)
            user = random.choice(users)
            story = random.choice(stories)
            created_at = timezone.now()

            try:
                Rating.objects.create(
                    value=value,
                    user=user,
                    story=story,
                    created_at=created_at
                )
                i+=1
            except IntegrityError as e:
                    pass
            story.update_avg_rating()
        self.stdout.write(self.style.SUCCESS('more than 20k ratings seeded successfully'))