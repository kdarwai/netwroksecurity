'''
This is the setup file used to distribute the pyhton project

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will retrun list of requirement
    
    """
    req_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                req=line.strip()
                if req and req!='-e .':
                    req_list.append(req)
    except FileNotFoundError:
        print("Req file not found")
    
    return req_list

setup(
    name="Networksecurity",
    version="0.0.0.1",
    author="Kirtiraj",
    packages=find_packages(),
    install_requires=get_requirements()
    )
