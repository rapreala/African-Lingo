from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Hausa: "))
result = translator.translate(text=word, dest='ha')
print(f"{word} in Hausa is: {result.text}")
 