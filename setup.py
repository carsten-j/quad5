import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quad5",
    version="0.1.7",
    description="""Quadratic Approximation custom step sampler for PYMC.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Carsten Jørgensen",
    packages=find_packages(include=["quad5"]),
    keywords=["Bayesian Statistics", "Probabalistic Programming Language", "Python"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["PYMC==5.15.0"],
    license="MIT",
    url="https://github.com/carsten-j/quad5",
)
