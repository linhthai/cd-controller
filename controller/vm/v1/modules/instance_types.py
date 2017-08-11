import datetime

from vm.v1.models import InstanceTypes


class InstanceTypesFunction:

    def create(self, **kwargs):
        try:
            ins_type_object, create = InstanceTypes.objects.get_or_create(type_instances=kwargs['type_instances'])
            if not ins_type_object:
                ins_type_object.type_instances = kwargs['type_instances']
                ins_type_object.type_instances_name = kwargs['type_instances_name']
                ins_type_object.created_date = datetime.date.today()
                ins_type_object.save()
            return ins_type_object
        except Exception as ex:
            print(ex)
            return None

    def update(self, **kwargs):
        try:
            obj = self.get_by_id(kwargs['id'])
            if not obj:
                return None
            obj.type_instances = kwargs['type_instances']
            obj.type_instances_name = kwargs['type_instances_name']
            obj.modified_date = datetime.date.today()
            obj.save()
            return obj
        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id):
        try:
            return InstanceTypes.objects.get(pk=id)
        except Exception as e:
            print(e)
            return None

    def get_all(self):
        try:
            return InstanceTypes.objects.all()
        except Exception as ex:
            print(ex)
            return None