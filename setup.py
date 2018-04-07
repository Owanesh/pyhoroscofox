from setuptools import setup, find_packages


setup(
    name='horoscofox',
    version='1.0',
    url='https://github.com/horoscofox/pyhoroscofox',
    license='MIT',
    author='Owanesh and astagi',
    description='',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        "requests==2.18.4"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
