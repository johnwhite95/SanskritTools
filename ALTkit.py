import pandas as pd
pairs11 = [
           ["a", "a"], ["a", "i"], ["i", "ī"], ["i", "a"], 
           ["h", "s"], ["u", "u"], ["m", "s"], ["t", "j"],
           ["ṭ", "h"], ["n", "t"], ["a", "ḥ"], ["a", "aḥ"],
           ["a", "an"]
          ]
joins11 = [
           "ā", "e", "ī", "y a", 
           "kṣ", "ū", "ṃs", "j j",
           "ḍ ḍh", "ṃs t", "aḥ", "āḥ",
           "ān"
          ]
pairs21 = [
           ["au", "ā"]
          ]
joins21 = [
           "āv ā"
          ]
pairs22 = [
           ["dh", "dh"]
          ]
joins22 = [
           "ddh"
          ]

cases = ["Nom.", "Voc.", "Acc.", "Ins.", "Dat.", "Abl.", "Gen.", "Loc."]
singdec_ma = ["aḥ", "a", "am", "ena", "āya", "āt", "asya", "e"]
dualdec_ma = ["au", "au", "au", "ābhyām", "ābhyām", "ābhyām", "ayoḥ", "ayoḥ"]
plurdec_ma = ["āḥ", "āḥ", "ān", "aiḥ", "ebhyaḥ", "ebhyaḥ", "ānām", "eṣu"]

singdec_na = ["am", "a", "am", "ena", "āya", "āt", "asya", "e"]
dualdec_na = ["e", "e", "e", "ābhyām", "ābhyām", "ābhyām", "ayoḥ", "ayoḥ"]
plurdec_na = ["āni", "āni", "āni", "aiḥ", "ebyaḥ", "ebyaḥ", "ānām", "eṣu"]

persons = ["third", "second", "first"]
pres_ten_end = ["ati", "asi", "āmi", "-", "-", "āvaḥ", "anti", "-", "āmaḥ"]

def sandhi(x, y):
    check11 = [x[len(x)-1:], y[:1]]
    check21 = [x[len(x)-2:], y[:1]]
    check22 = [x[len(x)-2:], y[:2]]
    
    if check11 in pairs11:
        location = pairs11.index(check11)
        between = joins11[location]
        return(x[:len(x)-1]+between+y[1:])
    
    elif check21 in pairs21:
        location = pairs21.index(check21)
        between = joins21[location]
        return(x[:len(x)-2] + between + y[1:])
    
    elif check22 in pairs22:
        location = pairs22.index(check22)
        between = joins22[location]
        return(x[:len(x)-2] + between + y[2:])
    
    else:
        return(x + y)

def decline(noun, gender):
    stem_cut = noun[:len(noun)-1]
    stem = noun[len(noun)-1:]
    singular = []
    dual = []
    plural = []
    if stem == "a":
        if gender == "masc":
            for i in range(0, len(singdec_ma)):
                singular.append(sandhi(stem_cut, singdec_ma[i]))
                dual.append(sandhi(stem_cut, dualdec_ma[i]))
                plural.append(sandhi(stem_cut, plurdec_ma[i]))
        elif gender == "neut":
            for i in range(0, len(singdec_ma)):
                singular.append(stem_cut + singdec_na[i])
                dual.append(stem_cut + dualdec_na[i])
                plural.append(stem_cut + plurdec_na[i])
        finished = pd.DataFrame({'case':cases, 'singular':singular, 
                                 'dual':dual, 'plural':plural}).reindex(
                                ['case', 'singular', 'dual', 'plural'], axis=1)
    return(finished)

print(decline("vacana", "neut"))

def conjugate(verb):
    verb_cut = verb[:len(verb)-1]
    first = []
    second = []
    third = []
    for i in range(0, 3):
        first.append(verb_cut + pres_ten_end[i])
    for i in range(3, 6):
        second.append(verb_cut + pres_ten_end[i])
    for i in range(6, 9):
        third.append(verb_cut + pres_ten_end[i])
    finished = pd.DataFrame({'person':persons, 'first':first, 'second':second,
                            'third':third}).reindex(
                            ['person', 'first', 'second', 'third'], axis=1)
    return(finished)

conjugate("gaccha")


