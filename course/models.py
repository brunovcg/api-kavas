from django.db import models
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer 

class Course(models.Model):

    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='course')

    users = UserSerializer(many=True)
