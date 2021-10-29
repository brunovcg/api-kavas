from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=255)
    points = models.FloatField()

