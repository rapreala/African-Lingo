from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to swahili: "))
result = translator.translate(text=word, dest='lg')
print(f"{word} in Swahili is: {result.text}")
