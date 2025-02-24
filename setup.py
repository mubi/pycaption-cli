#!/usr/bin/env python
import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.md')

dependencies = [
  'pycaption>=1.2.0'
]

setup(
  name='pycaption-cli',
  version='0.3.2',
  description='Command line caption conversion',
  author='Joe Norton',
  author_email='joey@nortoncrew.com',
  url='https://github.com/jnorton001/pycaption-cli',
  install_requires=dependencies,
  dependency_links=[
    'https://github.com/mubi/pycaption/tarball/master#egg=pycaption-1.2.0'
  ],
  packages=find_packages(),
  include_package_data=True,
  entry_points=dict(
    console_scripts=['pycaption=pycapcli.caption_converter:main']
  ),
)
