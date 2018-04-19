import json
import os

basepath = os.path.dirname(__file__)

def load_words(filename):#nome do arquivo, com sua extensão
    try:
        filepath = (os.path.join(basepath,"..","dicts\\", filename))
        with open(filepath,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)


english_words = load_words("english_dict.json")
print(english_words["fate"])