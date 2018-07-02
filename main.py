import click

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
    user.save()
    click.echo('Registerd as {} password {}'.format(email, password))

@click.command()
def login():
    """Logins in registerd user"""
    # email = click.prompt('Enter your user name')
    # password = click.prompt('Enter your password')
    # check_email = User.get_by_email(email=email)
    print(User.dbuser_details)


auth.add_command(register)
auth.add_command(login)

if __name__ == '__main__':
    auth()