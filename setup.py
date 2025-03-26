from setuptools import setup, find_packages

setup(
    name="mi_proyecto",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mi_proyecto=main:main",
        ],
    },
)
