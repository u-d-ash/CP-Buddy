from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory/"README.md").read_text()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='cp_buddy',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bidoo=cp_buddy.main:main',
        ],
    },
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={
        'my_package': ['template.cpp'],
    },
)
