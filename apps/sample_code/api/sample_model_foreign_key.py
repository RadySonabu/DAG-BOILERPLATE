from ..models import  SampleModelForeignKey
from rest_framework import viewsets
from ..serializers.sample_model_foreign_key import *



class SampleModelForeignKeyView(viewsets.ModelViewSet):
	queryset=SampleModelForeignKey.objects.all()
	serializer_class=SampleModelForeignKeySerializer