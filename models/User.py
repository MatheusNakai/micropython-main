

class User(object):

    def __init__(self, id: int, password: int):
        self.id = id
        self.password = password
        self.admin = 1
    
    def change_password(self, new_password):
        self.password = new_password
        
        print("senha trocada com sucesso")

        return True
    
    def change_role(self):
        if self.admin:
            self.admin = 0
        else:
            self.admin = 1
        
        return True

    