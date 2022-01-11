from setuptools import setup

def readme():
    with open('pypi.md') as f:
        return f.read()

setup(name='RadioF1',
    version='0.1',
    description='Get F1 Radio messages from their official api. ',
    long_description=readme(),
    url='https://github.com/siddharth-tewari/F1-TeamRadio',
    author='SiddharthTewari',
    license='MIT',
    install_requires=[
        'jsonstream',
    ],
    scripts=['bin/graph-power'],

    },
)
