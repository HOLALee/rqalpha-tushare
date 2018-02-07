from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='rqalpha-mod-tushare',     #mod名
    version="0.1.0",
    description='RQAlpha Tushare Mod',
    packages=find_packages(exclude=[]),
    author='liyuzhong',
    author_email='744234398@qq.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/HOLALee/rqalpha-tushare',
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.7',
    ],
)
