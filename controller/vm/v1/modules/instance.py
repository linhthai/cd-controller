from vm.v1.models import Instance, InstanceTypes
from vm.v1.modules.instance_types import InstanceTypesFunction

class InstanceFunction:

    def create(self, **kwargs):
        try:
            instance_type_id = kwargs['instance_type']
            itf_driver = InstanceTypesFunction()
            instype_obj = itf_driver.get_by_id(kwargs['instance_type'])
            if instype_obj:
                instance_type_id = instype_obj.id
            instance_obj, created = Instance.objects.get_or_create(instance_name=kwargs['instance_name'],
                                                                   ip_address=kwargs['ip_address'],
                                                                   instance_type=instype_obj)
            if instance_obj and created is True:
                instance_obj.description = kwargs['description']
                instance_obj.status = INSTANCE_STATUS.INS_STT_INIT
                instance_obj.save()
            return instance_obj
        except Exception as ex:
            print(ex)
            return None

    def get(self):
        try:
            return Instance.objects.all()
        except Exception as ex:
            return None

    def get_by_id(self, id):
        try:
            return Instance.objects.get(pk=id)
        except Exception as e:
            print(e)
            return None

