import sys
import os
import string
import fnmatch
import math

def readFileData(hash1,hash2,l):
    fileop = open("hmmmodel.txt","r")
    isTransition = False
    isEmission = False
    isTag = False
    for line in fileop:
        if("transition" in line):
            isTransition = True
            isEmission = False
            isTag = False
        if("Emmission" in line):
            isTransition = False
            isEmission = True
            isTag = False
        if("Taglist" in line):
            isTransition = False
            isEmission = False
            isTag = True
        if(isTransition):
            parts = line.split()
            if "transition" in parts[0]:
                continue
            elif parts[0] not in hash1:
                hash1[parts[0]] = {}
                hash1[parts[0]][parts[1]] = {}
                hash1[parts[0]][parts[1]] = parts[2]
            else:
                hash1[parts[0]][parts[1]] = parts[2]
        
        if(isEmission):
            parts = line.split()
            if("Emmission" in parts[0]):
                continue
            elif parts[0] not in hash2:
                hash2[parts[0]] = {}
                hash2[parts[0]][parts[1]]={}
                hash2[parts[0]][parts[1]] = parts[2]
            else:
                hash2[parts[0]][parts[1]] = parts[2]

        if(isTag):
            parts = line.split()
            if("Taglist" in parts[0]):
                continue
            elif parts[0] not in l:
                l.append(parts[0])
    fileop.close()       
def classifyFile(fileptr, hash1, hash2,l,filewr):
    start ="start"
    for sentences in fileptr:
        outputstructure =[{}]
        words = sentences.split()
        if(words[0] in hash2):
            for keys in hash2[words[0]]:
                outputvalue = float(hash1[start][keys]) * float(hash2[words[0]][keys])
                outputstructure[0][keys] = {}
                outputstructure[0][keys]['value'] = outputvalue
                outputstructure[0][keys]['previous'] = start
        else:
            for keys in l:
                outputvalue = hash1[start][keys]
                outputstructure[0][keys]={}
                outputstructure[0][keys]['value'] = outputvalue
                outputstructure[0][keys]['previous'] = start
        wordsafterzero = sentences.split()[1:]
        word =1
        for actualword in wordsafterzero:
            outputstructure.append({})
            if(actualword in hash2):
                for key in hash2[actualword]:
                    maximumvalue = -float('inf')
                    for tag in outputstructure[word-1]:
                        outputvalue = float(outputstructure[word-1][tag]['value'])*float(hash1[tag][key])*float(hash2[actualword][key])
                        if (maximumvalue < outputvalue):
                            maximumvalue =outputvalue
                            previoustag = tag
                        outputstructure[word][key]={}
                        outputstructure[word][key]['value'] = maximumvalue
                        outputstructure[word][key]['previous'] = previoustag
        
            else:
                for key in l:
                    maximumvalue = -float('inf')
                    for tag in outputstructure[word-1]:
                            outputvalue = float(outputstructure[word-1][tag]['value'])*float(hash1[tag][key])
                            if(maximumvalue < outputvalue):
                                maximumvalue = outputvalue
                                previoustag = tag
                    outputstructure[word][key] ={}
                    outputstructure[word][key]['value'] = maximumvalue
                    outputstructure[word][key]['previous'] = previoustag
            word = word+1
        tempmain = -float('inf')
        for previous in outputstructure[len(wordsafterzero)]:
            tempmax = outputstructure[len(wordsafterzero)][previous]['value']
            if(tempmax>tempmain):
                tempmain = tempmax
                maintag = previous
        previoustag = outputstructure[len(wordsafterzero)][maintag]['previous']
        stringtodisplay = words[len(wordsafterzero)]+'/'+maintag

        j = len(wordsafterzero)-1
        while(j>=0):
            stringtodisplay = words[j]+'/'+previoustag+' '+stringtodisplay
            previoustag = outputstructure[j][previoustag]['previous']
            j = j-1
        filewr.write(stringtodisplay+"\n")
    filewr.close()
            
def read_development_file(training_file):
    hash1 ={}
    hash2 ={}
    l =list()
    filewr = open("hmmoutput.txt","w")
    readFileData(hash1,hash2,l)
    fileop = open(training_file,"r")
    classifyFile(fileop,hash1,hash2,l,filewr)
    
filename = sys.argv[1]
read_development_file(filename)
