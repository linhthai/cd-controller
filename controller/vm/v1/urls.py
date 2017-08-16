from django.conf.urls import url
from vm.views import *

from vm.v1.views.instance_types import instancetypes_get as ITG
from vm.v1.views.instance_types import instancetypes_get_all_name as ITGAN
from vm.v1.views.instance_types import instancetypes_update as ITU
from vm.v1.views.instance_types import instancetypes_create as ITC

from vm.v1.views.instance import instance_get as INSG
from vm.v1.views.instance import instance_create as INSC
from vm.v1.views.instance import instance_update as INSU

urlpatterns = (
    url(r'^index$', Test.as_view(), name='index'),
    url(r'^instancetype$', ITG.as_view(), name='get_info'),
    url(r'^instancetype/getallname$', ITGAN.as_view(), name='get_all_instance_name'),
    url(r'^instancetype/update$', ITU.as_view(), name='update_info'),
    url(r'^instancetype/create$', ITC.as_view(), name='create_info'),
    url(r'^instance$', INSG.as_view(), name='get_info'),
    url(r'^instance/create$', INSC.as_view(), name='create_instance'),
    url(r'^instance/update$', INSU.as_view(), name='update_instance'),
)