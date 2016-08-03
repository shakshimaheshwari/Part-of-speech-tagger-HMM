# Part-of-speech-tagger-HMM
The project aims at designing a Hidden Markov Model part-of-speech tagger using Viterbi Algorithm for Catalan. The training data is provided tokenized and tagged with the corresponding tags and the test data is provided tokenized and the script generates the tags for the same. **Laplace smoothing** is applied for smoothing of the data as well as handling the unknown vocabulary in the data.


#Pre-requisites
1. PyCharm recent version installed
2. Python 3.0 or above installed(recommended)


#Data

* A file tagged with traning data in the word/TAG format, with words seperated by spaces and each sentence on a new line.
* A line with untagged development data, with words seperated by spaces and each sentence on a new line
* A file with tagged development data in the word/TAG format, with words seperated by spaces and each sentence on a new line, to serve as an answer key

#Files Description

* **hmmlearn.py**:- The program will learn a Hidden Markov Model, and write the model parameters to the file called hmmmodel.txt
* **hmmdecode.py**:- The program will read the parameters of a Hidden Markov Model from hmmmodel.txt, tag each word in the test data, and write the results to a text file called hmmoutput.txt in the same format as the training data.


#Evaluation
For evaluation, train the model and then run the tagger on the unseen data and the accuracy of then compare the output to a reference annotation.


