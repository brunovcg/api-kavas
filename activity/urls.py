from django.urls import path
from activity.views import ActivitiesView, OneActivityView, ActivitySubmissionView


urlpatterns = [

    path('activities/', ActivitiesView.as_view()),
    path('activities/<int:activity_id>/', OneActivityView.as_view()),
    path('activities/<int:activity_id>/submissions/', ActivitySubmissionView.as_view())
]