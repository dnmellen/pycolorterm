#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pycolorterm
----------------------------------

Tests for `pycolorterm` module.
"""

import sys
import unittest

from pycolorterm.pycolorterm import pretty_output, styles, print_pretty


class TestPycolorterm(unittest.TestCase):

    def setUp(self):
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")

    def _get_output(self):
        """Returns stdout"""
        return sys.stdout.getvalue().strip()  # because stdout is an StringIO instance

    def test_red_text(self):
        with pretty_output(styles['FG_RED']) as out:
            out.write('This is a test in RED')
        self.assertEquals(self._get_output(), '\x1b[31mThis is a test in RED\x1b[0m')

    def test_blue_text(self):
        with pretty_output(styles['FG_BLUE']) as out:
            out.write('This is a test in BLUE')
        self.assertEquals(self._get_output(), '\x1b[34mThis is a test in BLUE\x1b[0m')

    def test_bold_green_text(self):
        with pretty_output(styles['BOLD'], styles['FG_GREEN']) as out:
            out.write('This is a bold text in green')
        self.assertEquals(self._get_output(), '\x1b[1m\x1b[32mThis is a bold text in green\x1b[0m')

    def test_bold_green_bg_text(self):
        with pretty_output(styles['BOLD'], styles['BG_GREEN']) as out:
            out.write('This is a text with green background')
        self.assertEquals(self._get_output(), '\x1b[1m\x1b[42mThis is a text with green background\x1b[0m')

    def test_inline_bold_text(self):
        with pretty_output(styles['FG_GREEN']) as out:
            out.write('This is a green text with ' + styles['BOLD'] + 'bold' + styles['END'] + ' text included')
        self.assertEquals(self._get_output(), '\x1b[32mThis is a green text with \x1b[1mbold\x1b[0m\x1b[32m text included\x1b[0m')

    def test_inline_formatting_text(self):
        with pretty_output() as out:
            out.write('This is {BOLD}awesome{END} {FG_RED}because{END} you can {UNDERSCORE}mix{END} {BG_BLUE}many styles easily{END}'.format(**styles))
        self.assertEquals(self._get_output(), 'This is \x1b[1mawesome\x1b[0m \x1b[31mbecause\x1b[0m you can \x1b[4mmix\x1b[0m \x1b[44mmany styles easily\x1b[0m\x1b[0m')

    def test_print_pretty_red(self):
        print_pretty('{FG_RED}This is a test in RED')
        self.assertEquals(self._get_output(), '\x1b[31mThis is a test in RED\x1b[0m')

    def test_print_pretty_complex(self):
        print_pretty('{FG_RED}This{END} is a {BG_BLUE}{UNDERSCORE}more{END} complex {FG_GREEN}{BOLD}test')
        self.assertEquals(self._get_output(), '\x1b[31mThis\x1b[0m is a \x1b[44m\x1b[4mmore\x1b[0m complex \x1b[32m\x1b[1mtest\x1b[0m')

    def test_issue_pre_formatting(self):
        print_pretty('<FG_RED>This is a test<END> <FG_BLUE>{var1}<END> some variables'.format(var1="My var"))
        self.assertEquals(self._get_output(), '\x1b[31mThis is a test\x1b[0m \x1b[34mMy var\x1b[0m some variables\x1b[0m')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
