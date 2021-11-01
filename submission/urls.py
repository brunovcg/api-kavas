from django.urls import path
from submission.views import OneSubmissionView, SubmissionView

urlpatterns = [
    path('submissions/', SubmissionView.as_view()),
    path('submissions/<int:submission_id>/', OneSubmissionView.as_view())
]