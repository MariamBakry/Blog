from django.urls import path
from . import views

urlpatterns = [
    path('stories/create/', views.StoryCreateView.as_view(), name='create_story'),
    path('stories/', views.StoryRetrieveView.as_view(), name='retrieve_stories'),
    path('stories/<int:user_id>/', views.UserStoriesView.as_view(), name='user_stories'),
]
