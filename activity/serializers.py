from rest_framework import serializers
from submission.serializers import SubmissionSerializer

class ActivitySerializer(serializers.ActivitySerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    points = serializers.FloatField()

    submissions = SubmissionSerializer(many=True)