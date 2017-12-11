from setuptools import setup

setup(
    name = 'Program',
    version = '0.1',
    description = 'An example of an installable program',
    author = 'ghickman',
    url = '',
    license = 'MIT',
    packages = ['program'],
    entry_points = {'console_scripts': ['prog = program.program',],},
)
