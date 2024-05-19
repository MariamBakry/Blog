from rest_framework.response import Response
from .models import Rating
from .serializers import RatingSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from stories.models import Story

class RatingStoryView(APIView):
    def post(self, request, story_id):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(story_id=story_id, user_id = request.user.id)
            story = get_object_or_404(Story, id=story_id)
            story.update_avg_rating()
            return Response({'message':'rate added'})
        else:
            return Response(serializer.errors, status=400)
