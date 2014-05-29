#!/usr/bin/env python

"""
 PRONET - Network App Starter Kit
 Author - Hardik Shah
 Date   - May 2014
"""

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "pronet-da-starter",
    version = "0.1",
    packages = find_packages(),
    #scripts = ['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['flask', 'flask-rest' , 'requests', ],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Hardik Shah",
    author_email = "hardik.s@prodapt.com",
    description = "This is a starter Kit for Pronet Device App",
    license = "AGPL-3",
    keywords = "Pronet Device Application",

    # could also include long_description, download_url, classifiers, etc.
)
