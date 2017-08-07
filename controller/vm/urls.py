from django.conf.urls import url, include
from .v1 import urls as v1_urls

urlpatterns = (
    url(r'^v1/', include(v1_urls, app_name="apiv1", namespace="apiv1")),
)