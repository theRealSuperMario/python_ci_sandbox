"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages
import glob
import os

setup(
    name='theSandboxProject',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['pytest-runner', 'pytest'],
    setup_requires=["pytest"],
    tests_require=["pytest"],
    py_modules=[os.path.splitext(os.path.basename(path))[0]
                for path in glob.glob('src/*.py')],
    # entry_points={
    #     'console_scripts': [
    #         'tasks = tasks.cli:tasks_cli',
    #     ]
    # },
)
