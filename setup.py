from setuptools import setup, find_packages
from os import path
import sys
import re
from MyScript import const

setup(name=const.NAME,
      version=const.__version__,
      description='a Python script based on Py-Cli-Framework',
      author='Your Name',
      author_email='your.email@example.com',
      license='SEE LICENSE IN LICENSE',
      packages=[const.NAME],
      include_package_data=True,
      setup_requires=['pytest-runner >=2.1'],
      tests_require=['pytest >=2.7.3'],
      test_suite='tests',
      entry_points={
        'console_scripts': [
            '{} = {}.myscript:main'.format(const.COMMAND_NAME.lower(), const.NAME)
        ]
      })
