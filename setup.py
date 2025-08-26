import pathlib

from setuptools import find_packages, setup

from mootdx import __author__, __version__


def read_requirements():
    """从 requirements.txt 读取 install_requires"""
    req_file = pathlib.Path("requirements.txt")
    if not req_file.exists():
        return []
    lines = req_file.read_text(encoding="utf-8").splitlines(keepends=False)
    requires = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        requires.append(line.split(";")[0].strip())
    return requires


setup(
    name="mootdx",
    version=__version__,
    description="通达信数据读取接口.",
    author=__author__,
    url="https://www.mootdx.com",
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "mootdx = mootdx.__main__:entry",
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
)
