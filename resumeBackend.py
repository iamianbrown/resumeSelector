import re
import pdfminer.high_level
import pprint
from datetime import date
res = '/Users/ian/Documents/Personal/Employment/Resumes/Resume 11:20:2020.pdf'

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

#digest a text input into a keyword dictionary
def digest(text): #resume is a pdf file (as str)
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

    #add subwords in symbol-containing words to dictionary
    newWords = {}
    for word in words.keys():
        newWords[word] = words[word]
        subWords = re.split(r'\W', word)
        if len(subWords) > 1:
            print(subWords)
        for subWord in subWords:
            if subWord in words: #increment if already in words
                newWords[subWord] += 1
            else: #otherwise create new entru
                newWords[subWord] = 1
    words = newWords

    #remove all short/empty words and propositions from dictionary
    commonWords = set(['of','in','to','for','with','on','at','from','by','about','as','into','like','through',\
        'after','over','between','out','against','during','without','before','under','around','among','as','if',\
            'than','that','though','so','and','or','nor','but','yet', 'may', 'the','how','then','my','while','good',\
                 'st','ave','blvd','way','not','an','within','up'])
    newWords = {} #reset newWords
    for word in words.keys():
        if len(word) >= 2 and word not in commonWords:
            newWords[word] = words[word]
    words = newWords
    return words

#adds a new resume into database
def addResume(resumePDF):
    resumeWords = digest(pdfminer.high_level.extract_text(resumePDF))
    nameRegex = re.compile(r'([^\/^]+)(.pdf)') #gets everything after last / upto file type
    #inside of [], ^<character> means not the following
    resumeName = nameRegex.search(resumePDF)
    name = resumeName.group(1)
    
    resumeEntry = {'Name':name, 'Date Added':str(date.today()), 'Content':str(resumeWords)}
    resumes = open(r'digestedResumes.txt', 'a')
    resumes.write(str(resumeEntry) + '\n')
    resumes.close()

    #pickle resumeWords and store (should be stored in one file as a dictionary
    #with keynames the same as resume filenames)

#finds the resume with the highest number of keyword hits

#reads the file where the resume keyword dictionaries are stored
def getResumes(resumeFile):
    resumeDict = {} #name-indexed dictionary of dictionaries (subdictionaries include date added and content)
    nameRegex = re.compile(r'\'Name:\'\s+\'(.+)\',')
    dateRegex = re.compile(r'\'Date Added:\'\s+\'(.+)\',')
    with open('digestedResumes.txt', 'r') as f:
        resumes = f.readlines()
        for line in resumes:
            search = nameRegex.search(line) #find name of resume
            name = search.group(1)
            search = dateRegex.search(line) #find date resume was added
            dateAdded = search.group(1)
            content = extractContent(line)
            #resumeDict[name] = #date, content

def extractContent(resumeEntry):
    content = {}
    contentRegex = re.compile(r'\'Content:\'\s+\'(.+)\',')
    #contentRegex = re.compile
'''
def findBestResume(description):
    descriptionWords = digest(description)
    scores = {} #dictionary to keep track of how many same word instances there are for each resume
    for resume in resumeList:
        scores[resume] = 0
        for word in descriptionWords:
            if word in resume:
                scores[resume] += 1
    #return resume with highest score
'''
addResume(res)
