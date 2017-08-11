from vm.models import Instance

class InstanceFunction:

    def create_instance(self, instance_type):
        try:
            instance_obj, created = Instance.objects.get_or_create(instance_type=instance_type)
#            instance_obj.instance_name = 
        except Exception as ex:
            return None