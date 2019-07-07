import unittest
from app.models import User



class TestUser(unittest.TestCase):

    def setUp(self):
        self.user_fev= User(username="fev",password="123",email="fev@gmail.com",id=1)

    def tearDown(self):
        User.query.delete()

        def test_check_instance_variables(self):
            self.assertEquals(self.new_fev.id, 1)
            self.assertEquals(self.new_fev.username,'fev')
            self.assertEquals(self.new_fev.bio, '')
            self.assertEquals(self.new_fev.email, 'fev@gmail.com')
            self.assertEquals(self.new_fev.profile_pic_path, '')

       


    def test_password_setter(self):
        self.assertTrue(self.user.password_hash is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.user.password

    def test_password_verification(self):
            self.assertTrue(self.user.verify_password('123'))

if __name__ == "__main__":
    unittest.main()
