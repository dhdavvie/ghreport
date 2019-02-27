from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="gh-report",
    version="0.1",

    author="George P.",
    author_email="digitalduke@gmail.com",
    
    description="Review your daily activity on GitHub.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    url="https://github.com/digitalduke/gh-report",

    packages=find_packages(),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
)
