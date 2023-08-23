from pathlib import Path
from setuptools import setup, find_packages


def post_install():
    """ Implement post installation routine """
    with open('./requirements.txt') as f:
        install_requires = f.read().splitlines()

    return install_requires


def pre_install():
    """ Implement pre installation routine """
    # read the contents of your README file
    global long_description
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()


pre_install()


setup(
    name='besco',
    version='0.0.6',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["besco"],
    setup_requires=[
        'svgpathtools'
    ],
    url='https://github.com/SajjadAemmi/besco',
    license='',
    author='Sajjad Aemmi',
    author_email='sajjadaemmi@gmail.com',
    description='Besco is not only a Python package, Besco is a way of life.',
    include_package_data=True,
    package_data={"besco": ['azg.svg']},
    install_requires=post_install(),
    entry_points={
        "console_scripts": ["besco=besco.besco:main"],
    },
)
