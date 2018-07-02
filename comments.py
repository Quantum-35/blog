"""Implements a comment."""
import psycopg2

class Comment(object):
    """Creates a user comment."""

    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost", database="andela", user="postgres", password="leah")

    def create_comment(self, comment, author):

        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO comments (comment, username) \
                    VALUES ('{}', '{}')".format(comment, author)
            cursor.execute(query)
            self.connection.commit()
            self.connection.close()
        except Exception as e:
            return "Error: {}".format(e)

    def create_reply(self, comment, author, parent_id):
        cursor =self.connection.cursor()
        try:
            query = "INSERT INTO reply (comment, username, parent) \
                     VALUES ('{}', '{}', '{}')".\
                            format(comment, author, parent_id)
            cursor.execute(query)
            self.connection.commit()
            self.connection.close()
        except Exception as e:
            return "Error: {}".format(e)


if __name__ = '__main__':
    comment = 