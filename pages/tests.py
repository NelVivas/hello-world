from django.test import SimpleTestCase # Use SimpleTestCase if there's no database
                                       # TestCase otherwise

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        return self.assertEqual(response.status_code, 200)
    def test_about_page_statusd_code(self):
        response = self.client.get('/about/')
        return self.assertEqual(response.status_code, 200)