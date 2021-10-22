class Credential:
    """
    Class that generates new instances of Credentials.
    """
    credentials_list=[] #list of credentials
    
    def __init__(self,account,username,email,password):
        self.account= account
        self.username = username
        self.email= email
        self.password = password
        
    def save_credential(self):
        '''
         method saves credential objects into credential_list
        '''
        Credential.credentials_list.append(self)
        
    
    def find_by_account(cls,account):
        '''
        Method that takes in account name and returns credentials that match that account.

        Args:
            account: Account whose credentials to search for
        Returns :
            Credentials that match the account.
        '''
        for credential in cls.credentials_list:
            if credential.account ==account:
                return credential
    
    def credential_exist(cls,account):
        '''
        Method that checks if a crediantial exists from the credential list.
        
        Args:
            account: Account whose credentials to search for
        Returns :
            Boolean: True or false
        '''
        
        for credential in cls.credentials_list:
            if credential.account ==account:
                return True
            
        return False
    
  
                
    