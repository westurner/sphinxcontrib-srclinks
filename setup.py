# -*- coding: utf-8 -*-

# sphinxcontrib-srclinks/setup.py

import os
from setuptools import setup, find_packages

def here(path_):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path_)

with open(here('README.rst')) as f:
    README = f.read()

with open(here('CHANGELOG.rst')) as f:
    CHANGELOG = f.read()

long_desc = README + '\n\n' + CHANGELOG


requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-srclinks',
    version='0.2.4',
    url='http://bitbucket.org/westurner/sphinxcontrib-srclinks',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-srclinks',
    license='BSD (3-clause)',
    author='Wes Turner',
    author_email='wes@wrd.nu',
    description='Add source, edit, history, annotate links to GitHub or BitBucket',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
