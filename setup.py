from setuptools import setup

setup(
    name='flask-rollbar',
    version='1.0.1',
    url='https://github.com/angstwad/flask-rollbar',
    license='Apache v2.0',
    author='Paul Durivage',
    author_email='pauldurivage@gmail.com',
    description='A sane configuration for Rollbar for Flask selfishly based '
                'on my own needs',
    packages=['flask_rollbar'],
    install_requires=['rollbar>=0.11.0', 'flask>=0.10.1', "blinker==1.4"]
)
