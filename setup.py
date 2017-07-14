#! /usr/bin/env python

import os
import sys
from setuptools import setup

if sys.version_info[:2] < (2, 7):
    sys.exit('mayalauncher requires Python 2.7 or higher.')

here = os.path.abspath(os.path.dirname(__file__))

# Get long description
try:
    import pypandoc
    pypandoc.convert_file('README.md', 'rst', outputfile='README.rst')
    with open('README.rst') as rst:
        description = rst.read()
    os.remove('README.rst')
except (IOError, ImportError):
    with open(os.path.join(here, 'README.md'), 'r') as f:
        description = f.read()

setup(
    name='mayatest',
    version='0.1.2',
    description='Test Autodesk Maya scripts and modules with pytest',
    long_description=description,
    author='Marcus Albertsson',
    author_email='marcus.arubertoson@gmail.com',
    url='https://github.com/arubertoson/mayatest',
    license='MIT',
    packages=['mayatest'],
    install_requires=['pytest', 'mock'],
    include_package_data=True,
    zip_safe=False,
    entry_points={'console_scripts': ['mayatest = mayatest.cli:main']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
    ])
