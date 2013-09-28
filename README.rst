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

    from pycolorterm.pycolorterm import print_pretty

    print_pretty('This is <BOLD>awesome<END> <FG_RED>because<END> you can <UNDERSCORE>mix<END> <BG_BLUE>many styles easily<END>')


Result
============
.. image:: https://raw.github.com/dnmellen/pycolorterm/master/pycolorterm_example.png
