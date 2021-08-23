import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(category='Product pitch',pitch='You go but my life is You',date_posted='2021-08-20 14:58:31.689649',upvotes=0,downvotes=0,user_id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


