from rest_framework import serializers

class SubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    grade = serializers.FloatField()
    repo = serializers.CharField()
    user = serializers.IntegerField()
    activity = serializers.IntegerField()