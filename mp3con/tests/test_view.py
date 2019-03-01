import unittest

class TestStringMethods(unittest.TestCase):

    def test_url_code(self):
        response = self.client.get('/templates/index')
        self.assertEquals(response.status_code, 200)



    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()