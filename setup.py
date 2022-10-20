from pickle import LIST
from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    """
    this function will return list of requirements
    """
    requirement_list:List[str]=[]
    return requirement_list

setup(
    name='sensor',
    version='0.0.0.1',
    author='Kirthna',
    author_email='kirthnak7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement(),
)
