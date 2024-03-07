text = "abcdefghijklmnop"

print(dir(text))
help(text.isupper)
print(text.isupper())
print("ABC".isupper())
print(text.upper())
print(text.upper().isupper())

new_text = text.upper()
print(text, new_text)
print("bannannnnaa".count("n"))
print("bannnananaan".index("b"))
print("bananabananabanana".replace("ana", "XXYZZ"))

sentance = "Hello, how many! I be of service today?"
punctuation = ".,;!?-"
for p in punctuation:
    sentance = sentance.replace(p, "")
print(sentance)