from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Sesotho: "))
result = translator.translate(text=word, dest='st')
print(f"{word} in Sesotho is: {result.text}")