from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Amharic: "))
result = translator.translate(text=word, dest='am')
print(f"{word} in Amharic is: {result.text}")