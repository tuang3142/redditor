from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='redditor',
    version='0.2.3',
    author="Tuan Nguyen",
    author_email="tuan.nguyenviet271@gmail.com",
    description="use reddit like a doge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daenylio/redditor",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'praw'
    ],
    entry_points='''
        [console_scripts]
        redditor=redditor.main:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)