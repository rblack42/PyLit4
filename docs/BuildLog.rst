PyLit4 Build Log
################

..  include::   /references.inc

v0.1.0: Basic application setup
*******************************

This version is an attempt to build a minimal Flask application with testing
set up for :program:`nose`. The application can be clones by running these
commands:

..  code-block:: text

    $ git clone https://github.com/rblack42/PyLit4.git
    $ fab install

Of course, this assumes you have the following tools installed on the
development system:

    * Python 2.7.x
    * virtualenv
    * Fabric

Testing v0.1.0
==============

The test set up for this step simply checks that the application delivers a
simple "Hello, World" message. 

v0.1.1: Move to an Application Factory Setup
********************************************

The next modification needs no new test, and simply reorganizes the application
to a blueprint. We also use an application factory to create the Flask_ app. WE also move the Flask-Script to manage the application.

Test v0.0.1
===========

The existing tests should still run.
