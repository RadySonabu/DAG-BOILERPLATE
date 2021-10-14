from django_filters import rest_framework as filters
from django_restql.mixins import QueryArgumentsMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import MyUser
from ..serializers.my_user import *


class MyUserView(QueryArgumentsMixin, viewsets.ModelViewSet):
	queryset=MyUser.objects.prefetch_related().all()
	serializer_class=OutputMyUserSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	permission_classes = [IsAuthenticated,]
	filterset_fields = ['id', 'password',  'username', 'first_name', 'last_name', 'email', 'created_at', 'updated_at']
	
	def get_serializer_class(self):
		input_serializer = InputMyUserSerializer
		output_serializer = OutputMyUserSerializer
		if self.action == 'list':
			return output_serializer
		if self.action == 'retrieve':
			return output_serializer
		if self.action == 'create':
			return input_serializer
		if self.action == 'update':
			return input_serializer

		return output_serializer

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)

		if getattr(instance, '_prefetched_objects_cache', None):
			# If 'prefetch_related' has been applied to a queryset, we need to
			# forcibly invalidate the prefetch cache on the instance.
			instance._prefetched_objects_cache = {}

		
		email_value = serializer['email'].value
		email = MyUser.objects.get(email=email_value)
		refresh = RefreshToken.for_user(email)
		return Response({
			"user": {
					"id": 1,
					"firstname": serializer['first_name'].value,
					"lastname": serializer['last_name'].value,
					"email": serializer['email'].value,
					"password": serializer['password'].value,
					"created_at": serializer['created_at'].value,
					"updated_at": serializer['updated_at'].value
				},
			"message": "Successfully updated!",
			"token": str(refresh)

			})
                    