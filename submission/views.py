from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class OneSubmissionView(APIView):
    def put(self, request):
        return Response({'msg': 'Editando nota de submissão'}, status=status.HTTP_201_CREATED)

class SubmissionView(APIView):
    def get(self, request):
        return Response({'msg': 'Listando submission'}, status=status.HTTP_200_OK)        