from setuptools import setup

setup(
    name="sp",
    version='0.1',
    py_modules=['sp'],
    install_requires=[
        "pyedgeconnect",
        "PyYAML==6.0"
    ],
    entry_points='''
        [console_scripts]
        sp=sp:main
    ''',
    python_requires=">=3.7, <4",
)
