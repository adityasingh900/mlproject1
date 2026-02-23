from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirnments(file_path:str)->list[str]:
    ''' this function will return the list of requirnments 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup (
name = 'mlprojects',
version = '0.0.1',
author = 'aditya',
author_email = 'aadityasinghrajawat357@gmail.com',
packages =find_packages(),
install_requires = get_requirnments('requirements.txt')
)