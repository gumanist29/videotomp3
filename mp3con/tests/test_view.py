import unittest

class TestStringMethods(unittest.TestCase):

    def test_url_code(self):
        response = self.client.post('url')
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()