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

def checkRatio(str1, str2): #TESTA TODAS AS POSSIBILIDADES DE RATIO DO FUZZYWUZZY
    bestRatio = 0
    ratios = [fuzz.ratio(str1, str2), fuzz.partial_ratio(str1, str2), fuzz.token_sort_ratio(str1, str2),
              fuzz.token_set_ratio(str1, str2)]
    for ratio in ratios:
        if ratio > bestRatio:
            bestRatio = ratio
    return bestRatio

def test(user_input):
    input_size = len(user_input)
    best_ratio = 0
    english_words = load_words("english_dict.json")
    if user_input not in english_words:
        for word in english_words:
            if (len(word) > (input_size +1)) or (len(word) < (input_size-1)):
                pass
            else:
                ratio = checkRatio(user_input,word)
                if ratio > best_ratio:
                    print(word+"+"+str(ratio))
                    bestMatch = word
        print(bestMatch)


test("aiir")



