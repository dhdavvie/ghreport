from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="ghreport",
    version="0.9b1",

    author="George P.",
    author_email="digitalduke@gmail.com",
    
    description="Review your activity on GitHub.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    license="MIT",
    
    url="https://github.com/digitalduke/ghreport",

    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'PyGithub>=1.43.5',
        'python-dateutil>=2.8.0',
    ],
    python_requires='>=3',

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
