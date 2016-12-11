'''
This module contains user's self-defined exceptions.

@author: Xianzhi Cao (xc965)
'''

# Error: Data not available in this Country.
class NoCountryDataError(Exception):
    def __str__(self):
        return 'No Data Available in this country.\n'
