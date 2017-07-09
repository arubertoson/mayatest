#! /usr/bin/env python

import os
import sys
from setuptools import setup

if sys.version_info[:2] < (2, 7):
    sys.exit('mayalauncher requires Python 2.7 or higher.')

here = os.path.abspath(os.path.dirname(__file__))

# Get long description
try:
    with open(os.path.join(here, 'README.md'), 'r') as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name='mayatest',
    version='0.1.0',
    description='Test Autodesk Maya scripts and modules with pytest',
    long_description=long_description,
    author='Marcus Albertsson',
    author_email='marcus.arubertoson@gmail.com',
    url='https://github.com/arubertoson/mayatest',
    license='MIT',
    py_modules=['mayatest'],
    install_requires=['pytest'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['mayatest = mayatest.cli:main']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
    ],
)
