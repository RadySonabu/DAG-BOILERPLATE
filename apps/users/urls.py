
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.roles import RolesView
from .api.my_user import MyUserView
from .api.register import RegisterInfoViews
from .api.login import UserLogIn
from .api.logout import UserLogout

router = DefaultRouter()

# router.register("roles", RolesView)
router.register("users", MyUserView)


urlpatterns = [
    path("", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/register/", RegisterInfoViews.as_view(), name="register"),
    path("api/authenticate/", UserLogIn.as_view(), name="login"),
    path("api/logout/", UserLogout.as_view(), name="logout"),
    ]