import requests
import json

from django.conf import settings
from rest_framework.views import APIView

from vm.response import response_data_with_page, response_message
from vm.exceptions import V1Exception
from scm.v1.ultilities import auth_headers
from scm.v1.modules import repo
from scm.v1.modules import projects
from scm.v1.modules import user_privileges
from scm.v1.modules import group_privileges
from scm.v1.modules import branches


class bitbucket_get_all_repo(APIView):
    def get(self, request):
        try:
            # url = settings.BITBUCKET_URL + '/' + settings.BITBUCKET_VER + \
            # '/repositories/' + settings.BITBUCKET_TEAM 
            # url = settings.BITBUCKET_URL + '/' + settings.BITBUCKET_VER + \
            #     '/teams/' + settings.BITBUCKET_TEAM + '/projects/'
            # demo lay thu mot project
            url = "https://api.bitbucket.org/2.0/repositories/dzonesvn?q=project.key=\"VSN\""
            result = repo.serizalization_reponame(url)
            return response_data_with_page(result)
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")


class bitbucket_get_user_privileges(APIView):
    def get(self, request):
        try:
            url = "https://api.bitbucket.org/1.0/privileges/dzonesvn"
            result = user_privileges.serizalization_user_privileges(url)
            return response_data_with_page(result)
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")


class bitbucket_get_group_privileges(APIView):
    def get(self, request):
        try:
            url = "https://api.bitbucket.org/1.0/group-privileges/dzonesvn"
            result = group_privileges.serizalization_group_privileges(url)
            return response_data_with_page(result)
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")


class  bitbucket_get_all_project(APIView):
    def get(self, request):
        try:
            PF_driver = projects.ProjectsFunction(settings.BITBUCKET_TEAM)
            result = PF_driver.get_projects_from_bitbucket()
            return response_data_with_page(result)
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")


class bitbucket_get_branches(APIView):
    def get(self, request):
        try:
            url = "https://api.bitbucket.org/2.0/repositories/dzonesvn/services-content-manager/refs/branches"
            result = branches.serizalization_branches(url)
            return response_data_with_page(result)
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")