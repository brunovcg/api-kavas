from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ActivitiesView(APIView):
    def post(self, request):
        return Response({'msg': 'Criando uma atividade'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response({'msg': 'Listando Atividades'}, status=status.HTTP_200_OK)

class OneActivityView(APIView):
    def put(self, request):
        return Response({'msg': 'Atualizando Atividades'}, status=status.HTTP_200_OK)

class ActivitySubmissionView(APIView):
    def post(self, request):
        return Response({'msg': 'Fazendo uma submissão'}, status=status.HTTP_201_CREATED)