from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(filepath:str)->List[str]:
    
    requirement=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    return requirement
setup(
    name='mlprject',
    packages=find_packages(),
    version='0.0.1',
    author_email='nipungahane@gmail.com',
    author='Nipun Gahane',
    install_requires=get_requirements('requirements.txt'),
)