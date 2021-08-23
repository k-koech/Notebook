import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username='triplek',email='triplek901@gmail.com', password_secure = 'banana')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

