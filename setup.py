import pathlib
#from distutils.core import setup

from setuptools import find_packages,setup

here = pathlib.Path(__file__).parent.resolve()

install_requires = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

setup(
    name="pyspcli",
    version='0.1.1',
    py_modules=['sp'],
    setup_requires=["setuptools"],
    install_requires=install_requires,
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
