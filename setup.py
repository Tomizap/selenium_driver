from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

DESCRIPTION = ""

setup(
    name="selenium_driver",
    author="TZ",
    author_email="zaptom@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['selenium', 'undetected_chromedriver'],
    dependency_links=[
        "git+git://github.com/ultrafunkamsterdam/undetected-chromedriver#undetected_chromedriver",
    ],
    keywords=[],
    classifiers=[]
)
