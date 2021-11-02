import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from kanvas.permissions import Facilitador_and_instrutor, Estudante
from activity.serializers import ActivitySerializer
from activity.models import Activity
from django.core.exceptions import ObjectDoesNotExist
from submission.models import Submission
from submission.serializers import SubmissionSerializer
from django.contrib.auth.models import User


class ActivitiesView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Facilitador_and_instrutor]

    def post(self, request):

        data = request.data

        unique_title = Activity.objects.filter(title=data['title'])
        if len(unique_title) > 0:
            return Response({'error': 'Activity with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

        activity = Activity.objects.get_or_create(**data)

        if activity[1] == True:
            serialized = ActivitySerializer(activity[0])

            return Response(serialized.data, status=status.HTTP_201_CREATED)
        
        return Response({'error': 'Activity with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):

        activity = Activity.objects.all()
        serialized = ActivitySerializer(activity, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

class OneActivityView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Facilitador_and_instrutor]

    def put(self, request, activity_id=''):
        
        title = request.data['title']
        points = request.data['points']       
        
        try:
            activity = Activity.objects.get(id=activity_id)

        except ObjectDoesNotExist:

            return Response({"error": "invalid activity_id"}, status=status.HTTP_404_NOT_FOUND)

        serialized = ActivitySerializer(activity)

        if len(serialized.data['submissions']) > 0:
            return Response({'error': 'You can not change an Activity with submissions'}, status=status.HTTP_400_BAD_REQUEST)

        unique_title = Activity.objects.filter(title=title)
        if len(unique_title) > 0:
            return Response({'error': 'Activity with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
        activity.title = title
        activity.points = points
        activity.save()

        serialized = ActivitySerializer(activity)        

        return Response(serialized.data, status=status.HTTP_200_OK)
       

class ActivitySubmissionView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Estudante]

    def post(self, request, activity_id=''):
        
        activity = Activity.objects.get(id=activity_id)
        user = User.objects.get(id=request.user.__dict__["id"])

        submission_info = {
            'grade' : None,
            'repo' : request.data['repo'],
            'user' : user,
            'activity' : activity
        }

        submission = Submission.objects.create(**submission_info)

        serialized = SubmissionSerializer(submission)
   
        return Response(serialized.data, status=status.HTTP_201_CREATED)
