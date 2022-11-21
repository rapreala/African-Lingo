from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Xhosa: "))
result = translator.translate(text=word, dest='xh')
print(f"{word} in Xhosa is: {result.text}")