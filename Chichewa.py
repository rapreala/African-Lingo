from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Chichewa: "))
result = translator.translate(text=word, dest='ny')
print(f"{word} in Chichewa is: {result.text}")