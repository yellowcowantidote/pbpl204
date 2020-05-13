import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="maxp_emp",

    description="A paper focused on identifying regional employment centers s using the max-p regions algorithm",

    author="Center for Geospatial Sciences",

    packages=find_packages(exclude=['data', 'figures', 'output', 'notebooks']),

    long_description=read('README.md'),
)
