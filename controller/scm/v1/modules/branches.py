import json

from scm.v1.ultilities import get_data


def serizalization_branches(url):
    try:
        list_branches =  get_data(url)
        dict_branches = {}
        if list_branches is not None:
            json_branches = json.loads(list_branches)
            # print(json_branches)
            branches = json_branches["values"]
            for branch in branches:
                print(branch["name"])
                # dict_branches[branch["repository"]["slug"]] = {}
            # for group_privileges in json_group_privileges:
            #     data = {
            #         'privilege': group_privileges['privilege'],
            #         'user': group_privileges['group'],
            #     }
            #     dict_group_privileges[group_privileges["repository"]["slug"]][group_privileges["group"]["name"]] = data
        return dict_group_privileges
    except Exception as e:
        print(e)
        return None