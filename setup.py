from setuptools import setup, find_packages

setup(
    name="lukesutils",
    version="1.0.0",
    package_dir={"": "scripts"},
    packages=find_packages(where="scripts"),
    python_requires=">=3.10",
)