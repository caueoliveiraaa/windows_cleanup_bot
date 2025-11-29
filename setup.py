"""This file is responsible for the project's setup."""

from setuptools import find_packages, setup

_PROJECT_NAME: str = "Cleanup bot"
_PROJECT_VERSION: str = "0.1.0"
_PROJECT_AUTHOR: str = "Cauê Oliveira"
_PROJECT_DESCRIPTION: str = (
    "Cleans up some junk files and opens up a little bit of space, "
    "in the local machine."
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
    name=_PROJECT_NAME,
    version=_PROJECT_VERSION,
    packages=find_packages(exclude=["tests"]),
    install_requires=mandatory_libs,
    author=_PROJECT_AUTHOR,
    description=_PROJECT_DESCRIPTION,
)
