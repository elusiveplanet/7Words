import sys
import re
from os import path
from setuptools import find_packages, setup

assert sys.version_info[0] == 3, "7Words requires Python 3."

VERSIONFILE = "7Words/__init__.py"
ver_file = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, ver_file, re.M)

if mo:
    version = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in {}".format(VERSIONFILE))

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sevenwords',
    version=version,
    description='Download lyrics and metadata from Genius.com and determine potential FCC violations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    author='Alexis J. Renderos',
    url='https://github.com/renderos17/7Words',
    keywords='genius api genius-api music lyrics artists albums songs FCC violation 7words',
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            '7Words = 7Words.__main__:main']
    },
    classifiers=[
        'Topic :: Software Development :: Libraries',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
