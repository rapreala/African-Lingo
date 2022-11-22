from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Somali: "))
result = translator.translate(text=word, dest='so')
print(f"{word} in Somali is: {result.text}")