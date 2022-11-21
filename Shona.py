from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Shona: "))
result = translator.translate(text=word, dest='sn')
print(f"{word} in Shona is: {result.text}")