class User:
    """
    Class that generates new instances of users.
    """
    
    user_list=[]
    
    def __init__(self, username,password):
        self.username =username
        self.password =  password
        
    def user_save(self):
        '''
        method to login user
        '''
        User.user_list.append(self)
    
    @classmethod
    def user_verification(cls,username,password):
        for user in User.user_list:
            if(user.username == username and user.password == password):
              return username
       
        