import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tvoozkothxxx001",
    version="7.0.0",
    description="tvoozkothxxx001: Controller Script for tvoozkothxxx001",
    long_description=README,
    long_description_content_type="text/markdown",
    author="TvoozMagnificent",
    author_email="luchang1106@icloud.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["tvoozkothxxx001"],
    include_package_data=True,
    install_requires=["funcopy","rich"],
    url="https://github.com/TvoozMagnificent/tvoozkothxxx001",
)


