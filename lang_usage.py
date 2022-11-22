#!/usr/bin/python3
'''
    This is the file that takes in all the modules
    and functions that will translate and run the languages
''' 
from googletrans import Translator
translator = Translator()
context = {
    '1' : 'af',
    '2' : 'am',
    '3' : 'ny',
    '4' : 'kr' ,
    '5' : 'ha',
    '6' : 'ig',
    '7' : 'mg',
    '8' : 'st', 
    '9' : 'sn', 
    '10' : 'so',
    '11' : 'sw', 
    '12' : 'xh',
    '13' : 'yo', 
    '14' : 'zu',
}

def translate_lang(word,language):
    ''' runs the modules and functions that run the langs '''
    lang = context[str(language)]
    result = translator.translate(text=word, dest=lang)
    return result



