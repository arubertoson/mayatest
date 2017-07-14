"""
Tests for mayatest.mayaloc

pytest
"""
import os
import tempfile
import platform

from mayatest import mayaloc


def test_create_and_return():
    import uuid
    import tempfile
    test_dir = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
    assert not os.path.exists(test_dir)
    created_dir = mayaloc.create_and_return(test_dir)
    assert os.path.exists(created_dir)


def test_temp_app_dir():
    maya_app_dir = os.environ.setdefault('MAYA_APP_DIR', 'test_app_dir')
    with mayaloc.temp_app_dir() as tmp_dir:
        tmp_app_dir = tmp_dir
        assert os.path.exists(os.environ['MAYA_APP_DIR'])
    assert os.environ['MAYA_APP_DIR'] == maya_app_dir
    assert not os.path.exists(tmp_app_dir)


def test_clean_maya_environment():
    script_path = os.environ.setdefault('MAYA_SCRIPT_PATH', 'test_script')
    module_path = os.environ.setdefault('MAYA_MODULE_PATH', 'test_module')
    with mayaloc.clean_maya_environment():
        assert os.environ['MAYA_SCRIPT_PATH'] == ''
        assert os.environ['MAYA_MODULE_PATH'] == ''
    assert os.environ['MAYA_SCRIPT_PATH'] == script_path
    assert os.environ['MAYA_MODULE_PATH'] == module_path


def test_get_maya_location():
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


def test_mayapy():
    test_version = 2017
    mayapy_executable = mayaloc.mayapy(test_version)
    if platform.system() == 'Windows':
        assert mayapy_executable.endswith('/bin/mayapy.exe')
    else:
        assert mayapy_executable.endswith('/bin/mayapy')


def test_is_maya_module_modfile():
    assert not mayaloc.is_maya_module()
    with tempfile.NamedTemporaryFile(suffix='.mod', dir='./'):
        assert mayaloc.is_maya_module()

