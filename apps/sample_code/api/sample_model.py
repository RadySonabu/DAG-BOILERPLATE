from ..models import  SampleModel
from rest_framework import viewsets
from ..serializers.sample_model import *



class SampleModelView(viewsets.ModelViewSet):
	queryset=SampleModel.objects.all()
	serializer_class=SampleModelSerializer