from setuptools import setup, find_packages


setup(
    name='horoscofox',
    version='0.2',
    url='https://github.com/horoscofox/pyhoroscofox',
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
