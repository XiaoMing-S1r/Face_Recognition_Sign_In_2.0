from __future__ import division, absolute_import, print_function

__version__ = '0.9.1'


def setup(app, *args, **kwargs):
    from .numpydoc import setup
    return setup(app, *args, **kwargs)
