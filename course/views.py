from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from kanvas.permissions import Instrutor
from rest_framework.permissions import IsAuthenticated
from course.models import Course
from .serializers import CourseSerializer


class CourseView(APIView):  

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [Instrutor, IsAuthenticated]

    def post(self, request):
       
        CourseView.authentication_classes = [TokenAuthentication]
        CourseView.permission_classes = [Instrutor, IsAuthenticated]

        name = request.data['name']

        add_course = Course.objects.get_or_create(name=name)

        if add_course[1] == True:

            serialized = CourseSerializer(add_course[0])

            return Response(serialized.data, status=status.HTTP_201_CREATED)
        
        return Response({'error': 'Course with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)
        

    def get(self, request):

        course = Course.objects.all()

        serialized = CourseSerializer(course, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)


class OneCourseView(APIView):
    def put(self, request, course_id=''):
        OneCourseView.authentication_classes = [TokenAuthentication]
        OneCourseView.permission_classes = [IsAuthenticated, Instrutor]

        return Response({'msg': 'Atualizando Curso Especifico'}, status=status.HTTP_200_OK)

    def get(self,request,course_id=''):


        return Response({'msg': 'Filtrando um curso'}, status=status.HTTP_200_OK)

    def delete(self, request,course_id=''):
        OneCourseView.authentication_classes = [TokenAuthentication]
        OneCourseView.permission_classes = [IsAuthenticated, Instrutor]

        return Response({'msg': 'Deletando curso especifico'}, status=status.HTTP_204_NO_CONTENT)


class CourseRegistrationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Instrutor]
    
    def put(self, request, course_id=''):
        return Response({'msg': 'Atualizando lista de alunos matriculados'}, status=status.HTTP_200_OK)


