from setuptools import setup


setup(
    name='redditor',
    version='1.0',
    py_modules=['redditor'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        redditor=redditor:main
    ''',
)