# -*- coding: utf-8 -*-
"""
Date: 01/2023
Version: 1.0
Author: (C) Capgemini Engineering - Antonio Galan, Jose Pena
Website: www.capgemini.com


Setup
=====

Script to configure the creation of the wheel

"""
import os
import setuptools
from pkg_resources import parse_requirements


def get_req(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        reqs = [parse_requirements(req)
                for req
                in file.readlines()]
    return reqs


about = {}
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "src", "__version__.py")) as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()

extras = {
    "test": [
        "black",
        "coverage",
        "flake8",
        "mock",
        "pydocstyle",
        "pytest",
        "pytest-cov",
        "tox",
        "undecorated",
        "pytest-dependency"
    ],
    "analysis": [
        "jupyterlab",
        "ipykernel",
        "pandas[plot]",
        "matplotlib",
        "seaborn",
        "pandas-profiling"
    ]
}

if __name__ == '__main__':
    setuptools.setup(
        name=about["__title__"],
        description=about["__description__"],
        version=about["__version__"],
        author=about["__author__"],
        author_email=about["__author_email__"],
        long_description=readme,
        long_description_content_type="text/markdown",
        url=about["__url__"],
        license=about["__license__"],
        platforms=["unix", "linux", "osx", "cygwin", "win32"],
        packages=setuptools.find_packages(),
        include_package_data=True,
        python_requires=">=3.6,<=3.12",
        install_requires=get_req(os.path.join(here, "requirements", "core.txt")),
        extras_require=extras,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
        ],
    )
