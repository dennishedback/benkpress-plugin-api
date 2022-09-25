#! /usr/bin/env python3

"""Installation script for this benkpress_api."""

import os

from setuptools import setup

setup(
    name="benkpress_api",
    version="0.1.0",
    description="API for interoperating with benkpress.",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Dennis Hedback",
    packages=["benkpress_api"],
    install_requires=["sklearn"],
)