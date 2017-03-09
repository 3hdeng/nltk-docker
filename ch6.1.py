import nltk 
from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
        [(name, 'female') for name in names.words('female.txt')])
print(labeled_names[:10])

import random
random.shuffle(labeled_names)
print(labeled_names[:10])


#========================
def gender_features(word):
     return {'last_letter': word[-1]}

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
#the first 500 (feature, gender) as test_set
#the remaining as train_set
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print('Neo',  classifier.classify(gender_features('Neo')) )
# 'male'

for i in range(ord('a'), ord('z')+1):
        print ( chr(i),end=',')

print('#==================')

a_z=[chr(i) for i in range(ord('a'), ord('z')+1) ]
for x in a_z:
    print( x, classifier.classify({'last_letter':x}) )


#===================
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)


#===============
"""
When working with large corpora, constructing a single list that contains the features of every instance can use up a large amount of memory. In these cases, use the function nltk.classify.apply_features, which returns an object that acts like a list but does not store all the feature sets in memory:
"""
        
from nltk.classify import apply_features
train_set = apply_features(gender_features, labeled_names[500:])
test_set = apply_features(gender_features, labeled_names[:500])

classifier = nltk.NaiveBayesClassifier.train(train_set)
print('Neo',  classifier.classify(gender_features('Neo')) )
print('accuracy', nltk.classify.accuracy(classifier, test_set))

#======== 6.1.2 ===========
def gender_features2(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

print( gender_features2('John')  )


#=================
featuresets = [(gender_features2(n), gender) for (n, gender) in labeled_names]
# train_set, test_set = featuresets[500:], featuresets[:500]
train_set = apply_features(gender_features2, labeled_names[500:])
test_set = apply_features(gender_features2, labeled_names[:500])
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))

#=======================
train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set) 
print(nltk.classify.accuracy(classifier, devtest_set))
# 0.75

"""
Using the dev-test set, we can generate a list of the errors that the classifier makes when predicting name genders:
"""
        
errors = []
for (name, tag) in devtest_names:
            guess = classifier.classify(gender_features(name))
            if guess != tag:
                 errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors):
     print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))


#===========
def gender_features(word):
     return {'suffix1': word[-1:],
             'suffix2': word[-2:]}

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, devtest_set))



#======= 1.3   Document Classification ==========
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
print("count of documents= ", len(documents) )

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

# to limit the number of features that the classifier needs to process, we begin by constructing a list of the 2000 most frequent words in the overall corpus

def document_features(document):
    document_words = set(document) 
    features = {}
    for word in word_features:
          features['contains({})'.format(word)] = (word in document_words)
    return features


print(document_features(movie_reviews.words('pos/cv957_8737.txt'))) 

