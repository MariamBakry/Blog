from django.test import TestCase
from stories.models import Story
from users.models import CustomUser

class StoryModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(username='testuser', password='password123')

    def test_create_story(self):
        story = Story.objects.create(title='Test Story', body='Test Body', author=self.user)

        # Check if the author of the story is the test user
        self.assertEqual(story.author, self.user)
        self.assertEqual(story.title, 'Test Story',
                         msg='story title should be "Test Story"')
        self.assertEqual(story.body, 'Test Body',
                         msg='story bode should be "Test Body"')
