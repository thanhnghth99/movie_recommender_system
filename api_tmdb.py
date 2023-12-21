'''
Function to read and store personal API_KEY

'''

from api import *

def API_KEY():
    with open('API_KEY.txt') as file:
        api_key = file.read().strip()

    return api_key

