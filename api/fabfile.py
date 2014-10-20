import os.path
from fabric.api import (env, execute, lcd, local, parallel,
                        run, roles, task)

ROOT = os.path.dirname(os.path.realpath(__file__))
VIRTUALENV = os.path.join(ROOT, 'venv')


@task
def create_virtualenv(venv=VIRTUALENV,
                      requirements='requirements.txt', wipe=True):
    if wipe:
        local('rm -rf %s' % venv)

    local('virtualenv --python=python --distribute '
          '--never-download %s' % venv)

    local('%s/bin/pip install --exists-action=w '
          '--download-cache=/tmp/pip-cache '
          '-r %s' % (venv, requirements))

    local('%s/bin/pip install --exists-action=w '
          '--download-cache=/tmp/pip-cache '
          'virtualenv' % venv)
