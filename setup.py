#! /usr/bin/env python3

"""Installation script for this benkpress-plugins."""

import os

from setuptools import setup

setup(
    name="benkpress-plugins",
    version="0.1.0",
    description="Plugin API for interoperating with benkpress.",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Dennis Hedback",
    packages=["benkpress_plugins"],
    install_requires=["sklearn"],
    entry_points={
        "benkpress_plugins.preprocessors": ["Passthrough=benkpress_plugins.preprocessors.PassthroughPagePreprocessor"],
        "benkpress_plugins.pipelines": ["Dummy=benkpress_plugins.pipelines.DummyPipeline"]
    }
)