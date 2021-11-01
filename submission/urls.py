from django.urls import path
from submission.views import OneSubmissionView, SubmissionView

urlpatterns = [
    path('', SubmissionView.as_view()),
    path('<int:submission_id>/', OneSubmissionView.as_view())
]