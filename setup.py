import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PyLit4',
    version='0.1dev',
    url='https://github.com/rblack42/PyLit4',
    license='BSD3',
    author='Roie Black',
    author_email='rblack@austincc.edu',
    description='Literate programming with reStructuredText',
    long_description=read('README.rst'),
    packages='[pylit4'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_required=(
        'Flask>=0.10.1',
        'nose>=1.3.3'
    ),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
