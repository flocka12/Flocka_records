''' module for testing the user model '''
import unittest
from app import create_app
from app.api.v1.models.user_model import User
from manage import migrate, truncate


class UserTest(unittest.TestCase):
    ''' test '''
    def setUp(self):
        app = create_app('testing')
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()
        self.data_base = User()
        migrate()
        self.sample_user = dict(
            firstname="test_first",
            lastname="test_last",
            email="tester@example.com",
            username="tester_user",
            password="12345abcsde"
        )

    def tearDown(self):
        truncate()

    def test_it_registers_user(self):
        # act 
        response = self.client.post('api/v1/auth/signup', json=self.sample_user)

        # assert 
        self.assertEqual(201, response.status_code)
        self.assertEqual(self.sample_user['username'], response.get_json()['data']['username'])
        self.assertEqual(self.sample_user['email'], response.get_json()['data']['email'])
        self.assertNotIn('password', response.get_json()['data'])

    def test_it_logs_in_user(self):
        # setup
        self.data_base.add_user(self.sample_user)
        
        # act 
        response = self.client.post('api/v1/auth/login', json=self.sample_user)

        # assert 
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Successfully logged in')
        self.assertIn('access_token', data)
        self.assertIn('refresh_token', data)

if __name__ == "__main__":
    unittest.main()
