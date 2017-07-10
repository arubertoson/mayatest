"""
"""
import os
import sys
import argparse
import subprocess

import pytest
from mayatest import mayaloc


def args_parser(args):
    parser = argparse.ArgumentParser(
        description='Runs unit tests for a Maya module')
    parser.add_argument(
        '-m', '--maya', help='Maya version', type=int, default=2016)
    parser.add_argument(
        '-py', '--pytest', help='pytest extra args', type=str)
    return parser.parse_args(args)


def construct_command(pargs):
    mayapy = mayaloc.mayapy(pargs.maya)
    if not os.path.isfile(mayapy):
        raise RuntimeError(
            'Maya {0} is not installed on the system'.format(pargs.maya))

    cmd = [mayapy, os.path.normpath(os.path.realpath(pytest.__file__))]
    if pargs.pytest:
        cmd.append(pargs.pytest)
    return cmd


def main():
    pargs = args_parser(sys.argv[1:])
    with mayaloc.clean_maya_environment():
        try:
            subprocess.check_call(construct_command(pargs))
        except subprocess.CalledProcessError:
            pass


if __name__ == '__main__':
    main()
