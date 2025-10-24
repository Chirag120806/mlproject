from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    return requirements

setup(
name='mlproject',
version='0.0.1',
author= 'Chirag',
author_email='chiragthareja234@gmail.com',
pakcages=find_packages(),
install_requires= get_requirements('requirements.txt')

)