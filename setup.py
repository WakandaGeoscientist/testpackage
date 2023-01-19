from setuptools import setup

setup(
    name='testpackage',
    version='0.0.1',
    author='David Nworie',
    author_email='dcnworie@mines.edu',
    packages=['testpackage'],
    url='http://pypi.python.org/pypi/testpackage/',
    license='LICENSE.txt',
    description='Your first package.',
    long_description=open('README.txt').read(),
    install_requires=[],#Add any dependencies and versions.
    )
