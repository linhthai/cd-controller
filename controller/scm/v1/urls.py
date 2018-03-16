from django.conf.urls import url
from scm.v1.views.bitbucket import bitbucket_get_all_repo as BGAR
from scm.v1.views.bitbucket import bitbucket_get_all_project as BGAP
from scm.v1.views.bitbucket import bitbucket_get_user_privileges as BGUP
from scm.v1.views.bitbucket import bitbucket_get_group_privileges as BGGP
from scm.v1.views.bitbucket import bitbucket_get_branches as BGB


urlpatterns = (
    url(r'^repo$', BGAR.as_view(), name='get_all_repo'),
    url(r'^project$', BGAP.as_view(), name='get_all_project'),
    url(r'^user_privileges$', BGUP.as_view(), name='get_all_user_privileges'),
    url(r'^group_privileges$', BGGP.as_view(), name='get_all_group_privileges'),
    url(r'^branches$', BGB.as_view(), name='get_branches'),
)