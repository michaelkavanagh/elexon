import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elexon",
    version="0.0.1",
    author="Michael Kavanagh",
    author_email="michael@michaelkavanagh.me",
    description="A simple wrapper for the Elexon BMRS API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MichaelKavanagh/elexon-bmrs-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
