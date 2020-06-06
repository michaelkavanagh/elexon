import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elexon",
    version="0.0.7",
    author="Michael Kavanagh",
    description="A simple wrapper for the Elexon BMRS API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MichaelKavanagh/elexon",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'elexon = elexon.__main__:main'
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests']
)
