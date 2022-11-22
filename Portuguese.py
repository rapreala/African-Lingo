from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to portuguese: "))
result = translator.translate(text=word, dest='pt')
print(f"{word} in portuguese is: {result.text}")