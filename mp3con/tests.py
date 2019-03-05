import re

# from django.test import TestCase
#
# from django.urls import reverse
# from .redis import download_mp3
#
#
# class UtuberPageTests(TestCase):
#
#     def test_url_code(self):
#         response = self.client.get('index')
#         self.assertEquals(response.status_code, 200)
#
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('base'))
#         self.assertEquals(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('/templates/base/'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'base.html')
#
#     def test_error_html(self):
#         response = self.client.get('templates')
#         self.assertNotContains(response, 'anywhere i should not be in page.')



def youtube_url_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(6)

    return youtube_regex_match

    youtube_urls_test = [
        'http://www.youtube.com/watch?v=5Y6HSHwhVlY',
        'http://youtu.be/5Y6HSHwhVlY',
        'http://www.youtube.com/embed/5Y6HSHwhVlY?rel=0" frameborder="0"',
        'https://www.youtube-nocookie.com/v/5Y6HSHwhVlY?version=3&amp;hl=en_US',
        'http://www.youtube.com/',
        'http://www.youtube.com/?feature=ytca']


    for url in youtube_urls_test:
        m = youtube_url_validation(url)
        if m:
            return HttpResponse("Ok")
            # print ('OK {}'.format(url))
            # print (m.groups())
            # print (m.group(6))
        else:
            return HttpResponse("Fail")