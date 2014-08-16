PyLit4: Literate Programming with reStructuredText
##################################################

..  _Github:    https:/github.com/rblack42/PyLit4
..  _Gitlab:    https://about.gitlab.com/
..  |ACC|       replace::   Austin Community College

..  image:: https://travis-ci.org/rblack42/PyLit4.svg?branch=master

This application is a Python Flask project designed to provide a web tool for
creating `Literate Programming` based projects. In this system, the
project code is contained in a set of `reStructuredText` files and
extracted from those files each time the code is tested. The application is
designed to be hosted on a service like Github_ or one using GitLab_.

The application is also being continously tested as :term:`commits` are pushed
to Github_ using TravisCI. (The status of the last build is visible at the top
of this page when viewed on Github_).

PyLit4_ is also a general purpose tool I use to host lecture notes for classes
I teach at |ACC|. A running version of the application is at
http://www.pylit.org.

General Program Structure
*************************

This program is structured following this guide:

    * `Matt Wright: How I Structure My Flask Applications <http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html>`_
