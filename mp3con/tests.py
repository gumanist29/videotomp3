from unittest import TestCase

from django.urls import reverse



class UtuberPageTests(TestCase):

    def test_url_code(self):
        response = self.client.get('urls')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('base'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('/templates/base/'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_error_html(self):
        response = self.client.get('urls')
        self.assertNotContains(response, 'anywhere i should not be in page.')