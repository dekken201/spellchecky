from core.functions import *

#LOADS THE JSON DICTIONARY, CREATES A TREE, ADDS THE DICTIONARY TO THE TREE, AND DUMPS IT INTO A PICKLE OBJECT
#pickle_dump(BKTree(load_words("english_dict")),"english_dict_pickle")

def main():
    tree = pickle_load("english_dict_pickle")
    while True:
        user_input = input("Write the word you want spellchecked:")
        if user_input != "":
            print(tree.find(user_input, 1))
        else:
            break

main()