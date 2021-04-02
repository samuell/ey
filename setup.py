import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='ey',
    version='0.3.1',
    description='Simple and easy-to-use library for executing shell commands saving data to the file system without re-executing already executed tasks.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Samuel Lampa',
    author_email='samuel.lampa@rilnet.com',
    url='https://github.com/samuell/ey',
    license='MIT',
    keywords='workflows workflow pipeline task',
    packages=[
        'ey',
    ],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
)
