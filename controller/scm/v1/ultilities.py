import base64
import requests
import json

from django.conf import settings

def auth_headers(username,password):
    """
    Authenticate when get info
    Input:  username,password
    Output: 'Basic base64(username:password)'
    """
    try:
        str_ = '%s:%s' % (username,password)
        return 'Basic ' + base64.b64encode(str_.encode()).decode()
    except Exception as e:
        print(e)
        return False

def get_data(url, parameter=None):
    try:
        result = None
        url = url
        if parameter is not None:
            url = url + '?' + parameter
        auth = auth_headers(settings.BITBUCKET_USER,
                            settings.BITBUCKET_PA)
        headers  = {"Authorization": auth}
        response = requests.get(url, headers=headers)
        if response is None:
            return None
        elif response.status_code == 200:
            result = response.content.decode('ascii', 'ignore')
        return result
    except Exception as e:
        print(e)
        return None