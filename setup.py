from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="quad5",
    version='{{VERSION_PLACEHOLDER}}',
    description="""Quadratic Approximation custom step sampler for PYMC.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Carsten Jørgensen",
    packages=find_packages(include=["quad5"]),
    keywords=['Bayesian Statistics', 'Probabalistic Programming Language', 'Python'],
    classifiers=[
        "Intended Audience :: PYMC users",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    license="MIT",
    url="https://github.com/carsten-j/quad5",
)
