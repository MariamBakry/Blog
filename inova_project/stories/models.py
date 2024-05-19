from django.db import models
from django.conf import settings
from rating.models import Rating
from django.db.models import Avg
# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    avg_rating = models.FloatField(default=0)

    def update_avg_rating(self):
        avg_rating = Rating.objects.filter(story=self).aggregate(avg_rating=Avg('value'))['avg_rating']
        self.avg_rating = avg_rating or 0
        self.save() 

    def __str__(self):
        return self.title
