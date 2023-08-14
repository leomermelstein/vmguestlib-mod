#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = (0, 1, 2)

if __name__ == '__main__':

    setup(
        name = 'vmguestlib-mod',
        version = '0.1.5',
        author='Leo Mermelstein',
        author_email='leomermelstein@gmail.com',
        url='https://github.com/leomermelstein/vmguestlib-mod',
        description='Python API for interacting with VMware\'s VMGuestLib SDK',
        license = 'GPLv2',
        install_requires=[],
        py_modules = ['vmguestlib', ],
        scripts=[ 'vmguest-stats', ],
        keywords = ['Virtual', 'vmware', 'ESX', 'ESXi', 'VMGuestLib', 'SDK', 'API'],
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Operating System :: OS Independent',
            'Development Status :: 5 - Production/Stable',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Quality Assurance',
            'Topic :: Software Development :: Testing',
            'Topic :: System :: Distributed Computing',
            'Topic :: System :: Emulators',
            'Topic :: System :: Hardware',
            'Topic :: System :: Operating System',
            'Topic :: System :: Systems Administration',
            'Topic :: Utilities'
        ],
        long_description='''Python API for interacting with VMware\'s VMGuestLib SDK
This software is (c) 2013-2014 Dag Wieers dag@wieers.com, modified 2023 by Leo Mermelstein
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version.''',
    )

# vim:ts=4:sw=4:et
