from rest_framework import serializers

class SubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    grade = serializers.FloatField()
    repo = serializers.CharField()
    user_id = serializers.IntegerField()
    activity_id = serializers.IntegerField()