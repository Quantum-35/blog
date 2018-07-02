import click
import psycopg2

from models import User

@click.group()
def auth():
    pass

@click.command()
def register():
    """Sign up the user"""
    email = click.prompt('Enter your user name')
    password = click.prompt('Enter your password')
    user = User(email, password)
    user.register_user()
    click.echo('Registerd as {} password {}'.format(email, password))

@click.command()
def login():
    """Logins in registerd user"""
    email = click.prompt('Enter your user name')
    password = click.prompt('Enter your password')
    conn  = psycopg2.connect(host="localhost",database="andela", user="postgres", password="leah")
    curs = conn.cursor()
    query = 'SELECT * FROM cli WHERE email=%s'
    curs.execute(query, (email,))
    row = curs.fetchone()
    if row:
        pass
    else:
        click.echo('Please register')


auth.add_command(register)
auth.add_command(login)

if __name__ == '__main__':
    auth()