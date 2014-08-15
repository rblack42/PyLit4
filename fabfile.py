from fabric.api import *

def install():
    local('virtualenv _venv')
    local('source _venv/bin/activate ; pip install -r requirements.txt')

def test():
    local('nosetests')

def push(message):
    local('git add .')
    local('git commit -m "%s"' % message)
    local('git push origin master')
