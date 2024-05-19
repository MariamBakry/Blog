from django.urls import path
from . import views

urlpatterns = [
    path('<int:story_id>/', views.RatingStoryView.as_view(), name='add_rating'),
]
