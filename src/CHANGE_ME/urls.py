from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="CHANGE_ME API",
        default_version="v1",
        description="CHANGE_ME",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@fake.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", admin.site.urls),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    )
]