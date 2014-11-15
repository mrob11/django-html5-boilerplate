# fabric file for this project.
from fabric.api import lcd, local

# Runs tests and commits changes.
def prepare_deployment(branch_name):
    local('python manage.py test django_project')
    local('git add -p && git commit') # or local('hg add && hg commit')

# This will pull your changes from the development master branch,
# run any migrations you've made, run your tests, and restart your web server.
def deploy():
    with lcd('/path/to/my/prod/area/'):

        # With git...
        local('git pull /my/path/to/dev/area/')

        # With Mercurial...
        # local('hg pull /my/path/to/dev/area/')
        # local('hg update')

        # With both
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')
