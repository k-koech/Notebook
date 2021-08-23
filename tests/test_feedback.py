import unittest
from app.models import Feedback,User

class FeedbackTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Feedback class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_kelvin = User(username = 'James',password_secure = 'potato', email = 'james@ms.com')
        self.new_feedback = Feedback(id = 1,feedback='The site is working well bravo', user_id = self.user_kelvin,date_posted='2021-08-20 14:58:31.689649')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_feedback,Feedback))


