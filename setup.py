from setuptools import setup


def readme():
    return open("README.md", "r").read()

requirements = [
    'six'
]

setup(
    name='infinity',
    packages=['infinity'],
    version='1.0.0',
    long_description=readme(),
    description="generate awesome mathematical series",
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/infinity.git',
    license="MIT",
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ],
    install_requires=requirements
)
