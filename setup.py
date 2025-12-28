from setuptools import setup, find_packages

setup (
    name = 'ugit',
    version='1.0',
    packages=find_packages(),
    entry_points = {
        'console_scripts':[
            'ugit = ugit.cli:main'
        ]
    }
)