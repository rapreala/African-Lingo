from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to sudanese: "))
result = translator.translate(text=word, dest='su')
print(f"{word} in Sudanese is: {result.text}")