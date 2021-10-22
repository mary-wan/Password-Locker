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
        
    
  