from django.test import TestCase
from stories.models import Story
from users.models import CustomUser
from .models import Comment

class CommentModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(username='testuser', password='password123')
        self.story = Story.objects.create(title='Test Story', body='Test Body', author=self.user)

    def test_create_comment(self):
        comment = Comment.objects.create(content='hello world', user=self.user, story=self.story)

        self.assertEqual(comment.content, 'hello world',
                         msg='The comment content should be "Hello world"')
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.story, self.story)
