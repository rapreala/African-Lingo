from googletrans import Translator

translator = Translator()

word = str(input("Enter an English word to translate to Afrikaans: "))
result = translator.translate(text=word, dest='af')
print(f"{word} in Afrikaans is: {result.text}")