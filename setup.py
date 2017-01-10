#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'slack_logging_handler',
    'author': 'Dan Cohen',
    'url': 'www.github.com/danie1cohen/slack_logging_handler',
    'download_url': 'https://github.com/danie1cohen/slack_logging_handler/tarball/0.1.10',
    'author_email': 'daniel.o.cohen@gmail.com',
    'version': '0.1.10',
    'install_requires': [],
    'packages': ['slack_logging_handler'],
    'scripts': [],
    'name': 'slack_logging_handler'
}

setup(**config)
