from django.urls import path, include
from .views import ProjectList

urlpatterns = [
    path('', ProjectList.as_view()),
]