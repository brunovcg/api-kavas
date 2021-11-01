from rest_framework import serializers
from accounts.serializers import UserShortSerializer


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    users = UserShortSerializer(many=True)

    