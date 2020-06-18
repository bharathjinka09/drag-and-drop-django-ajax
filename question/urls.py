from django.urls import include, path
from .views import PaperQuestionReorder

urlpatterns = [
    path('manage-paper/<int:pk>/', PaperQuestionReorder.as_view(), name='manage-paper'),
]
