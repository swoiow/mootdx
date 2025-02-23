from setuptools import setup

from mootdx import __author__, __version__


setup(
    name="mootdx",
    version=__version__,
    packages=[
        "mootdx",
        "mootdx.cache",
        "mootdx.tools",
        "mootdx.utils",
        "mootdx.contrib",
        "mootdx.financial",
    ],
    url="",
    license="",
    author=__author__,
    description=""
)
