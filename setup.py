from setuptools import setup, find_packages

setup(
    name='python-fse',
    version='0.3.3',
    packages=find_packages(),
    install_requires=['numpy', 'cffi'],
    setup_requires=['cffi', 'wheel'],
    cffi_modules=['fse/build.py:ffibuilder'],
)
