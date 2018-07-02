
class User:
    dbuser_details=[]
    def __init__(self, email, password, role='user'):
        self.email = email
        self.password = password
        self.role = role

    def save(self):
        user_details = {}
        user_details['email'] = self.email
        user_details['password'] = self.password
        user_details['role'] = self.role
        User.dbuser_details.append(user_details)
        print(User.dbuser_details)

class Moderator(User):
    def __init__(self, email, password, role='moderator'):
        super().__init__(email, password)
        self.role = role

class Admin(User):
    def __init__(self,email, password, role='admin'):
        super().__init__(email, password)
        self.role = role

class Comments:

    def __init__(self, message, role):
        self.message = message
        self.role = role
