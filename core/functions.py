import json, os, pickle, Levenshtein



basepath = os.path.dirname(__file__)
listspath = os.path.join(basepath,"..","lists\\")

def distance_function(str1,str2):
    return Levenshtein.distance(str1,str2)

def load_words(filename):#nome do arquivo, sem extensão
    try:
        filepath = (os.path.join(basepath,"..","dicts\\", filename+".json"))
        with open(filepath,"r") as dictionary:
            words = json.load(dictionary)
            return words
    except Exception as e:
        return str(e)

def pickle_dump(tree, filename):
    try:
        filepath = (os.path.join(basepath,"..","dicts\\", filename+".txt"))
        with open(filepath, "wb") as pickling:
            pickle.dump(tree, pickling)
    except Exception as e:
        return str(e)


def pickle_load(filename):
    filepath = (os.path.join(basepath, "..", "dicts\\", filename + ".txt"))
    with open(filepath, "rb") as pickling:
        return pickle.load(pickling)