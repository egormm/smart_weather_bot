from pkg_resources import parse_requirements
from setuptools import setup
from typing import List


def load_requirements(fname: str) -> List:
    requirements = []
    with open(fname, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


setup(
    name="Smart weather bot",
    version="0.0.1",
    author="Egor Makrushin",
    author_email="egormm@gmail.com",
    license="UNLICENSED",
    description="Example tg bot for CTO school",
    long_description=open('README.md').read(),
    url='https://t.me/great_weather_cto_bot',
    platforms='all',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    python_requires='>=3.8',
    install_requires=load_requirements('requirements.txt'),
    extras_require={'dev': load_requirements('requirements.dev.txt')},
)
