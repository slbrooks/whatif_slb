from setuptools import find_packages, setup

setup(
    name='whatif',
    packages=find_packages("src"),
    package_dir={"": "src"},
    version='0.1.0',
    description='whatif project management and packaging',
    author='Sheila Brooks',
    license='',
)
