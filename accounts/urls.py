from django.urls import path
from .views import LoginView, AccountsView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('accounts/', AccountsView.as_view()),
]