from django.conf.urls import url
from vm.views import *
from vm.v1.views.instance_types import instancetypes_get as ITG
from vm.v1.views.instance_types import instancetypes_update as ITU
from vm.v1.views.instance_types import instancetypes_create as ITC

urlpatterns = (
    url(r'^index$', Test.as_view(), name='index'),
    url(r'^instancetype$', ITG.as_view(), name='get_info'),
    url(r'^instancetype/update$', ITU.as_view(), name='update_info'),
    url(r'^instancetype/create$', ITC.as_view(), name='update_info'),
)