
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.sample_model import SampleModelView
from .api.sample_model_foreign_key import SampleModelForeignKeyView

router = DefaultRouter()

router.register("sample-model", SampleModelView)
router.register("sample-model-foreign-key", SampleModelForeignKeyView)


urlpatterns = [path("", include("rest_framework.urls")),path("api/", include(router.urls)),]