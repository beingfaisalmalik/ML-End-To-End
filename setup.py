from setuptools import find_packages,setup
from typing import List
HYPER_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''Returns a list of requirements'''
    requirements = []
    with open(file_path) as fileobj:
       requirements = fileobj.readlines()
       requirements=[req.replace('\n','') for req in requirements]
       if HYPER_E_DOT in requirements:
           requirements.remove(HYPER_E_DOT)
    return requirements
       
setup(
    name='python_project',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt'),
    author='Faisal',
)