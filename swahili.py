from googletrans import Translator
translator = Translator()
word = str(input("Enter an English word to translate to swahili: "))
result = translator.translate(word, dest='sw')
print(word, "in Swahili is: ",result.text)