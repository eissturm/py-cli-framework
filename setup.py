from setuptools import setup, find_packages
from os import path
import sys
import re
from src import const

requires = [

]

setup(name=const.NAME,
      version=const.__version__,
      description='a Python script based on Py-Cli-Framework',
      author='Your Name',
      author_email='your.email@example.com',
      license='SEE LICENSE IN LICENSE',
      packages=find_packages(exclude=['tests', 'tests.*']),
      setup_requires=['pytest-runner >=2.1'],
      tests_require=['pytest >=2.7.3'],
      test_suite='tests',
      entry_points={
        'console_scripts': [
            '{} = scriptname.myscript:main'.format(const.NAME)
        ]
      },
      install_requires=requires)
