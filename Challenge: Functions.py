def most_frequent(word):
    mydict={}
    for letter in word:
        if letter in mydict.keys():
            #print("executed for " + letter)
            mydict[letter]=mydict[letter]+1
        else:
            mydict[letter]=1
    print(mydict)
        #print(mydict[a])
word=input("Please enter the word: ")
most_frequent(word)
