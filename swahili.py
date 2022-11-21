from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to swahili: "))
<<<<<<< HEAD
result = translator.translate(text=word, dest='sw')
=======

result = translator.translate(text=word, dest='sw')

>>>>>>> d7a7fbf7d29eb12ab530d62fca9f43c63fef6be5
print(f"{word} in Swahili is: {result.text}")
