import click

from models import User

@click.command()
def auth():
    """Sign up the user"""
    email = click.prompt('Enter your user name')
    password = click.prompt('Enter your password')
    user = User(email, password)
    user.save()

if __name__ == '__main__':
    auth()