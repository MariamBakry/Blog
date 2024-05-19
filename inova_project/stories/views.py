from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Story
from .serializers import StoryCreateSerializer, StorySerializer
from django.shortcuts import get_object_or_404
from users.models import CustomUser
from inova_project.pagination import StoriesRatingPagination

class StoryCreateView(APIView):
    def post(self, request, format=None):
        serializer = StoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoryRetrieveView(APIView):
    pagination_class = StoriesRatingPagination
    def get(self, request, format=None):
        stories = Story.objects.all()
        paginator = self.pagination_class()
        paginated_stories = paginator.paginate_queryset(stories, request)
        serializer = StorySerializer(paginated_stories, many=True)
        return paginator.get_paginated_response(serializer.data)
    
class UserStoriesView(APIView):
    pagination_class = StoriesRatingPagination
    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        stories = Story.objects.filter(author=user)
        paginator = self.pagination_class()
        paginated_stories = paginator.paginate_queryset(stories, request)
        serializer = StorySerializer(paginated_stories, many=True)
        return paginator.get_paginated_response(serializer.data)
