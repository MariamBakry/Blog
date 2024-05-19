from django.test import TestCase
from stories.models import Story
from users.models import CustomUser
from .models import Rating

class RatingModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user1 = CustomUser.objects.create_user(username='testuser1', password='password123')
        self.user2 = CustomUser.objects.create_user(username='testuser2', password='password123')
        self.story = Story.objects.create(title='Test Story', body='Test Body', author=self.user1)

    def test_create_rating(self):
        rating1 = Rating.objects.create(value=4, user=self.user1, story=self.story)
        rating2 = Rating.objects.create(value=3, user=self.user2, story=self.story)

        self.assertEqual(rating1.value, 4,
                         msg='the rating value should be 4')
        self.assertEqual(rating1.user, self.user1)
        self.assertEqual(rating1.story, self.story)

        self.assertEqual(rating2.value, 3,
                         msg='the rating value should be 3')
        self.assertEqual(rating2.user, self.user2)
        self.assertEqual(rating2.story, self.story)

        rating1.story.update_avg_rating()

        self.assertEqual(rating1.story.avg_rating, 3.5,
                         msg='rating avg of the story should update to be 3.5, there is error with rating1')
        self.assertEqual(rating2.story.avg_rating, 3.5,
                         msg='rating avg of the story should update to be 3.5, there is error with rating12')
