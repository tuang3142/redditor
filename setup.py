from setuptools import setup


setup(
    name='redditor',
    version='2.0',
    py_modules=['redditor'],
    install_requires=[
        'Click',
        'Praw'
    ],
    entry_points='''
        [console_scripts]
        redditor=main:cli
    ''',
)