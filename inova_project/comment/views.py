from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class CommentStoryView(APIView):
    def post(self, request, story_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(story_id=story_id, user_id = request.user.id)
            return Response({'message':'comment added'})
        else:
            return Response(serializer.errors, status=400)
