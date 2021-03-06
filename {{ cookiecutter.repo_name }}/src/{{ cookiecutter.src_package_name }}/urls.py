from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, views, response


schema_view = get_schema_view(
    openapi.Info(
        title="{{ cookiecutter.project_title }} API",
        default_version="v1",
        description="{{ cookiecutter.project_description }}",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="{{ cookiecutter.author_email }}"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class HealthCheck(views.APIView):
    def get(self, request, *args, **kwargs):
        return response.Response()


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("health-check/", HealthCheck.as_view()),
    path("admin/", admin.site.urls),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
