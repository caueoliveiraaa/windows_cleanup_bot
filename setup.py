"""This file is responsible for the project's setup.

PROJECT_NAME (str): Project's name.
PROJECT_VERSION (str): Project's version.
PROJECT_AUTHOR (str): Project's author.
PROJECT_DESCRIPTION (str): Project's description.
"""

from setuptools import find_packages, setup

PROJECT_NAME: str = "Cleanup bot"
PROJECT_VERSION: str = "0.1.0"
PROJECT_AUTHOR: str = "Cauê Oliveira"
PROJECT_DESCRIPTION: str = (
    "This project cleans up junk files and opens up a bit of space "
    "in the local windows operational system."
)

mandatory_libs: list[str] = []
for encoding in ["utf-16", "utf-8"]:
    try:
        with open("requirements.txt", "r", encoding=encoding) as file:
            mandatory_libs = file.read().splitlines()
            break
    except UnicodeDecodeError:
        print(f"{encoding} is not valid.")

if not mandatory_libs:
    raise ValueError("Could not find libs in 'requirements.txt'.")

setup(
    name=PROJECT_NAME,
    versin=PROJECT_VERSION,
    packaes=find_packages(exclude=["tests"]),
    instal_requires=mandatory_libs,
    author=PROJECT_AUTHOR,
    description=PROJECT_DESCRIPTION,
)
