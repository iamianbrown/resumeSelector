import re
import pdfminer.high_level

res = '/Users/ian/Documents/Personal/Employment/Resumes/Resume 10:7:2020.pdf'

def stripSymbols(word):#remove symbols from ends of words
    regexPattern = re.compile(r'^[\W_]+')#add end strip regex
    newWord = regexPattern.sub('', word)
    return newWord

def digestResume(resume): #resume is a pdf file (as str)
    text = pdfminer.high_level.extract_text(resume)
    text = text.lower() #make search case insensitive
    textLst = text.split() #parse resume into list
    words = {} #dictionary where word count will be stored

    #count number of instances of each word
    for word in textLst:
        if word.strip() in words.keys():
            words[word] += 1
        else:
            words[word] = 1
    
    #strip symbols from the ends of words (such as parentheses)
    newWords = {} #new dictionary to hold updated keys
    for word, number in words.items():
        newWords[stripSymbols(word)] = number
    words = newWords

    #remove all non-alphabetical words
    words = {word:number for word, number in words.items()\
         if word[0].isalpha() and word[len(word) - 1].isalpha()}#fix this

    return words

print(digestResume(res))
