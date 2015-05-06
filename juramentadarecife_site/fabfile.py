__author__ = 'anderson'

from fabric.api import run, sudo, cd, env

env.user = 'root'
env.hosts = ['104.236.205.124']


def git_pull():
    sudo('su - django')
    with cd('juramentadarecife/'):
        result = run('git pull origin master')
        print(result)
    disconnect_all()

