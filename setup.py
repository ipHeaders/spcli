import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="sp",
    version='0.1',
    py_modules=['sp'],
    setup_requires=["setuptools_scm"],
    install_requires=[
        "pyedgeconnect",
        "PyYAML==6.0",
        "tabulate==0.8.10"
    ],
    packages=find_packages(),
    package_dir={"lib": "lib"},
    zip_safe=False,
    entry_points='''
        [console_scripts]
        sp=sp:main
    ''',
    python_requires=">=3.7, <4",
)
