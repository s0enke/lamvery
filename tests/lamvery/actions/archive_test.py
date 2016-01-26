# -*- coding: utf-8 -*-

import os
from unittest import TestCase
from nose.tools import ok_, eq_, raises
from mock import Mock,MagicMock,patch

from lamvery.actions.archive import ArchiveAction

def default_args():
    args = Mock()
    args.conf_file = '.lamvery.yml'
    args.dry_run = True
    args.no_libs = False
    return args

class ArchiveActionTestCase(TestCase):

    def tearDown(self):
        if os.path.exists('test.zip'):
            os.remove('test.zip')

    def test_action(self):
        action = ArchiveAction(default_args())
        action._config = Mock()
        action._config.get_archive_name = Mock(return_value='test.zip')
        action._config.generate_lambda_secret = Mock(return_value={})
        action._config.get_exclude = Mock(return_value=[])
        action.action()
        ok_(os.path.exists('test.zip'))
