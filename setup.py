from distutils.core import setup

import setuptools

VERSION = '0.0.13'
DESCRIPTION = 'Biher projects'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

# Setting up
setup(
    name="Biher2py",
    packages=setuptools.find_packages(),
    version=VERSION,
    author="Rebison",
    author_email="rebison85@gmail.com",
    url="https://github.com/Rebison/Biher2py",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
