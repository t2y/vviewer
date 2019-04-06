import os
import re
import sys

from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

metadata_py = open('vviewer/main.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", metadata_py))

setup(
    name='vviewer',
    version=metadata['version'],
    description='viewer for text data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Environment :: Console',
        'Topic :: Utilities',
    ],
    keywords=['vertical', 'viewer', 'csv'],
    url='https://github.com/t2y/vviewer',
    license='Apache License 2.0',
    author='Tetsuya Morimoto',
    author_email='tetsuya.morimoto@gmail.com ',
    zip_safe=False,
    platforms=['unix', 'linux', 'osx', 'windows'],
    packages=['vviewer'],
    include_package_data=True,
    install_requires=[],
    tests_require=[
        'tox', 'pytest', 'pytest-pep8', 'pytest-flakes',
    ],
    entry_points = {
        'console_scripts': [
            'vviewer=vviewer.main:main',
        ],
    },
)
