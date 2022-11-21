from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Yoruba: "))
result = translator.translate(text=word, dest='yo')
print(f"{word} in Yoruba is: {result.text}")