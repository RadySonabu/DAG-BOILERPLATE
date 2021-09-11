from ..models import  Roles
from django_restql.mixins import QueryArgumentsMixin
from rest_framework import viewsets
from ..serializers.roles import *
from django_filters import rest_framework as filters



class RolesView(QueryArgumentsMixin, viewsets.ModelViewSet):
	queryset=Roles.objects.select_related().all()
	serializer_class=OutputRolesSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	def get_serializer_class(self):
		input_serializer = InputRolesSerializer
		output_serializer = OutputRolesSerializer
		if self.action == 'list':
			return output_serializer
		if self.action == 'retrieve':
			return output_serializer
		if self.action == 'create':
			return input_serializer
		if self.action == 'update':
			return input_serializer

		return output_serializer
                    