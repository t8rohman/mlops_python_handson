from setuptools import setup, find_packages

'''
program to set up and install the package in your local folder.
'''

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='outliers',
      version='0.1',
      description='An exercise to make a package by wrapping up outliers detection functionality.',
      author='xxx',
      license='MIT',
      packages=find_packages(),           # pass this as find_packages() to automatically look for submodules
      install_requires=requirements,      # install all the requirements
      zip_safe=False
      )