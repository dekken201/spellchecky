from core.functions import *
import cProfile, os, pickle, Levenshtein, distance


def test():
    for i in range(0,1000000):
        print(Levenshtein.distance("everything","doesnotmatter"))

def test2():
    for i in range(0,1000000):
        print(distance.levenshtein("everything","doesnotmatter"))

def test3():
    tree = pickle_load("english_dict_pickle")
    print(tree.find("zero", 1))

cProfile.run('test3()')




#TESTING WITHOUT TREE
#import distance
#test = load_words("english_dict")
#for word in test:
#    if distance.levenshtein(word,"zero") <= 1:
#        print(word)