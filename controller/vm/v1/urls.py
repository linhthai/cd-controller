from django.conf.urls import url
from vm.views import *
from vm.v1.views.instancetypes import instancetypes_get as ITG

urlpatterns = (
    url(r'^index$', Test.as_view(), name='index'),
    url(r'^instancetype$', ITG.as_view(), name='get_info'),
)