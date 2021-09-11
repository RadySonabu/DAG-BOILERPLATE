
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.roles import RolesView
from .api.my_user import MyUserView

router = DefaultRouter()

router.register("roles", RolesView)
router.register("my-user", MyUserView)


urlpatterns = [path("", include("rest_framework.urls")),path("api/", include(router.urls)),]