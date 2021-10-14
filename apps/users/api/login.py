from rest_framework import viewsets, generics, permissions, mixins
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import generics, status, views, permissions
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import os
from rest_framework.permissions import IsAuthenticated, AllowAny
import requests 

from ..serializers.login import LoginSerializer
from ..models import *

class UserLogIn(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny,]

    def post(self, request, *args,  **kwargs): 
        data = request.data
        user = MyUser.objects.get(email=data['email'])
        print(user.email)
        refresh = RefreshToken.for_user(user)

        if user.email is not None:

            return Response({
                # 'status' : 200,
                "user": {
                    "id": user.id,
                    "firstname": user.first_name,
                    "lastname": user.last_name,
                    "email": user.email,
                    "password": user.password,
                    "created_at": user.date_joined,
                    # "created_at": "2021-09-20"
                },
                "token": str(refresh.access_token)

            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 404,
                'error': 
                    {
                        "message" : "Invalid username or password. User may not yet register in the system"
                    }
            }, status=status.HTTP_404_NOT_FOUND)