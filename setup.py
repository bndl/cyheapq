#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

extensions = [
    Extension('cyheapq', ['cyheapq.pyx']),
]

try:
    from Cython.Build import cythonize
    extensions = cythonize(extensions,
                           compiler_directives={
                               'language_level': 3
                           })
except ImportError:
    pass


if __name__ == '__main__':
    setup(
        name='cyheapq',
        version='0.1.1',
        url='https://github.com/bndl/cyheapq',
        description='Heapq in Cython',
        long_description=open('README.rst').read(),
        author='Frens Jan Rumph',
        author_email='mail@frensjan.nl',

        packages=(
            find_packages()
        ),

        include_package_data=True,
        zip_safe=False,

        install_requires=[],
        extras_require=dict(
            dev=[
                'cython',
            ],
        ),

        ext_modules=extensions,

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
    )
