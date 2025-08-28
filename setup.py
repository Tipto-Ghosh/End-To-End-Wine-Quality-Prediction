from setuptools import setup , find_packages 
from typing import List


# read the README.md file
with open("README.md" , "r" , encoding = "utf-8") as f:
    long_description = f.read()
    

HYPER_E_DOT = "-e ."

# read the requirements.txt file
def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    requirements = []
    
    with open(file_path) as file:
        requirements = file.readlines()
        # remove the \n
        requirements = [req.replace("\n" , "") for req in requirements]
        
        # also remove the -e .
        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)
    
    return requirements

description = (
    "The Wine Quality Prediction project focuses on building an end-to-end machine learning pipeline that" 
    "predicts the quality of wine based on its physicochemical properties."
)


# All the meta data
project_name = "Wine Quality Prediction"
version = "0.0.1"
author_name = "Tipto_Ghosh"
author_email = "tiptoghosh@gmail.com"
project_url = "https://github.com/Tipto-Ghosh/End-To-End-Wine-Quality-Prediction"


setup(
    name = project_name,
    version = version,
    description = description,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    maintainer = author_name,
    maintainer_email = author_email,
    author = author_name,
    author_email = author_email,
    url = project_url,
    packages = find_packages(),
    install_requires = get_requirements(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)