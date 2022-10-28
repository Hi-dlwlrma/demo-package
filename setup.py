from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="new_library_package",
    version="1.0.0",
    author_name="dungntn",
    author_email="dungntn@gmail.com",
    description="Demo for release package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hi-dlwlrma/demo-package",

    packages=find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.8',
)