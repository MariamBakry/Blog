from django.urls import path
from . import views

urlpatterns = [
    path('<int:story_id>/', views.CommentStoryView.as_view(), name='add_comment'),
]
