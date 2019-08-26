from django.http import request
from django.urls import reverse
from mock import call, patch, MagicMock
from mp3con.redis import download_mp3


from django.test import TestCase


class UtuberTestCase(TestCase):
    @patch('mp3con.redis.download_mp3')
    def test_success_download_mp3(self, mocked_fun):
        y_url = 'http://www.youtube.com/watch?v=5Y6HSHwhVlY'
        # mocked_fun.download_mp3.asser_called_once()
        #resp = self.client.post(reverse('mp3con:index'), data={'url': y_url})
        resp = self.client.post('mp3con:index', data={'url': y_url})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Downloaded check in your Folder")




    def test_list_of_stories(self):
            url = reverse('base')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)



    def test_index(self):
            url = reverse('index')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

