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
        
    def test_save_credential(self):
        '''
        test case to test if the credential is saved into the credential list
        '''
        
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)
        
    def test_save_multiple(self):
        '''
        test to check if  multiple credentials objects to to the contact_list
        '''
        
        self.new_credential.save_credential()
        credential_two =Credential("ig","kiki","kiki@gmail.com","uiop5")
        credential_two.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
        
    def test_find_by_account(self):
        '''
        test to check if we can find a credential by account name and display information
        '''
        self.new_credential.save_credential()
        credential_two = Credential("ig","kiki","kiki@gmail.com","uiop5")
        credential_two.save_credential()
        
        credential_found = Credential.find_by_account("ig")
        self.assertEqual(credential_found.username, credential_two.username)
    
    
    def test_find_by_account(self):
        '''
        test to check if we can find a credential by account name 
        '''
        self.new_credential.save_credential()
        credential_two = Credential("ig","kiki","kiki@gmail.com","uiop5")
        credential_two.save_credential()
        
        credential_exits = Credential.credential_exist("twitter")
        self.assertTrue(credential_exits)
        
    def test_display_credentials(self):
        '''
        test to check that returns a list of all contacts saved is displayed
        '''
        
        self.assertEqual(Credential.display_credential(),Credential.credentials_list)
        
  