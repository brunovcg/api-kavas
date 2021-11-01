from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CourseView(APIView):
    def post(self, request):
        return Response({'msg': 'Criando Curso'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response({'msg': 'Obtendo toda a lista de alunos'}, status=status.HTTP_201_CREATED)


class OneCourseView(APIView):
    def put(self, request):

        return Response({'msg': 'Atualizando Curso Especifico'}, status=status.HTTP_200_OK)

    def get(self,request):
        return Response({'msg': 'Filtrando um curso'}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response({'msg': 'Deletando curso especifico'}, status=status.HTTP_204_NO_CONTENT)


class CourseRegistrationsView(APIView):
    def put(self, request):
        return Response({'msg': 'Atualizando lista de alunos matriculados'}, status=status.HTTP_200_OK)


