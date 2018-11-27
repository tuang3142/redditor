from setuptools import setup

setup(
    name='redditor',
    version='0.1',
    py_modules=['redditor'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        redditor=redditor:cli
    ''',
)