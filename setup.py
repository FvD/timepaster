# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '0.5.1'

setup(name='timepaster',
      version=version,
      description="Console time calculator that copies the result to the system clipboard",
      long_description="""\
        A console based time calculator that will take a begin and end time as
        arguments and calculate the time difference in decimals and place the
        result in your clipboard.
        
        This is primarily (if not only) useful to fill in time sheets, as you
        can quickly calculate a difference and then paste the result.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Time Calculator, Time Paster',
      author='Frans van Dunné',
      author_email='fvd@southshield.net',
      url='www.innovateonline.nl',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'pyperclip==1.5.11'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      timepaster = timepaster.timepaster:main
      """,
      )
