from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Arabic: "))
result = translator.translate(text=word, dest='ar')
print(f"{word} in Arabic is: {result.text}")