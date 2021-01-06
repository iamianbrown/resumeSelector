import re
import pdfminer.high_level
import pprint
import json
from datetime import date
import os
from shutil import copy
resume1 = '/Users/ian/Documents/Personal/Employment/Resumes/Resume 8:22:2020.pdf'
resume2 = '/Users/ian/Documents/Personal/Employment/Resumes/20201204 Resume.pdf'

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

def startup():
    abspath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(abspath))
    pdfFolder = r'resumePDFs'
    if not os.path.exists(pdfFolder):
        os.mkdir(pdfFolder)

#digest a text input into a keyword dictionary
def digestResume(resumePDF): #resume is a pdf file (as str)
    text = pdfminer.high_level.extract_text(resumePDF)
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
        for subWord in subWords:
            if '\\' not in subWord:
                if subWord in newWords: #increment if already in newWords
                    newWords[subWord] += 1
                else: #otherwise create new entry
                    newWords[subWord] = 1
    words = newWords

    #remove all short/empty words and propositions from dictionary
    commonWords = set(['of','in','to','for','with','on','at','from','by','about','as','into','like','through',\
        'after','over','between','out','against','during','without','before','under','around','among','as','if',\
            'than','that','though','so','and','or','nor','but','yet', 'may', 'the','how','then','my','while','good',\
                 'st','ave','blvd','way','not','an','within','up','will'])
    newWords = {} #reset newWords
    for word in words.keys():
        if len(word) >= 2 and word not in commonWords:
            newWords[word] = words[word]
    words = newWords
    return words

#get job description (input as plain text) word count
def digestDescription(text): 
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
        for subWord in subWords:
            if subWord in newWords: #increment if already in words
                newWords[subWord] += 1
            else: #otherwise create new entru
                newWords[subWord] = 1
    words = newWords

    #remove all short/empty words and propositions from dictionary
    commonWords = set(['of','in','to','for','with','on','at','from','by','about','as','into','like','through',\
        'after','over','between','out','against','during','without','before','under','around','among','as','if',\
            'than','that','though','so','and','or','nor','but','yet', 'may', 'the','how','then','my','while','good',\
                 'st','ave','blvd','way','not','an','within','up','com','will'])
    newWords = {} #reset newWords
    for word in words.keys():
        if len(word) >= 2 and word not in commonWords:
            newWords[word] = words[word]
    words = newWords
    return words

#adds a new resume into database (returns true if successful)
#returns false if resume with duplicate name already exists
def addResume(resumePDF):
    #change directory to resumePDFs
    abspath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(abspath) + '/resumePDFs')
    #get filename from resumePDF
    nameRegex = re.compile(r'([^\/]+)(.pdf)') #gets everything after last / upto file type
    #inside of [], ^<character> means not the following
    name = nameRegex.search(resumePDF)
    filename = name.group(1) + name.group(2)
    #copy resume pdf to be stored in app
    print(os.getcwd())
    copy(resumePDF, filename)
    #return to parent directory, where digestedResumes.json is stored
    os.chdir('/..')
    print(os.getcwd())
    #write resume to file (if there exist no duplicates), returns False if resume is a duplicate
    resumeFile = r'digestedResumes.json'
    resumes = []
    if os.path.exists(resumeFile):
        resumes = getResumes()
        if not any(res['Name'] == filename for res in resumes): #check that resume not already in file
            #convert resume pdf into json with digested word count and add
            resumeWords = digestResume(resumePDF)
            entry = {'Name':filename, 'Date Added':str(date.today()), 'Location': os.getcwd() + '/resumePDFs/' + filename, 'Content':resumeWords}
            resumes.append(entry)
        else: #return false if resume with that name already exists
            return False
    else: #if file is empty, simply write resume
        #convert resume pdf into json with digested word count
        resumeWords = digestResume(resumePDF)
        entry = {'Name':filename, 'Date Added':str(date.today()), 'Location': 'resumePDFs/' + filename, 'Content':resumeWords}
        resumes.append(entry)
    with open(resumeFile, 'w') as f:
        out = json.dumps(resumes)
        f.write(out)
        return True

#opens and reads stored resume data
def getResumes():
    #change directory to script's directory
    abspath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(abspath))
    with open(r'digestedResumes.json', 'r') as f:
            fileContent = f.read()
            resumes = json.loads(fileContent)
    return resumes

#deletes a resume with a given name, if it exists
def delResume(resumeName): #takes resume as name with .pdf extension
    #change directory to resumePDFs
    abspath = os.path.abspath(__file__)
    os.chdir(os.path.dirname(abspath) + '/resumePDFs')
    print(os.getcwd())
    resumeFile = r'digestedResumes.json'
    resumes = getResumes()
    for resume in resumes:
        if resume['Name'] == resumeName: #if resume has name that matches input, remove it from the list
            resumes = [resume for resume in resumes if resume['Name'] != resumeName]
            content = json.dumps(resumes)
            with open(resumeFile, 'w') as f:
                f.write(content)
            os.remove(resume['Location'])
            return True  #returns true if resume was successfully deleted
        else:
            return False #returns false if there is no resume with matching name

#deletes resume with name resumeToDeleteName and replaces it with data from replacement (replacement is pdf)
def replaceResume(resumeToDeleteName, replacement):
    delResume(resumeToDeleteName)
    addResume(replacement)

def findBestResume(description):
    descriptionWords = digestDescription(description)
    scores = [] #list containing dict for each resume with name and score
    resumes = getResumes()
    for res in resumes:
        score = 0
        for word in descriptionWords:
            if word in res['Content']:
                score += 1
                print(word)
        pprint.pprint(res['Content'])
        scores.append({'Name':res['Name'],'Score':score})
    maximum = 0
    for elem in scores:
        if elem['Score'] > maximum:
            maximum = elem['Score']
            bestResume = elem['Name']
    for res in resumes:
        if res['Name'] == bestResume:
            return res['Location']



