intro = input("Enter your introduction:")
print(intro)

characterCount=0
wordCount=1

for i in intro:
    characterCount=characterCount+1
    print(i)
    if(i==' '):
        wordCount=wordCount+1
        
print(wordCount)
print(characterCount)