
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

class Comment():
    """Creates a user comment."""

    def __init__(self, comment, author):
        self.connection = psycopg2.connect(
                host="localhost", database="andela", user="postgres", password="leah")
        self.comment = comment
        self.author = author

    def create_comment(self):

        cursor = self.connection.cursor()
        query = "INSERT INTO comments (comments, email) \
                VALUES ('{}', '{}')".format(self.comment, self.author)
        cursor.execute(query)
        self.connection.commit()
        self.connection.close()

    def create_reply(self, parent_id):
        cursor =self.connection.cursor()
        try:
            query = "INSERT INTO reply (comment, username, parent) \
                     VALUES ('{}', '{}', '{}')".\
                            format(self.comment, self.author, parent_id)
            cursor.execute(query)
            self.connection.commit()
            self.connection.close()
        except Exception as e:
            return "Error: {}".format(e)
