from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.createAccount.as_view()),
]