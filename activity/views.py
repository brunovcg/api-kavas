from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from kanvas.permissions import Facilitador, Instrutor, Estudante
from activity.serializers import ActivitySerializer
from activity.models import Activity 


class ActivitiesView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [Facilitador, Instrutor]

    def post(self, request):

        data = request.data

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
    permission_classes = [IsAuthenticated, Instrutor, Facilitador]

    def put(self, request, activity_id=''):



        return Response({'msg': 'Atualizando Atividades'}, status=status.HTTP_200_OK)

class ActivitySubmissionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Estudante]
    def post(self, request, activity_id=''):
        return Response({'msg': 'Fazendo uma submissão'}, status=status.HTTP_201_CREATED)