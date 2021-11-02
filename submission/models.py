from django.db import models
from django.contrib.auth.models import User
from activity.models import Activity

class Submission(models.Model):
    grade = models.FloatField(null=True)
    repo = models.CharField(max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions") 
    activity = models.ForeignKey('activity.Activity', on_delete=models.CASCADE, related_name='submissions')