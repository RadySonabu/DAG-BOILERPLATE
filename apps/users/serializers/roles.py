from ..models import  *
from rest_framework import serializers
from rest_framework import viewsets
from django_restql.mixins import DynamicFieldsMixin

class InputRolesSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
	class Meta:
		model = Roles 
		fields='__all__'
		depth=4

class OutputRolesSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
	class Meta:
		model = Roles 
		fields=['id', 'active_status', 'created_by', 'created_date', 'modified_by', 'modified_date', 'role']
		depth=4