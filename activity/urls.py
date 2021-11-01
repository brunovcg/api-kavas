from django.urls import path
from activity.views import ActivitiesView, OneActivityView, ActivitySubmissionView


urlpatterns = [

    path('', ActivitiesView.as_view()),
    path('<int:activity_id>/', OneActivityView.as_view()),
    path('<int:activity_id>/submissions/', ActivitySubmissionView.as_view())
]