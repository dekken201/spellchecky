from core.functions import *
import cProfile, os, pickle

#LOADS THE JSON DICTIONARY, CREATES A TREE, ADDS THE DICTIONARY TO THE TREE, AND DUMPS IT INTO A PICLE OBJECT
#pickle_dump(BKTree(load_words("english_dict")),"english_dict_pickle")

tree = pickle_load("english_dict_pickle")
print(tree.find("airplane", 1))


