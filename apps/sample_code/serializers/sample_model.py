from ..models import  SampleModel
from rest_framework import serializers
from rest_framework import viewsets

class SampleModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SampleModel 
		fields=['id', 'name', 'description']