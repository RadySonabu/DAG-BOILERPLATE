from ..models import  *
from rest_framework import serializers
from rest_framework import viewsets
from django_restql.mixins import DynamicFieldsMixin

class InputMyUserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
	# role_id = serializers.PrimaryKeyRelatedField(queryset = Roles.objects.select_related().all(), source="role")
	class Meta:
		model = MyUser 
		exclude = ['groups', 'user_permissions', 'username']
		depth=4
	
	def create(self, validated_data):
		user = super(InputMyUserSerializer, self).create(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

class OutputMyUserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
	class Meta:
		model = MyUser 
		fields=['id', 'password', 'first_name', 'last_name', 'email', 'created_at', 'updated_at']
		depth=4