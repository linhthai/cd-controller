import requests
import json

from django.conf import settings

from scm.v1.ultilities import auth_headers, get_data


def serizalization_reponame(url):
    try:
        list_repo =  get_data(url)
        dict_repo_name = {}
        if list_repo is not None:
            json_repo = json.loads(list_repo)

            pagelen = int(json_repo["pagelen"])
            size_br = int(json_repo["size"])
            page_br = int(json_repo["page"])
            page_next = json_repo["next"]
            list_values_repo = json_repo["values"]

            for repo in list_values_repo:

                data = {
                    'slug': repo["slug"],
                    'uuid': repo['uuid'],
                    'branches': repo['links']['branches']['href'],
                    'name': repo["name"],
                    'created': repo['created_on'],
                    'updated': repo['updated_on'],
                    'is_private': repo['is_private'],
                    'description': repo['description'],
                }
                dict_repo_name[repo["slug"]] = data
            while size_br > pagelen*page_br:
                list_repo = get_data(page_next)
                if list_repo is not None:
                    json_repo = json.loads(list_repo)
                    page_br = int(json_repo["page"])
                    list_values_repo = json_repo["values"]
                    page_next = json_repo["next"] if "next" in json_repo else "null"
                    for repo in list_values_repo:
                        data = {
                            'slug': repo["slug"],
                            'uuid': repo['uuid'],
                            'branches': repo['links']['branches']['href'],
                            'name': repo["name"],
                            'created': repo['created_on'],
                            'updated': repo['updated_on'],
                            'is_private': repo['is_private'],
                            'description': repo['description'],
                        }
                        dict_repo_name[repo["slug"]] = data
        return dict_repo_name
    except Exception as e:
        print(e)
        return None