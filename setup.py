from setuptools import setup, find_packages
from setuptools import *

setup(
    name = "dCrypy",
    version = "1.0.1",
    author = "Stealth.py",
    url = "https://github.com/Stealth-py",
    description = "A CLI to decode ciphertext to plaintext from the given options.",
    license = "Apache",
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        "Click",
    ],
    entry_points = {
        "console_scripts":[
            "dcrypy=dcrypy.cli:cli"
        ]
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)

"""
dCrypy
Stealth.py, 2021
"""