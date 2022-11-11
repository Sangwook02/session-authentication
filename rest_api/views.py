from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from rest_framework.permissions import AllowAny
from .models import User
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