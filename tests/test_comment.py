from app.models import User,Comments
from app import db
import unittest

class UserModelTest(unittest.TestCase):
        def setUp(self):
                self.user_kelvin = User(username = 'James',password_secure = 'potato', email = 'james@ms.com')
                self.new_comment = Comments(id=12345,pitch_id='1',comment='Its lit',user_id = self.user_kelvin, date_posted='2021-08-20 14:58:31.689649')
        
        def test_instance(self):
               self.assertTrue(isinstance(self.new_comment,Comments))