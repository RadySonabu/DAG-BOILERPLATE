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

from ..serializers.register import RegisterSerializer
from ..models import *

from rest_framework.permissions import IsAuthenticated, AllowAny

class RegisterInfoViews(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]
    def post(self, request, *args,  **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # Save user
        user = serializer.save()
        # Generate Token
        email = MyUser.objects.get(email=user.email)
        refresh = RefreshToken.for_user(email)

        return Response({
            "user": {
                'id': user.id,
                "firstname": user.first_name,
                "lastname": user.last_name,
                "email": user.email,
                "password": user.password,
                "created_at": user.date_joined

            },
            "message": "User Created Successfully.  Now perform Login to get your token",
            "token": str(refresh)
        })