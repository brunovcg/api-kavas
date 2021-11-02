from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from kanvas.permissions import Facilitador_and_instrutor, Instrutor, Estudante
from submission.models import Submission
from submission.serializers import SubmissionSerializer


class OneSubmissionView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, Facilitador_and_instrutor]

    def put(self, request, submission_id=''):

        grade = request.data['grade']

        submission = Submission.objects.get(id=submission_id)

        submission.grade = grade

        submission.save()

        serialized = SubmissionSerializer(submission)
        
        return Response(serialized.data, status=status.HTTP_200_OK)
        

class SubmissionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user.__dict__

        if user['is_staff'] == False:
            submissions = Submission.objects.filter(user_id=user['id'])

        else:
            submissions = Submission.objects.all()

        serialized = SubmissionSerializer(submissions, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)        