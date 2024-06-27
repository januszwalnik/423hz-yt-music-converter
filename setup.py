import os
import pkg_resources
from setuptools import setup, find_packages


setup(
    name="423-yt-converter",
    py_modules=["423-yt-converter"],
    version="1.0.0",
    description="",
    author="jw",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True
)