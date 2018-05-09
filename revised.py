
# coding: utf-8

# In[482]:


import pandas as pd

D_vowel = [
    "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ",
    "औ", "ऋ", "ॠ", "ऌ", "ॡ", "ं", "ः"
]
R_vowel = [
    "a", "ā", "i", "ī", "u", "ū", "e", "ai", "o",
    "au", "ṛ", "ṝ", "ḷ", "ḹ", "aṃ", "ḥ"
]

dia_d = [
    " ", "ि", "ु", "ॢ"
]

dia_r = [
    "a", "i", "u", "ḷ"
]

D_cons = [
    "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ",
    "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द",
    "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र",
    "ल", "व", "श", "ष", "स", "ह"
]
R_cons = [
    "k", "kh", "g", "gh", "ṅ", "c", "ch",
    "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh",
    "ṇ", "t", "th", "d", "dh", "n", "p",
    "ph", "b", "bh", "m", "y", "r", "l",
    "v", "ś", "ṣ", "s", "h"
]

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

cases = ["Nom.", "Voc.", "Acc.", "Ins.", "Dat.", "Abl.", 
         "Gen.", "Loc."]

singdec_ma = ["aḥ", "a", "am", "ena", "āya", "āt", "asya", "e"]
dualdec_ma = ["au", "au", "au", "ābhyām", "ābhyām", "ābhyām", "ayoḥ", "ayoḥ"]
plurdec_ma = ["āḥ", "āḥ", "ān", "aiḥ", "ebhyaḥ", "ebhyaḥ", 
              "ānām", "eṣu"]
singdec_na = ["am", "a", "am", "ena", "āya", "āt", "asya", "e"]
dualdec_na = ["e", "e", "e", "ābhyām", "ābhyām", "ābhyām", 
              "ayoḥ", "ayoḥ"]
plurdec_na = ["āni", "āni", "āni", "aiḥ", "ebyaḥ", "ebyaḥ", 
              "ānām", "eṣu"]

singdec_mi = ["is", "e", "im", "inā", "aye", "es", "es", "au"]
dualdec_mi = ["ī", "ī", "ī", "ibhyām", "ibhyām", "ibhyām", 
              "yos", "yos"]
plurdec_mi = ["ayas", "ayas", "īn", "ibhis", "ibhyas", 
              "ibhyas", "īnām", "iṣu"]
singdec_ni = ["i", "i/-e", "i", "iṇā", "iṇe", "iṇas", "iṇas", "iṇi"]
dualdec_ni = ["iṇī", "iṇī", "iṇī", "ibhyām", "ibhyām", 
              "ibhyām", "iṇnos", "iṇnos"]
plurdec_ni = ["īṇī", "īṇī", "īṇī", "ibhis", "ibhyas", 
              "ibhyas", "īṇām", "iṣu"]
singdec_fi = ["is", "e", "im", "yā", "aye", "es", "es", "au"]
dualdec_fi = ["ī", "i", "ī", "ibhyām", "ibhyām", "ibhyām", 
              "yos", "yos"]
plurdec_fi = ["ayas", "aya", "is", "ibhis", "ibhyas", 
              "ibhyas", "īnām", "iṣu"]

ma_dec = [singdec_ma, dualdec_ma, plurdec_ma]
na_dec = [singdec_na, dualdec_na, plurdec_na]
mi_dec = [singdec_mi, dualdec_mi, plurdec_mi]
ni_dec = [singdec_ni, dualdec_ni, plurdec_ni]
fi_dec = [singdec_fi, dualdec_fi, plurdec_fi]

relationship_nouns = ["pitṛ", "matṛ"]

persons = ["third", "second", "first"]
pres_ten_end = ["ati", "asi", "āmi", "-", "-", "āvaḥ", 
                "anti", "-", "āmaḥ"]


# In[430]:


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


# In[431]:


def list_declen(without_stem, declist):
    singular = []
    dual = []
    plural = []
    for i in range(0, 8):
        singular.append(without_stem + declist[0][i])
        dual.append(without_stem + declist[1][i])
        plural.append(without_stem + declist[2][i])
    finished = pd.DataFrame({'case':cases, 'singular':singular, 
                             'dual':dual, 'plural':plural}).reindex(
                            ['case', 'singular', 'dual', 'plural'], axis=1)  
    return(finished)


# In[432]:


def decline(noun, gender):
    stem_cut = noun[:len(noun)-1]
    stem = noun[len(noun)-1:]
    if stem == "a":
        if gender == "masc":
            output = list_declen(stem_cut, ma_dec)
        elif gender == "neut":
            output = list_declen(stem_cut, na_dec)
    elif stem == "i":
        if gender == "masc":
            output = list_declen(stem_cut, mi_dec)
        elif gender == "neut":
            output = list_declen(stem_cut, ni_dec)
        elif gender == "fem":
            output = list_declen(stem_cut, fi_dec)
    elif stem == "ṛ":
        output = "blah"
    else:
        output = "noun not recognized"
    return(output)


# In[433]:


decline("phala", "neut")


# In[434]:


def pronouns(gender):
    persons = ["third", "second", "first", "interr"]
    if gender == "masc":
        first = ['sa/saḥ', 'tvam', 'aham', 'kaḥ']
        second = ['tam', 'tvām', 'mām', 'kam']
        third = ['tam', 'tvām', 'mām', 'kam']
        finished_sing = pd.DataFrame({'person':persons, 'nom':first, 'voc':second,
                                'acc':third}).reindex(
                                ['person', 'nom', 'voc', 'acc'], axis=1)
    elif gender == "neut":
        first = ['tat', 'tvam', 'aham', 'kim']
        second = ['tat', 'tvām', 'mām', 'kim']
        third = ['tat', 'tvām', 'mām', 'kim']
        finished_sing = pd.DataFrame({'person':persons, 'nom':first, 'voc':second,
                                'acc':third}).reindex(
                                ['person', 'nom', 'voc', 'acc'], axis=1)  
        
    return(finished_sing)


# In[435]:


pronouns("neut")


# In[436]:


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


# In[437]:


"""maybe include an option for clusters"""
def devanagari(kind):
    if kind == "vowels":
        finished_sing = pd.DataFrame({'D_vowel':D_vowel, 'R_vowel':R_vowel}).reindex(
                                ['D_vowel', 'R_vowel'], axis=1)
        return(finished_sing)

    elif kind == "consonants":
        finished_sing = pd.DataFrame({'D_cons':D_cons, 'R_cons':R_cons}).reindex(
                                ['D_cons', 'R_cons'], axis=1)
        return(finished_sing)
    else:
        return("error: invalid argument")


# In[438]:


devanagari("vowels")


# In[483]:


def romanize(text):
    out = []
    dev = D_vowel + D_cons + dia_d
    rom = R_vowel + R_cons + dia_r
    for i in range(0, len(text)):
        location = text[i]
        out.append(rom[dev.index(text[i])])
    return(''.join(str(x) for x in out))


# In[485]:


romanize("प")

