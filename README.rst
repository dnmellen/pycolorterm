===============================
PyColorTerm
===============================

.. image:: https://badge.fury.io/py/pycolorterm.png
    :target: http://badge.fury.io/py/pycolorterm
    
.. image:: https://travis-ci.org/dnmellen/pycolorterm.png?branch=master
        :target: https://travis-ci.org/dnmellen/pycolorterm

.. image:: https://coveralls.io/repos/dnmellen/pycolorterm/badge.png
        :target: https://coveralls.io/r/dnmellen/pycolorterm

.. image:: https://pypip.in/d/pycolorterm/badge.png
        :target: https://crate.io/packages/pycolorterm?version=latest


PyColorTerm allows you to write colored and styled lines out in the terminal from Python and in a pythonic way

* Free software: BSD license
* Documentation: http://pycolorterm.rtfd.org.

Features
--------

* Get your line prints pretty with color and style formatting
* Python 3 ready!
* Pythonic


Getting started
--------

Installation
===========
.. code-block :: bash

    $ pip install pycolorterm

Usage
============
.. code-block :: python

    from pycolorterm import pycolorterm
    with pycolorterm.pretty_output(pycolorterm.FG_GREEN) as out:
        out.write('Works OK!')
