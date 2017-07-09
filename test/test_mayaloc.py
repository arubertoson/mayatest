"""
"""
import os
import platform

from mayatest import mayaloc


def test_create_and_return_dir_with_temp_app_dir():
    maya_app_dir = os.environ['MAYA_APP_DIR']
    with mayaloc.temp_app_dir() as app_dir:
        local_appdir = app_dir
        assert os.path.exists(app_dir)
        assert os.environ['MAYA_APP_DIR'] == app_dir
    assert os.path.exists(local_appdir) is False
    assert os.environ['MAYA_APP_DIR'] == maya_app_dir


def test_system_return_maya_location():
    test_version = 2016
    location = mayaloc.get_maya_location(test_version)

    system = platform.system()
    if system == 'Windows':
        assert location == 'C:/Program Files/Autodesk/Maya{0}'.format(
            test_version)
    elif system == 'Darwin':
        assert location == ('/Applications/Autodesk/maya{0}/Maya.app/Contents'
                            .format(test_version))
    else:
        unixpath = '/usr/autodesk/maya{0}'.format(test_version)
        if test_version < 2016:
            # Starting Maya 2016, the default install directory name changed.
            unixpath += '-x64'
        assert location == unixpath


def test_system_mayapy_executable_location():
    test_version = 2017
    mayapy_executable = mayaloc.mayapy(test_version)
    if platform.system() == 'Windows':
        assert mayapy_executable.endswith('/bin/mayapy.exe')
    else:
        assert mayapy_executable.endswith('/bin/mayapy')
