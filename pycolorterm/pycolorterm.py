#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


styles = {
    # Text attributes
    'ALL_OFF': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERSCORE': '\033[4m',
    'BLINK': '\033[5m',
    'REVERSE': '\033[7m',
    'CONCEALED': '\033[7m',

    # Foreground colors
    'FG_BLACK': '\033[30m',
    'FG_RED': '\033[31m',
    'FG_GREEN': '\033[32m',
    'FG_YELLOW': '\033[33m',
    'FG_BLUE': '\033[34m',
    'FG_MAGENTA': '\033[35m',
    'FG_CYAN': '\033[36m',
    'FG_WHITE': '\033[37m',

    # Background colors
    'BG_BLACK': '\033[40m',
    'BG_RED': '\033[41m',
    'BG_GREEN': '\033[42m',
    'BG_YELLOW': '\033[43m',
    'BG_BLUE': '\033[44m',
    'BG_MAGENTA': '\033[45m',
    'BG_CYAN': '\033[46m',
    'BG_WHITE': '\033[47m',

    # Special END separator
    'END': '0e8ed89a-47ba-4cdb-938e-b8af8e084d5c',
}

def _prepare(text):
    '''
    Prepares text to style formatting

    :param text: Input text
    :type text: string
    '''
    
    return text.replace('<', '{').replace('>', '}')  # Change <> to {}


class pretty_output():
    '''
    Context manager for pretty terminal prints
    '''

    def __init__(self, *attr):
        self.attributes = attr

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def write(self, msg):
        msg = _prepare(msg)
        style = ''.join(self.attributes)
        print('{}{}{}'.format(style, msg.replace(styles['END'], styles['ALL_OFF'] + style), styles['ALL_OFF']))


def print_pretty(text, **kwargs):
    '''
    Prints using pycolorterm formatting

    :param text: Text with formatting
    :type text: string
    :param kwargs: Keyword args that will be passed to the print function
    :type kwargs: dict

    Example::

        print_pretty('Hello {BG_RED}WORLD{END}')
    '''

    text = _prepare(text)
    print('{}{}'.format(text.format(**styles).replace(styles['END'], styles['ALL_OFF']), styles['ALL_OFF']))
