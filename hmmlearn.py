import sys
import os
import fnmatch

def probalisticdetermination(hash1,l,hash2,hash3):
    fileop = open("hmmmodel.txt","w")
    count = len(l)
    tagcount =0
    wordemmisioncount =0
    for keys in hash1:
        for tag in hash1[keys]:
            tagcount += hash1[keys][tag]
        hash1[keys]["denominator"]={}
        hash1[keys]["denominator"] = tagcount+count
        tagcount=0
    fileop.write("transition" + "\n")
    for keys in hash1:
        for tag in hash1[keys]:
            if (tag != "denominator"):
                hash1[keys][tag] = (hash1[keys][tag]+1)*1.0/(hash1[keys]["denominator"])
                stringtransitionprobability = keys + ' '+tag+' '+str(hash1[keys][tag])
                fileop.write(stringtransitionprobability+'\n')
    
    fileop.write("Emmission"+ "\n")
    for keys in hash2:
        for tag in hash2[keys]:
            if (tag != "count"):
                hash2[keys][tag] = (hash2[keys][tag])*1.0 / (hash3[tag])
                stringemmisionprobability = keys +' '+tag+' '+str(hash2[keys][tag])
                fileop.write(stringemmisionprobability+'\n')
    fileop.write("Taglist"+"\n")
    for tags in l:
        fileop.write(tags)
        fileop.write("\n")
    fileop.close()
    
    
def hiddenmarkovlearn(filename,hash1,hash2,hash3):
    l = list()
    for sentences in filename:
        words = sentences.split()
        previoustag = "start"
        for word in words:
            tag = word.rsplit("/",1)
            if previoustag in hash1:
                if(tag[1] in hash1[previoustag]):
                    hash1[previoustag][tag[1]]= hash1[previoustag][tag[1]]+1
                else:
                    hash1[previoustag][tag[1]]= 1
            else:
                hash1[previoustag]={}
                hash1[previoustag][tag[1]]={}
                hash1[previoustag][tag[1]] = 1
            previoustag = tag[1]
            if tag[0] in hash2:
                if(tag[1] in hash2[tag[0]]):
                    hash2[tag[0]][tag[1]]= hash2[tag[0]][tag[1]]+1
                else:
                    hash2[tag[0]][tag[1]]= 1
            else:
                hash2[tag[0]]={}
                hash2[tag[0]][tag[1]] ={}
                hash2[tag[0]][tag[1]] = 1
                
            if tag[1] in hash3:
                hash3[tag[1]] = hash3[tag[1]]+1
            else:
                hash3[tag[1]] ={}
                hash3[tag[1]] = 1
            
            if tag[1] not in l:
                l.append(tag[1])

        for tag in l:
            for keys in hash1:
                if tag not in hash1[keys]:
                    hash1[keys][tag] = {}
                    hash1[keys][tag] = 0
    probalisticdetermination(hash1,l,hash2,hash3)   
        
        
def read_training_file(training_file):
    hash1 ={}
    hash2 ={}
    hash3 ={}
    fileop = open(training_file,"r")
    hiddenmarkovlearn(fileop,hash1,hash2,hash3)
    
training_file = sys.argv[1]
read_training_file(training_file)
