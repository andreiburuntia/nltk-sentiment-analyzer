import nltk
from nltk.classify import NaiveBayesClassifier

# nltk.download('punkt')

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})
 
pos = []
with open("./pos_tweets.txt") as f:
    for i in f: 
        pos.append([format_sentence(i), 'pos'])
 
neg = []
with open("./neg_tweets.txt") as f:
    for i in f: 
        neg.append([format_sentence(i.decode('utf-8')), 'neg'])
 
# next, split labeled data into the training and test data
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]

classifier = NaiveBayesClassifier.train(training)

print classifier.classify(format_sentence("Iran vows to restart nuclear program if deal collapses"))