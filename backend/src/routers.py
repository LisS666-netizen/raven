from django.urls import path, include


urlpatterns = [
    path('', include('src.profiles.urls')),
    path('projects/', include('src.restapi.urls')),
]