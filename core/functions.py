import json, os
from fuzzywuzzy import fuzz


basepath = os.path.dirname(__file__)
listspath = os.path.join(basepath,"..","lists\\")

def load_words(filename):#nome do arquivo, com sua extensão
    try:
        filepath = (os.path.join(basepath,"..","dicts\\", filename))
        with open(filepath,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

def separate(dictionary):
    for word in dictionary:
        filename = str(len(word))+" words.txt"
        try:
            with open(listspath+filename,'a+') as f:
                f.write(word+"\n")
        except Exception as e:
            return str(e)

def test(word):
    filename = str(len(word)) + " words.txt"
    maiorRatio = 0
    bestMatch = ""
    try:
        with open(listspath + filename, 'r') as f:
            for line in f:
                ratio = fuzz.ratio(word,line)
                if (ratio > maiorRatio):
                    bestMatch = [line,ratio]
            print(bestMatch)
    except Exception as e:
        return str(e)

#TO GENERATE THE LISTS BY NUMBER OF WORDS
#separate(load_words("english_dict.json"))

test("aaaaaa")
