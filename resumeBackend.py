import re
import pdfminer.high_level

res = '/Users/ian/Documents/Personal/Employment/Resumes/Resume 10:7:2020.pdf'

def stripSymbols(word):#remove symbols from ends of words
    regexPattern = re.compile(r'^[\W_]+') 
    newWord = regexPattern.sub('', word) #remove symbols from beginning
    regexPattern = re.compile(r'[\W_]+$') 
    newWord = regexPattern.sub('', newWord) #remove symbols from end
    return newWord


#serialization
#library pickle (not 3rd party) can handle dicts
#numpy library numeric calculation library for python—good at arrays (can add, do cool stuff element by element, find big stuff)
#has own way to store things in files
#could use array indices to represent each word
#(fix order of words)
#could use plain text or json file (json can be read by anything)
#could use library that finds similar words

#digest job description
def digestResume(resume): #resume is a pdf file (as str)
    text = pdfminer.high_level.extract_text(resume)
    text = text.lower() #make search case insensitive
    textLst = text.split() #parse resume into list
    words = {} #dictionary where word count will be stored

    #count number of instances of each word and strip symbols off of them
    #make symbol-only words empty
    newWords = {} #new dictionary to hold updated keys
    for word in textLst:
        if stripSymbols(word) in newWords.keys():
            newWords[stripSymbols(word)] += 1
        else:
            newWords[stripSymbols(word)] = 1
    words = newWords

   #make all number-symbol words empty
    newWords = {} #reset newWords
    numRegex = re.compile(r'^[\W_\d]+$') #selects all number-symbol words
    for word in words.keys():
       newWords[numRegex.sub('', word)] = words[word]
    words = newWords

    #remove all short/empty words from dictionary
    newWords = {} #reset newWords
    for word in words.keys():
        if len(word) >= 2:
            newWords[word] = words[word]
    words = newWords
    #set data structure for non-pertitent words
    return words

print(digestResume(res))
