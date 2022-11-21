from googletrans import Translator

hangul = Translator()

korean_hangul = str(input("Enter any korean/ Hangul word: "))
output = hangul.translate(text=korean_hangul, dest='kr')
print(f"{korean_hangul} in Korean is: {output.text}")
