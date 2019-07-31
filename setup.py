from setuptools import setup, find_packages

setup(
    name='pyfse',
    version='0.9.0',
    packages=find_packages(),
    install_requires=['numpy', 'cffi'],
    setup_requires=['cffi', 'wheel'],
    cffi_modules=['fse/build.py:ffibuilder'],
)
