from ..models import  SampleModelForeignKey
from rest_framework import serializers
from rest_framework import viewsets

class SampleModelForeignKeySerializer(serializers.ModelSerializer):
	class Meta:
		model = SampleModelForeignKey 
		fields=['id', 'name', 'sample_model_id']