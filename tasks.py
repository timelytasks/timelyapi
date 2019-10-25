from invoke import task


@task
def b(c):
    """ Black formatting """
    c.run("black app/")


@task
def run(c):
    """ Run API """
    c.run("python manage.py runserver", pty=True)


@task
def t(c):
    test(c)
    c.run("coverage html")


@task
def test(c):
    """ Run test suite """
    c.run("flake8 tasks.py")
    c.run("flake8 app/")
    c.run("coverage run --source='app' manage.py test", pty=True)
    c.run("coverage report")


@task
def mm(c):
    """ Make migrations and migrate """
    c.run("python manage.py makemigrations", pty=True)
    c.run("python manage.py migrate", pty=True)


@task
def sh(c):
    """ Shell command """
    # shell_plus
    c.run("python manage.py shell", pty=True)


@task
def h(c):
    """ Opens coverage home page """
    c.run("python -m webbrowser -t \"htmlcov/index.html\"")
