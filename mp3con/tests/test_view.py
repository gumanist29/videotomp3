from django.contrib.sites import requests
from mock import call, patch
from requests import request

from mp3con.views import HomeView


@patch.object(requests,'get')
def test_response_verify(self, mock_requests):

    mock_requests.get.return_value.status_code = 200

    response = HomeView().post(request, {'urls': 'some_url'})

    self.assertEqual(
        mock_requests.get.call_args_list,
        [call('some_url', params={'verify': 'hello'})]
    )
