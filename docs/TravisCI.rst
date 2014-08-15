Continuous Integration With TravisCI
####################################

..  _TravisCI:  https://travis-ci.org/

TravisCI_ is a hosted continuous integration service that lets you test an
application you are managing using Github_. SInce so many :term:`open source`
projects use Github_ it is natural to use TravisCI as part of your development
and testing process.

Signing Up
**********

To get started, you need to sign up for an account on the system. Navigate to
the TravisCI site and click on the :menuselection:`Sign in with Github` link at
the top right. You will be taken to a page where you identify the project you
want to test. Basically, you are giving permission allowing access to your
Github :term:`repository`.

Activate Github Hook
====================

Click on :menuselection:`Authorize application` at the bottom of this page.
You will enter your Github_ account password and TravisCI_ will log into your
account and generate a list of all projects you have hosted there. There is a
set of switches on each project you use to turn TravisCI support on for each
one. 

..  note::

    If you add a new :term:`repository`, there is a :menuselection:`Sync now`
    button tat the top you can use to update this list.

Set Up Your Project
===================

Create your basic application, including a fresh :term:`repository` on Github_. Be sure to add a `setup.py` file for your project. It should list the dependencies, but you will still need to list those in the `requirements.txt` file we will use for installing the project environment.

Here is my basic `setup.py` file:

..  code-block:: text

    import os
    from setuptools import setup

    def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

    setup(
        name='PyLit4',
        version='0.1dev',
        url='https://github.com/rblack42/PyLit4',
        license='BSD',
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

Finally, you need to add a configuration file to your project. This file is
named `.travis.yml`. Here is mine:

..  literalinclude::    ../.travis.yml
    :linenos:

Trigger a Build
===============

TravisCI adds a :term:`post-commit hook` to your Github_ project so that each
time you :term:`commit` a modification to your project, a test will be run. The
whole point of this is that once this is set up, you can forget about it, and
see the results of this test 


