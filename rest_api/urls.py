from django.urls import path
from . import views

app_name = 'rest_api'

urlpatterns = [
    path('register/', views.createAccount.as_view()),
    path('login/', views.login.as_view(), name='login'),
    path('logout/', views.logout.as_view()),
]