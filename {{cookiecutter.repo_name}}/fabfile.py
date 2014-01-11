from fabric.api import local, env
from fabric.contrib.project import rsync_project

env.hosts = []
env.user = ''

env.build_dir = 'build/'

# =============================================================================
#  ENV
# ==========================================================================
# def production():
#     '''Setting overides for production environment.'''
#     env.hosts = ['fueled.com']
#     env.user = 'ubuntu'
#     env.remote_deploy_dir = '/opt/webapps/fueled.com/'


# =============================================================================
#  TASKS
# ==========================================================================

def setup():
    '''Setup local development environment using middleman. http://middlemanapp.com/'''
    local('sudo gem install middleman')
    local('sudo bundle install')


def serve():
    '''Run local development server.'''
    local('bundle exec middleman')


def build():
    local('bundle exec middleman build --clean --verbose')


def deploy():
    # local('rm -rf %(build_dir)s' % env)
    build()
    local('git push')

    rsync_project(remote_dir=env.remote_deploy_dir,
                  local_dir=env.build_dir)
