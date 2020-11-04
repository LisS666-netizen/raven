from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class Gender(models.Model):
    """
        Gender model from user profile info
    """

    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class VController(models.Model):
    """
        Service version controll
    """

    VERSION_CONTROLLER_SERVICE = (
        ('github', 'github'),
        ('gitlab', 'gitlab'),
        ('dockerhub', 'dockerhub')
    )

    service = models.CharField(max_length=10, choices=VERSION_CONTROLLER_SERVICE, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.service}:{self.username}"


class Division(models.Model):
    """
        Division
    """

    name = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.name}:{self.country}:{self.city}"


class Position(models.Model):
    """
        Position
    """

    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ATSUser(AbstractUser):
    """
        Customize user model
    """
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    job_email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    birthday = models.DateField(max_length=50, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    github = models.ForeignKey(VController, on_delete=models.CASCADE, blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)