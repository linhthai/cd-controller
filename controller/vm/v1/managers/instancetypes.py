import datetime

from vm.v1.models import InstanceTypes


class InstanceTypesFunction:

    def create(self, type_instance):
        try:
            ins_type_object, create = InstanceTypes.objects.get_or_create(type_instance=type_instance)
            if not ins_type_object:
                ins_type_object.type_instance = type_instance
                ins_type_object.created_date = datetime.date.today()
                ins_type_object.save()
            return ins_type_object
        except Exception as ex:
            print(ex)
            return None

    def get_all(self):
        try:
            return InstanceTypes.objects.all()
        except Exception as ex:
            print(ex)
            return None