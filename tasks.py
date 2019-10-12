from invoke import task, run
from subprocess import call


@task
def build(c):
    call("docker-compose down", shell=True)
    call("docker-compose build", shell=True)
    call("docker-compose run server python3 manage.py db_setup", shell=True)
    call("docker-compose up -d", shell=True)


