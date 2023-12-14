from setuptools import setup, find_packages

setup(
    name='email_automation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'email-automation=main:main'
        ],
    },
)
