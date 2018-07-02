
import psycopg2
class User:
    def __init__(self, email, password, role='user'):
        self.email = email
        self.password = password
        self.role = role
        self.conn  = psycopg2.connect(host="localhost",database="andela", user="postgres", password="leah")

    def register_user(self):
        curs = self.conn.cursor()
        query = 'INSERT INTO cli(email,password, role) VALUES(%s, %s, %s)'
        curs.execute(query, (self.email, self.password, self.role))
        self.conn.commit()
        self.conn.close()

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
