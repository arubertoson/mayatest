"""
Module to help locate maya installation aswell as setup clean working
environments
"""
import os
import platform
import glob
import shutil
import tempfile
import uuid
from contextlib import contextmanager


def create_and_return(*args):
    dir_ = os.path.join(*args)
    if not os.path.exists(dir_):
        os.makedirs(dir_)
    return dir_


@contextmanager
def temp_app_dir():
    """Contextmanager to create and remove a temporary app dir to perform
    our tests from.
    """
    maya_app_dir = os.environ.setdefault('MAYA_APP_DIR', '')
    try:
        tmp_app_dir = create_and_return(
            tempfile.gettempdir(), 'maya_app_dir{0}'.format(str(uuid.uuid4())))
        os.environ['MAYA_APP_DIR'] = tmp_app_dir
        yield tmp_app_dir
    finally:
        shutil.rmtree(tmp_app_dir)
        os.environ['MAYA_APP_DIR'] = maya_app_dir


@contextmanager
def clean_maya_environment():
    """Contextmanager to reset necessary environment values for a clean
    run, then restore overwritten values.
    """
    with temp_app_dir():
        script_path = os.environ.get('MAYA_SCRIPT_PATH', '')
        module_path = os.environ.get('MAYA_MODULE_PATH', '')
        try:
            os.environ['MAYA_SCRIPT_PATH'] = ''
            os.environ['MAYA_MODULE_PATH'] = get_module_path()
            yield
        finally:
            os.environ['MAYA_SCRIPT_PATH'] = script_path
            os.environ['MAYA_MODULE_PATH'] = module_path


def get_module_path():
    return os.getcwd() if is_maya_module() else ''


def is_maya_module():
    return glob.glob(os.getcwd() + '/*.mod')


def get_maya_location(version):
    """Find the location of maya installation

    If MAYA_LOCATION is present in system and/or user variables mayatest
    will use whatever is stored there.
    """
    if 'MAYA_LOCATION' in os.environ:
        return os.environ['MAYA_LOCATION']

    try:
        # These paths are hardcoded after normal conventions
        location = {
            'Windows': 'C:/Program Files/Autodesk/Maya{0}',
            'Darwin': '/Applications/Autodesk/maya{0}/Maya.app/Contents',
        }[platform.system()]
    except KeyError:
        location = '/usr/autodesk/maya{0}'
        if version < 2016:
            # Starting Maya 2016, the default install directory name changed.
            location += '-x64'
    return location.format(version)


def mayapy(version):
    """Find the mayapy executable path."""
    mayapy_executable = '{0}/bin/mayapy'.format(get_maya_location(version))
    if platform.system() == 'Windows':
        mayapy_executable += '.exe'
    return mayapy_executable
