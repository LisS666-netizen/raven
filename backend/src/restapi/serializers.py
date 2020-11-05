from rest_framework import serializers
from .models import Project


# Create your views here.

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields= ('name', 'author', 'members')
        model = Project
