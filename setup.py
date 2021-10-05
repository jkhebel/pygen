from setuptools import setup

setup(
    name='pygen',
    version='0.1.0',
    py_modules=['pygen'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'pygen = pygen:cli'
        ],
    },
)
