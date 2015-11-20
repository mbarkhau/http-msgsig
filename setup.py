from setuptools import setup, find_packages

setup(
    name='http_msgsig',
    version="0.1.0",
    description='API Tools for Signing HTTP Messages',
    author='Manuel Barkhau',
    author_email='mbarkhau@gmail.com',
    install_requires=[
        "flask",
        "requests",
        "decorator",
    ],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        'Topic :: Utilities',
    ],
)

