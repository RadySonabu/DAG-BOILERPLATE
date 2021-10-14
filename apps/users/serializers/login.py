from ..models import MyUser
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', "password"]