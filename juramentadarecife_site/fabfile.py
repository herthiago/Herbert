__author__ = 'anderson'

from fabric.api import run

env.user = 'root'
env.hosts = ['104.236.205.124']


def git_pull():
    run('sudo su - django')
    run('cd juramentadarecife/')
    result = run('git pull origin master')
    print(result)
