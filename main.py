import click
import psycopg2

from models import User, Comments

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
        if password != row[2]:
            click.echo('wrong password')
        else:
            click.echo('signup successfully')
            comment = click.prompt('make comment: ')
            comnt = Comments(comment)
            comnt.add_comment()
            click.echo('Your previous comments')
            curs = conn.cursor()
            query = 'SELECT * FROM cli_coment'
            curs.execute(query)
            row = curs.fetchall()
            com_id = 0
            for u in row:
                com_id =com_id+1
                click.echo('{}st {}'.format(com_id,u[1]))
    else:
        click.echo('Please register')


auth.add_command(register)
auth.add_command(login)

if __name__ == '__main__':
    auth()