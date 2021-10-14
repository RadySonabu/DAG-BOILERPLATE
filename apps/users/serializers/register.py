from ..models import *
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    # class Meta:
    #     model = MyUser
    #     fields = ['first_name', 'last_name','email', 'password', 'confirm_password']

    def validate_email(self, email):
        existing = MyUser.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                "address has already registered. Was it you?")
        return email

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            username=validated_data['email'], 
            email= validated_data['email'], 
            first_name= validated_data['first_name'], 
            last_name= validated_data['last_name'],
            # role= validated_data['role'],
            password=validated_data['password'], 
            )

        return user

class VerifiedUser(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', "password"]