# Copyright (c) 2014 Michael Howitz
# See also LICENSE.txt

# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""Math exercises for kids.
"""

from setuptools import setup, find_packages
import glob
import os.path


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


setup(
    name='icemac.mathexercise',
    version='0.1.dev0',

    install_requires=[
        'setuptools',
        'odfpy',
        ],

    extras_require={
        'test': [
            ],
        },

    entry_points={
        'console_scripts': [
            'mathexercise.txt=icemac.mathexercise.txt:main',
            'mathexercise.odt=icemac.mathexercise.odt:main',
            ]
        },

    author='gocept <mail@gocept.com>',
    author_email='mail@gocept.com',
    license='ZPL 2.1',
    url='https://projects.gocept.com/projects/icemac-mathexercise/',

    keywords='odf math exercise kid addition subtraction',
    classifiers="""\
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 2 :: Only
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
            'README.txt',
            'HACKING.txt',
            'CHANGES.txt',
            )),

    namespace_packages=['icemac'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('', glob.glob(project_path('*.txt')))],
    zip_safe=False,
    )
