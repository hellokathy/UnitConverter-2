'''
Created on 15/01/2013

@author: joshua
'''
from reprlib import repr

class CategoryError(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
