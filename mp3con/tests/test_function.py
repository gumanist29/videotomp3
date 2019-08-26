# import unittest
# from django.test import Client
# from mp3con.models import Utuber
#
#
# class SimpleTest(unittest.TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_details(self):
#         response = self.client.get('/stories/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.context['stories']), 10)
#
#     def testread(self):
#         request = Utuber.objects.all()
#         context = {'all_link_list': all_link_list}
#         self.assertEqual(len(request.context) )

# #
# #
# #
# #     # c = Client()
# #     # response = c.post('/base/', {'stories: '})
#     # self.assertTemplateUsed(response, 'base.html')
#
# from mp3con.redis import download_mp3
#
#
# class DownloadResponseTestCase(unittest.TestCase):
#     def test_content_disposition_encoding(self):
#         """Content-Disposition header is encoded."""
#         response = download_mp3('fake file' ,attachment=True,
#                                     basename=u'espacé .txt',)
#         headers = response.default_headers
#         self.assertIn("filename=\"espace_.txt\"",
#                       headers['Content-Disposition'])
#         self.assertIn("filename*=UTF-8''espac%C3%A9%20.txt",
# headers['Content-Disposition'])