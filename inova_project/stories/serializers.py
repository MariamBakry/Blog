from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'body', 'author', 'created_at', 'avg_rating')


class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('title', 'body')