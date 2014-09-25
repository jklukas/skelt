from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# # Get the long description from the relevant file
# with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='skelt',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='0.0.1',

    description='Creating and rehydrating code skeletons since 2014',
    # long_description=long_description,

    # The project's main homepage.
    url='https://github.com/jklukas/skelt',

    # Author details
    author='Jeff Klukas',
    author_email='jeff@klukas.net',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='library setup generator skeleton',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['skelt'],

)
