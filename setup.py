#! /usr/bin/env python3

"""Installation script for this package."""

import os

from setuptools import setup

setup(
    name="package",
    version="0.1.0",
    description="<one line to give the program's name and a brief idea of what it does.>",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Dennis Hedback",
    packages=["package"],
    install_requires=[],
)