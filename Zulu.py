from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Zulu: "))
result = translator.translate(text=word, dest='zu')
print(f"{word} in Zulu is: {result.text}")