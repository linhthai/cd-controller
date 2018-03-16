import json

from scm.v1.ultilities import get_data


def serizalization_group_privileges(url):
    try:
        list_group_privileges =  get_data(url)
        dict_group_privileges = {}
        if list_group_privileges is not None:
            json_group_privileges = json.loads(list_group_privileges)
            for group_privileges in json_group_privileges:
                dict_group_privileges[group_privileges["repository"]["slug"]] = {}
            for group_privileges in json_group_privileges:
                data = {
                    'privilege': group_privileges['privilege'],
                    'user': group_privileges['group'],
                }
                dict_group_privileges[group_privileges["repository"]["slug"]][group_privileges["group"]["name"]] = data
        return dict_group_privileges
    except Exception as e:
        print(e)
        return None
