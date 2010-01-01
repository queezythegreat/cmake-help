from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='CMakeHelp',
      version=version,
      description="CMake Interactive Help System",
      long_description=open('doc/README').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='cmake interactive help system command line',
      author='Tomasz Bogdal',
      author_email='vladsmailtotomas@gmail.com',
      url='http://www.qtzlabs.com/',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts' : [
              'cmake-help = cmakehelp.cmakehelp:main'
          ]
      },
      )
