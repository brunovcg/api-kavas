from django.db import models
from django.contrib.auth.models import User

class Submission(models.Model):
    grade = models.FloatField()
    repo = models.CharField(max_length=255)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    activity_id = models.ForeignKey('activity.Activity', on_delete=models.CASCADE)