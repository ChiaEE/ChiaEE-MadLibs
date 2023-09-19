import random

##Madlib File
Text = "MadLib Sentences.txt"

def MadLibsFile(File,Sent):
    '''Splits up MadLib File line by line and appends them to the Sentences list'''
    madLib = open(File,"r")
    for line in madLib:
        SentList = line.split("\n")
        Name = SentList[0]
        Sent.append(Name)
    return Sent

##List of Sentences from MadLib File        
Sentences = []
##Calls the MadLibsFile function and appends each sentence from file to Sentences list
SentenceList = MadLibsFile(Text,Sentences)

def computerWants(AList):
    '''Takes list of Madlib Phrases and chooses one randomly'''
    AutoMove=random.choice(AList)
    return AutoMove

def PromptList(AutoPick):
    '''Takes the Random Choice of Sentence and returns a list of the words in the brackets that will be replaced'''
    Replace = []
    AutoPick=AutoPick.replace('>','>,')
    AutoList = AutoPick.split(',')
    for word in AutoList:
        if '>' in word:
            begin = word.find('<')+1
            end = word.find('>')
            phrase = word[begin:end]
            Replace.append(phrase)
    return Replace

    
def PromptChange(AutoPick,ProList):
    '''Takes the Random Choice of sentence and the list of words in brackets to make a dictionary
    where the list is the keys and user's input is the value.
    Replaces the word if it matches the dictionary keys with the key's value and returns the new sentence.'''
    MadLibsDict = dict.fromkeys(ProList,'')
    for item in ProList:
        for key,value in MadLibsDict.items():
            value = input("Enter a(n)"+" "+key+":"+" ")
            MadLibsDict[key]=value
            if key in AutoPick:
                AutoPick = AutoPick.replace(key,value)
        return AutoPick
        
        
##Calls the computerWants function so it can randomly choose a sentence from the list.
Choice=computerWants(Sentences)

##Calls the PromptList Function to return a list of the words that will be replaced
ListToReplace = PromptList(Choice)

##Returns the MadLib with the user's input
NewMadlib = PromptChange(Choice,ListToReplace)
print(NewMadlib)

    

    
    
