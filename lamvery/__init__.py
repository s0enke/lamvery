"""
lamvery
----
Function based deploy and management tool for AWS Lambda.
"""

__version__ = '0.12.0'

import importlib

secret = importlib.import_module('lamvery.secret')
