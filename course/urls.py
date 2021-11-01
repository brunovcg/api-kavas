from django.urls import path
from course.views import CourseView, OneCourseView, CourseRegistrationsView


urlpatterns = [

    path('', CourseView.as_view()),
    path('<int:course_id>/', OneCourseView.as_view()),
    path('<int:course_id>/registrations/', CourseRegistrationsView.as_view())
]