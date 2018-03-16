import json
from django.conf import settings

from scm.v1.ultilities import get_data
from scm.v1.models import Projects

class ProjectsFunction:

    user = None

    def __init__(self, user):
        self.user = user

    def create(self, **kwargs):
        try:
            project_obj, created = Projects.objects.get_or_create(uuid=kwargs['uuid'],
                                                                    owner=self.user,
                                                                    name=kwargs['name'],
                                                                    key=kwargs['key'])
            print(project_obj)
            if project_obj and created is True:
                project_obj.description = kwargs['description']
                project_obj.is_private = kwargs['is_private']
                project_obj.created_date = kwargs['created']
                project_obj.modified_date = kwargs['updated']
                project_obj.save()
            return project_obj, True
        except Exception as ex:
            print(ex)
            return None, False


    def get_projects_from_bitbucket(self):
        try:
            url = settings.BITBUCKET_URL + '/' + settings.BITBUCKET_VER + \
                '/teams/' + settings.BITBUCKET_TEAM + '/projects/'
            list_project =  get_data(url)
            dict_project_name = {}
            if list_project is not None:
                json_project = json.loads(list_project)
                pagelen = int(json_project["pagelen"])
                # size_br = int(json_branch["size"])
                page_br = int(json_project["page"])
                # page_next = json_branch["next"]
                list_values_project = json_project["values"]

                for project in list_values_project:
                    data = {
                        'uuid': project['uuid'],
                        'repositories': project['links']['repositories']['href'],
                        'name': project["name"],
                        'created': project['created_on'],
                        'updated': project['updated_on'],
                        'is_private': project['is_private'],
                        'description': project['description'],
                        'key': project["key"],
                    }
                    project_obj, result = self.create(**data)
                    if result is False:
                        print(project)
            return True
        except Exception as ex:
            print(ex)
            return None


    def get(self):
        try:
            return Projects.objects.all()
        except Exception as ex:
            return None


    def get_by_key(self, key):
        try:
            return Projects.objects.get(key=key)
        except Exception as e:
            print(e)
            return None


