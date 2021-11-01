from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from kanvas.permissions import Instrutor
from rest_framework.permissions import IsAuthenticated
from course.models import Course
from .serializers import CourseSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User



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
        data = request.data

        try:
            course = Course.objects.get(id=course_id)
            course.name = data["name"]
            course.save()
        except ObjectDoesNotExist:
            return Response({"error": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)


        serialized = CourseSerializer(course)


        return Response(serialized.data, status=status.HTTP_200_OK)


    def get(self,request,course_id=''):

        try:
            course = Course.objects.get(id=course_id)
            serialized = CourseSerializer(course)
        except ObjectDoesNotExist:
            return Response({"error": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def delete(self, request,course_id=''):
        OneCourseView.authentication_classes = [TokenAuthentication]
        OneCourseView.permission_classes = [IsAuthenticated, Instrutor]

        try:
            course = Course.objects.get(id=course_id)
            course.delete()
        except ObjectDoesNotExist:
            return Response({"error": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)



class CourseRegistrationsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Instrutor]
    
    def put(self, request, course_id=''):

        users = request.data['user_ids']

        if not type(users) == list:
            return Response({"errors": "user_ids must be a list(array)"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(id=course_id)

        except ObjectDoesNotExist:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        course.users.set([])
        


        for user_id in users:
            try:
                user = User.objects.get(id=user_id)

                if user.is_staff or user.is_superuser:
                    return Response({"errors": "Only students can be enrolled in the course."}, status=status.HTTP_404_NOT_FOUND)

                course.users.add(user)

            except ObjectDoesNotExist:
                return Response({"errors": "invalid user_id list"}, status=status.HTTP_404_NOT_FOUND)
          
        serialized = CourseSerializer(course)

        return Response(serialized.data, status=status.HTTP_200_OK)


