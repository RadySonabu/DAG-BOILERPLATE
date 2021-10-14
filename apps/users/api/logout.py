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

class UserLogout(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args,  **kwargs): 
        return Response({"message": "Succesfully logged out!"})