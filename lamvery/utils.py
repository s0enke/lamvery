# -*- coding: utf-8 -*-

import os
import re
import shlex
import subprocess

from lamvery.log import get_logger

ENV_PATTERN = re.compile('^(?P<name>[^\s]+)\s*=\s*(?P<value>.+)$')


def previous_alias(alias):
    return '{}-pre'.format(alias)


def parse_env_args(env):
    if not isinstance(env, list):
        return None

    ret = {}
    for e in env:
        matches = ENV_PATTERN.match(e)

        if matches is None:
            raise Exception(
                'The format of "env" option must be "NAME=VALUE": {}'.format(e))

        name = matches.group('name')
        value = matches.group('value')
        k, v = shlex.split('{} {}'.format(name, value))
        ret[k] = v

    return ret

def run_commands(commands, working_dir=os.getcwd()):
    cwd = os.getcwd()
    os.chdir(working_dir)

    for c in commands:
        try:
            subprocess.check_output(
                c, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            os.chdir(cwd)
            raise Exception(e.output)

    os.chdir(cwd)
