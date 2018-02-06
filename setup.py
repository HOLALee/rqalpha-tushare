from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='rqalpha-mod-tushare',     #mod名
    version="0.1.0",
    description='RQAlpha Mod to say hello',
    packages=find_packages(exclude=[]),
    author='your name',
    author_email='your email address',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/HOLALee/rqalpha-mod-tushare',
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
