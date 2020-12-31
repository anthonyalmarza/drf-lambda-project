import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from CHANGE_ME.urls import urlpatterns as prod_urlpatterns


urlpatterns = (
    [
        path("__debug__/", include(debug_toolbar.urls))
    ]
    + prod_urlpatterns
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
