from setuptools import setup, find_packages

setup(
    name='pygoofball',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='uhh',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/bagoflays/pygoofball',
    author='bagoflays',
    author_email='smvreactionschannel@gmail.com'
)
