from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from kanvas.permissions import Facilitador, Instrutor, Estudante


class OneSubmissionView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Instrutor, Facilitador]

    def put(self, request):
        
        return Response({'msg': 'Editando nota de submissão'}, status=status.HTTP_201_CREATED)

class SubmissionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Instrutor, Facilitador, Estudante]
    
    def get(self, request):
        return Response({'msg': 'Listando submission'}, status=status.HTTP_200_OK)        