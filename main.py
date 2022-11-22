#!/usr/bin/python3
'''The opening file for the application'''
import json


translate_lang = __import__('lang_usage').translate_lang


lan_supported = {
    1 : 'Afrikans',
    2 : 'Amharic',
    3 : 'Chichewa',
    4 : 'Hangul',
    5 : 'Hausa',
    6 : 'Igbo', 
    7 : 'Malagasy',
    8 : 'Sesotho', 
    9 : 'Shona', 
    10 : 'Somali',
    11 : 'Swahili', 
    12 : 'xhosa',
    13 : 'Yoruba', 
    14 : 'Zulu',
    15 : 'Exit'
}


def keep_translating(lang_chose, exitcode):
    if exitcode == 0:
        return 0
    else:
        lang = lan_supported[lang_chose]
        word = str(input(f"Enter an English word to translate to {lang}: "))
        result = translate_lang(word, lang_chose)
        print(f"""
              '{word}' in '{lang}' is: {result.text} \n
        """)
        exitcode =  int(input(
            """
            Press 0 exit 
            Press 1 to use another word : """))
        return keep_translating(lang_chose, exitcode)


print(
    '''
    Hello, Welcome to African-Lingo
    we Have Created a Data set of many African Languages and we love to help you
    translate your English Words to the African Native Language of your choice  
    '''
)

name = input("To get Started, Please Tell us your name: ")




choice = int(input(f'''
    Welcome {name}
    Please Choose a language of your choice to get started.
    
    Please Make a choice to continue the program 
    1 : To continue  
    2 : To Exit() the program 
    
    Choose a number(1 / 2) : '''))

def Main():
    lang_chose = int(input(f'''
        In order to choose a language, Just Choose the language number (eg. 1)
        {
            json.dumps(lan_supported, indent=8, sort_keys=True)
        }
        
        Please choose the language you want : '''))
    lang = lan_supported[lang_chose]
    if lang_chose == 15:
        return 0
    else:
        result = keep_translating(lang_chose, 1)
        if result == 0:
            return Main()


Main()