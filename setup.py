from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="ghreport",
    version="0.8",

    author="George P.",
    author_email="digitalduke@gmail.com",
    
    description="Review your activity on GitHub.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    url="https://github.com/digitalduke/ghreport",

    packages=find_packages(exclude=['tests*']),

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

    entry_points={
              'console_scripts': [
                  'ghreport = ghreport.ghreport:run',
              ]
    },
)
