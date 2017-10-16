from os import path
from codecs import open
from setuptools import setup, find_packages

VERSION = "0.0.0"

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()


with open(path.join(here, "requirements.txt")) as requirements_file:
    requirements = requirements_file.readlines()


setup(
    name='ProjectManager',
    version=VERSION,
    description="Tools for 3DS Max",
    author="Anthony Mondelin",
    author_email="anthonymondelin@hotmail.fr",
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    include_package_data = True
)
