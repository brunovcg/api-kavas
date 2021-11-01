from rest_framework import serializers
from submission.serializers import SubmissionSerializer

class ActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    points = serializers.FloatField()
    submissions = SubmissionSerializer(many=True)
