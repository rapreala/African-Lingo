from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Malagasy: "))
result = translator.translate(text=word, dest='mg')
print(f"{word} in Malagasy is: {result.text}")