import json

from scm.v1.ultilities import get_data


def serizalization_user_privileges(url):
    try:
        list_user_privileges =  get_data(url)
        dict_user_privileges = {}
        if list_user_privileges is not None:
            json_user_privileges = json.loads(list_user_privileges)
            for user_privileges in json_user_privileges:
                dict_user_privileges[user_privileges['repository']['slug']] = {}
                # print(user_privileges)
            for user_privileges in json_user_privileges:
                data = {
                    'privilege': user_privileges['privilege'],
                    'user': user_privileges['user'],
                    # 'repositories': project['links']['repositories']['href'],
                    # 'name': project["name"],
                    # 'created': project['created_on'],
                    # 'updated': project['updated_on'],
                    # 'is_private': project['is_private'],
                    # 'description': project['description'],
                }
                dict_user_privileges[user_privileges['repository']['slug']][user_privileges["user"]["username"]] = data
        return dict_user_privileges
    except Exception as e:
        print(e)
        return None