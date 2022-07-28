from setuptools import setup

setup(
    name="sp",
    version='0.1',
    py_modules=['sp'],
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
        sp=sp:main
    ''',
)
