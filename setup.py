import setuptools
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "chicken_disease_mlops"
AUTHOR_USER_NAME = "adi3011"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "19bcs1084@gmail.com"

HYPEN_E  = "-e ."

def get_requirements(filePath:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(filePath)  as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
            
    return requirements

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires= get_requirements('requirements.txt')
)