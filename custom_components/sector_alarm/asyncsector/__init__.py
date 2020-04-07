'''
    Asynchronous package for Sector Alarm
'''
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

__version__ = '0.2.2'

__all__ = ['AsyncSector']

from .asyncsector import AsyncSector


