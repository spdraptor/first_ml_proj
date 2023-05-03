from setuptools import find_packages,setup
from typing import List
def getRequired(path:str)->List[str]:
    
    '''
    method to read txt file and return list of package names 
    '''
    reqirements=[]
    hypen_e_dot = '-e .'
    with open(path) as file:
        reqirements = file.read().split("\n")
        if hypen_e_dot in reqirements:
            reqirements.remove(hypen_e_dot)
    return reqirements  



setup(
    name= 'First ML project',
    version='0.0.1',
    author='SPDraptor',
    author_email='spdraptor.micro@outlook.com',
    packages=find_packages(),
    install_requires = getRequired("requirements.txt")
)