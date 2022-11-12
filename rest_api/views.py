from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from .models import User
from django.contrib.auth.hashers import check_password
# Create your views here.
class createAccount(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user_info': {
                'id': user.id
            },
        },
            status=status.HTTP_200_OK)

class login(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)

        #pw 확인
        input_id = request.data['user_id']
        input_pw = request.data['password']
        data_from_DB = User.objects.get(user_id=input_id)
        if(check_password(input_pw,data_from_DB.password)):
            request.session['user'] = data_from_DB.user_id
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class logout(APIView):
    permission_classes = [AllowAny]
    def delete(self, request):
        try:
            request.session.flush()
            return redirect('rest_api:login')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
