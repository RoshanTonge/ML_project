from setuptools import find_packages,setup
from typing import List

HYPEN_e_DOT='-e .'
def get_requierments(file_path:str)->List[str]:
    '''
    this function will return the list of requierments
    '''
    requierments=[]
    with open(file_path) as file_obj:
        requierments=file_obj.readlines()
        requierments=[req.replace('\n','') for req in requierments]
        
        if HYPEN_e_DOT in requierments:
            requierments.remove(HYPEN_e_DOT)
    return requierments
    
setup(
    name="mlproject",
    version='0.0.1',
    author='roshan',
    author_email='tongeroshan95@gmail.com',
    packages=find_packages(),
    install_requires=get_requierments('requierments.txt')
)