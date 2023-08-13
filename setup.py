from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

DESCRIPTION = ""

setup(
    name="selenium_driver",
    author="TZ",
    version="0.0.1",
    author_email="zaptom@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['selenium', 'webdriver-manager'],
    keywords=[],
    classifiers=[]
)
