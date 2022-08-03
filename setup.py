import pathlib
#from distutils.core import setup

from setuptools import find_packages,setup

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="sp",
    version='0.0.7',
    py_modules=['sp'],
    setup_requires=["setuptools"],
    install_requires=[
        "pyedgeconnect",
        "PyYAML==6.0",
        "tabulate==0.8.10",
        "importlib_metadata",
    ],
    packages=find_packages(where="spcli"),
    package_dir={"": "spcli"},
    include_package_data=True,
    package_data={"lib": ["*.py",]},

    #zip_safe=False,
    entry_points='''
        [console_scripts]
        sp=sp:main
    ''',
    python_requires=">=3.7, <4",
)
