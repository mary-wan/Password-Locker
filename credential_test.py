import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
     Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        method to run before each test case.
        '''
        self.new_credential = Credential("twitter","Maria", "maria@gmail.com","1234h")
        
    def tearDown(self):
        '''
        method to run after each test case.
        '''
        Credential.credentials_list=[]
        
    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.username,"Maria")
        self.assertEqual(self.new_credential.email,"maria@gmail.com")
        self.assertEqual(self.new_credential.password,"1234h")
        
  