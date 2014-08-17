PyLit4 Build Log
################

..  include::   docs/references.inc

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

The organization I use is based on Matt Wright's organization.

    * `How I Structure My Flask Applications
      <http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html>`_

Testing v0.1.0
==============

The test set up for this step simply checks that the application delivers a
simple "Hello, World" message. 

v0.1.1: Move to an Application Factory Setup
********************************************

The next modification needs no new test, and simply reorganizes the application
to a blueprint. We also use an application factory to create the Flask_ app. We also move the Flask-Script to manage the application.

Test v0.1.1
===========

The existing tests should still run.

Step 1: Add manager
-------------------

Create the `manage.py` file in the project folder. This file imports `create_app` from `pylit.api`, so we add this logic to the api `__init__.py` file.

Step 2: Move to application factory
-----------------------------------

the factory is set up in `pylit/factory.py`. The `create_app` method in this file is called by the `create_app` method in the api. (:TODO: explain why)


Create a '`factory.py` file where the application will be created. We set up an `api` package where the actual application creation logic is kept.


Step 3: Get a basic route running
---------------------------------

In this step, we add basic routing to the app. The best place to do this is in
the `factory.py` file where the application is created. (We will move this
later).


Step 4: add site map
--------------------

As the flask application develops, I find it handy to see what endpoints exist and what functions they are bound to. 

Step 5: Add Frontend Blueprints
-------------------------------

In this step, we move the front display into a Flask Blueprint. This blueprint
will be called `frontend`, and captures all the basic logic for top level views.

A blueprint is created for each page on the site. These are stored in the
`views` directory under `frontend`.


v0.1.2: Set up application logging
**********************************

Test v0.1.2
===========

Add a test to see if the log file is created

Step 1: Add logging setup to `app.py`

ref: skylines.app example code

v0.1.3: Add configuration
*************************

This modification adds a configuration module

Test v0.1.3
===========

Add a test to check the logging file

v0.1.4: Add basic templating
****************************

Start Jinja templating for the app

Test v0.1.4
===========

Test the strings are still there after switching to render_template.

v0.2.0: Add reStructuredText
****************************

Test v0.2.0
===========

    * test app config variable
    * test rst directory exists
    * test table of contents
    * test empty page rendering
    * test rendered test page



