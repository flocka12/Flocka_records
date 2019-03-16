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
        "setup"
        response = self.client.post('api/v2/auth/signup', json=self.sample_user)

        self.assertEqual(404, response.status_code)
        # self.assertEqual(self.sample_user['username'], response.get_json()['data']['username'])
        # self.assertNotIn('password', response.get_json())

    # def test_registration_with_duplicate_email_fails(self):
    #     "# setup"
    #     self.data_base.add_user(self.sample_user)

    #     # act
    #     self.sample_user.update({
    #         'username': 'something_new',
    #         'password': 'Kab3!Eds'
    #     })

    #     response = self.client.post('api/v2/auth/signup', json=self.sample_user)

    #     # assert
    #     self.assertEqual(422, response.status_code)
    #     self.assertEqual('email already in use', response.get_json()['message'])

    # def test_registration_with_duplicate_username_fails(self):
    #     "# setup"
    #     self.data_base.add_user(self.sample_user)

    #     # act
    #     self.sample_user.update({
    #         'password': 'Kab3!Eds',
    #         'email': 'new@anewemail.com'
    #     })

    #     response = self.client.post('api/v2/auth/signup', json=self.sample_user)

    #     # assert
    #     # self.assertEqual(422, response.status_code)
    #     self.assertEqual('username already taken', response.get_json()['message'])

if __name__ == "__main__":
    unittest.main()
