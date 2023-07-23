# -*- coding: utf-8 -*-
# ########################################################################                          
# Program: Emeralds
# Author: Jason Drawdy
# Version: 0.0.1
# Date: 07/21/23
# #########################################################################
# Description:
# Contains all classes and functions for creating a complete pip package.
# #########################################################################
from setuptools import setup, find_packages
import codecs
import os

class Setup:
    """A encapsulation object containing all necessary components for creating a pip package."""
    def __init__(self: "Setup") -> None:
        self.version = '0.0.1'
        self.description = 'A testing package for learning PyPi.'
        self.long_description = self.get_readme()
        self.configure_installation()

    def get_readme(self: "Setup"):
        """Returns the current README documentation or a default description."""
        default_data = 'Cool package for testing!'
        current_path = os.path.abspath(os.path.dirname(__file__))
        readme_file = os.path.join(current_path, "README.md")
        if os.path.exists(readme_file):
            with codecs.open(readme_file, encoding="utf-8") as file:
                return file.read()
        return default_data 

    def configure_installation(self: "Setup"):
        """Perform the actual package installation using all provided `setup()` information."""
        setup(
            name="emeralds",
            version=self.version,
            author="Jason Drawdy",
            author_email="<40871836+jasondrawdy@users.noreply.github.com>",
            description=self.description,
            long_description_content_type="text/markdown",
            long_description=self.long_description,
            packages=find_packages(),
            extras_require={'dev': ['sphinx-rtd-theme', 'sphinx-autoapi']},
            keywords=['emeralds', 'test', 'package'],
            classifiers=[
                "Development Status :: 1 - Planning",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "Programming Language :: Python :: 3.11+",
                "Operating System :: OS Independent",
            ]
        )

# Initializing the object acts as a function call due to
# how the __init__() function in the object itself works.
Setup()