========
Usage
========

To use PyColorTerm in a project

.. code-block:: python

    from pycolorterm.pycolorterm import pretty_output, styles
    
    with pretty_output(styles['FG_RED']) as out:
        out.write('This is a test in RED')

    with pretty_output(styles['FG_BLUE']) as out:
        out.write('This is a test in BLUE')

    with pretty_output(styles['BOLD'], styles['FG_GREEN']) as out:
        out.write('This is a bold text in green')

    with pretty_output(styles['BOLD'], styles['BG_GREEN']) as out:
        out.write('This is a text with green background')

    with pretty_output(styles['FG_GREEN']) as out:
        out.write('This is a green text with ' + styles['BOLD'] + 'bold' + styles['END'] + ' text included')

    with pretty_output() as out:
        out.write(styles['BOLD'] + 'Use this' + styles['END'] + ' even with ' + styles['BOLD'] + styles['FG_RED'] + 'no parameters' + styles['END'] + ' in the with statement')

    with pretty_output() as out:
        out.write('This is {BOLD}awesome{END} {FG_RED}because{END} you can {UNDERSCORE}mix{END} {BG_BLUE}many styles easily{END}'.format(**styles))
