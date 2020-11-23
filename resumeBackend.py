import re
import pdfminer.high_level

print(pdfminer.__version__)
res = '/Users/ian/Documents/Personal/Employment/Resumes/Resume 10:7:2020.pdf'
def digestResume(resume): #resume is a pdf file (as str)
    text = pdfminer.high_level.extract_text(resume)
    return text

def digest(textStr):
    textLst = textStr.split()
    words = {}
    for word in textLst:
        if word.strip() in words.keys():
            words[word] += 1
        else:
            words.setdefault(word, 1)
    newWords = {}
    regexPattern = re.compile(r'[\W_]+')
    for word in words.keys():
        #print(word, end='')
        newWord = regexPattern.sub('', word)
        if word.isalpha():
            newWords[newWord] = words[word]
        #print(word)
    words = newWords
    return words

print(digest(digestResume(res)))
