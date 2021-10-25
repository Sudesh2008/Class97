intro = input("Enter your introduction: ")
print(intro)

characterCount = 0
wordCount = 1

for i in intro:
    characterCount = characterCount + 1
#print(characterCount)
    if (i == " "):
        wordCount = wordCount + 1

print("number of words in the intro: ")
print(wordCount)

print("number of characters in the intro: ")
print(characterCount)



