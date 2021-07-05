import os, re
from textwrap import dedent
from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):

    help = "Create serializers and views"
    # Gets the name of the app
    def add_arguments(self, parser):
        parser.add_argument("app", type=str, nargs="+", help="Get the app name")

    def handle(self, *args, **kwargs):
        app_name = kwargs["app"][0]
        # new_project_name = kwargs['new'][0]

        base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        )
        path = base_dir + "\\apps" + "\\" + app_name
        serializers_path = path + "\\serializers"
        views_path = path + "\\api"
        try:
            os.mkdir(serializers_path)
        except FileExistsError:
            print("File already exist")
        try:
            os.mkdir(views_path)
        except FileExistsError:
            print("File already exist")
        # read the model classes

        app = apps.get_app_config(app_name).get_models()
        model_names = [apps.get_model(app_name, str(m._meta.object_name)) for m in app]
        model_fields = [m._meta.get_fields() for m in model_names]

        # get field names
        for m in model_names:
            name = re.sub(r"(?<!^)(?=[A-Z])", "_", m.__name__).lower()
            file_path = serializers_path + f"/{name}.py"
            with open(file_path, "w+") as file:
                file.write(f"from ..models import  {m.__name__}")
                file.write(
                    f"\nfrom rest_framework import serializers\nfrom rest_framework import viewsets"
                )
                file.write(
                    f"\n\nclass {m.__name__}Serializer(serializers.ModelSerializer):"
                )
                file.write(f"\n\tclass Meta:\n\t\tmodel = {m.__name__} ")
                fields = []
                for field in m._meta.concrete_fields:
                    field_model = field.model.__name__
                    model = m.__name__

                    if model == field_model:
                        fields.append(field.name)
                file.write(f"\n\t\tfields={fields}")

            # TODO: Generate VIEW
            file_path = views_path + f"/{name}.py"
            with open(file_path, "w+") as file2:
                file2.write(f"from ..models import  {m.__name__}")
                file2.write(f"\nfrom rest_framework import viewsets")
                file2.write(f"\nfrom ..serializers.{name} import *")
                file2.write(
                    f"\n\n\n\nclass {m.__name__}View(viewsets.ModelViewSet):\n\tqueryset={m.__name__}.objects.all()\n\tserializer_class={m.__name__}Serializer"
                )

        url_path = path + "/urls.py"
        with open(url_path, "w+") as file:
            file.write(
                dedent(
                    f"""
                from django.urls import include, path
                from rest_framework.routers import DefaultRouter

                """
                )
            )

            for m in model_names:
                file_name = re.sub(r"(?<=\w)([A-Z])", r"_\1", m.__name__)
                file.write(f"from .api.{file_name.lower()} import {m.__name__}View\n")
            file.write(f"\nrouter = DefaultRouter()\n\n")
            for m in model_names:
                file_name = re.sub(r"(?<=\w)([A-Z])", r"-\1", m.__name__)
                file.write(
                    f'router.register("{file_name.lower()}", {m.__name__}View)\n'
                )

            file.write(
                f'\n\nurlpatterns = [path("", include("rest_framework.urls")),path("api/", include(router.urls)),]'
            )
