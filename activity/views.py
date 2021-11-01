from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from kanvas.permissions import Facilitador, Instrutor, Estudante


class ActivitiesView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Instrutor, Facilitador]

    def post(self, request):
        return Response({'msg': 'Criando uma atividade'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response({'msg': 'Listando Atividades'}, status=status.HTTP_200_OK)

class OneActivityView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Instrutor, Facilitador]

    def put(self, request):
        return Response({'msg': 'Atualizando Atividades'}, status=status.HTTP_200_OK)

class ActivitySubmissionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Estudante]
    def post(self, request):
        return Response({'msg': 'Fazendo uma submissão'}, status=status.HTTP_201_CREATED)