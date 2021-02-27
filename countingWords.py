def openingFiles():
    fileName = input("Enter the file name:")
    opening = open(fileName)

    wordCount = 0

    for line in opening:
        words = line.split()
        wordCount=wordCount+len(words)
    print(words)
    print(wordCount)

openingFiles()

