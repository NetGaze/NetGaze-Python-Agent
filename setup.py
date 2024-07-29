import json
import os
from typing import List

from setuptools import setup, find_packages

version = '0.0.1'


def get_requirements_to_install() -> List[str]:
    __curr_location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    requirements_txt_file_as_str = f'{__curr_location__}/requirements.txt'
    with open(requirements_txt_file_as_str, 'r') as reqfile:
        libs = reqfile.readlines()
        for i in range(len(libs)):
            libs[i] = libs[i].replace('\n', '')
    return libs



setup(
    name='netgaze-agent',
    version=version,
    description='A lightweight agent that collects connectivity information from configured endpoints and reports it '
                'to the NetWatch server.',
    long_description='A lightweight agent that collects connectivity information from configured endpoints and reports it '
                'to the NetWatch server.',
    install_requires=get_requirements_to_install(),
    author='Amith Koujalgi',
    author_email='koujalgi.amith@gmail.com',
    packages=find_packages(include=['netgaze_agent']),
    package_data={
        'netgaze_agent': ['static/*', 'static/**/*'],
    },
    entry_points={
        'console_scripts': [
            'netgaze = netgaze_agent.netgaze_agent_cli:main'
        ],
    },
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ]
)
