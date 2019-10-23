from invoke import task


@task
def run(c):
    c.run("python manage.py runserver", pty=True)


@task
def test(c):
    c.run("coverage run --source='app' manage.py test", pty=True)
    c.run("coverage report")
