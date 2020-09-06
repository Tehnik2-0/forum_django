from django.test import TestCase


class TestRegisterAuth(TestCase):
    def test_register_and_authorization(self):
        response = self.client.get('http://your_server_ip:8000')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/register', {'username': 'admin', 'password': '123456'})
        response = self.client.post('/login', {'username': 'admin', 'password': '123456'})
        response = self.client.get('/')
        user = response.context['user']
        user = user.__str__()
        self.assertEqual(user, 'admin')