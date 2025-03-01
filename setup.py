'''
Setup.py used for the entity package
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    Get the requirements from the requirements.txt file
    '''
    requirement_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore comments, empty lines, and -e requirements
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt not found')
        return []
    
    return requirement_list

setup(
    name='NetworkSecurity',
    version='0.1.0',
    description='Entity package',
    author='Salman',
    packages=find_packages(),
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'entity=entity.__main__:main'
        ]
    },
)