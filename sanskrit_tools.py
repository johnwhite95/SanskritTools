import pandas as pd

D_vowel = [
    " ", "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ",
    "औ", "ऋ", "ॠ", "ऌ", "ॡ", "ं", "ः"
]
R_vowel = [
    " ", "a", "ā", "i", "ī", "u", "ū", "e", "ai", "o",
    "au", "ṛ", "ṝ", "ḷ", "ḹ", "aṃ", "ḥ"
]

dia_d = [
    "ा", "ी", "ि", "ु", "ू", "ृ", "ॄ", "ॢ", "ॣ", "े", "ै", "ो", "ौ", "्"
]

dia_r = [
    "ā", "ī", "i", "u", "ū", "r", "ṛ", "ḷ", "ḹ", "e", "ai", "o", "au", ""
]

D_cons = [
    "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ",
    "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द",
    "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र",
    "ल", "व", "श", "ष", "स", "ह"
]

R_cons = [
    "ka", "kha", "ga", "gha", "ṅa", "ca", "cha",
    "ja", "jha", "ña", "ṭa", "ṭha", "ḍa", "ḍha",
    "ṇa", "ta", "tha", "da", "dha", "na", "pa",
    "pha", "ba", "bha", "ma", "ya", "ra", "la",
    "va", "śa", "ṣa", "sa", "ha"
]

R_cons_na = [
    "k", "kh", "g", "gh", "ṅ", "c", "ch",
    "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh",
    "ṇ", "t", "th", "d", "dh", "n", "p",
    "ph", "b", "bh", "m", "y", "r", "l",
    "v", "ś", "ṣ", "s", "h"
]

# combine all devanagari characters and diacritics
all_d = D_cons + D_vowel + dia_d
# combine romanizations of all devanagari characters and diacritics
all_r = R_cons + R_vowel + dia_r
# combine romanizations of all devanagari characters and diacritics, where the consonant characters
# have the implied *a dropped
all_na = R_cons_na + R_vowel + dia_r


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

# code to switch out consonant syllables in form *a with just *, where the is a diacritic vowel
# also concatenates and nicely outputs the final text
# takes arguments for the two lists of characters as well as the length of the lists
def switch(split_characters, length_of):
    for i in range(0, length_of):
        # if a diacritic vowel comes next, replace current consonant with one not ending in a
        if split_characters[0][i] in dia_d:
            split_characters[1][i-1] = all_na[all_r.index(split_characters[1][i-1])]
    # join all characters together as a continuous stream of text; first the devanagari, then the
    # transliteration
    return(''.join(str(x) for x in split_characters[0]) + ' → ' + ''.join(str(x) for x in split_characters[1]))

# code to parse through the text, split into individual characters and find corresponding locations in arrays
# between devanagari and roman characters
def parse(text):
    # vectors for storing romanized and devanagari output
    output_r = []
    output_d = []
    # store locations of diacritic characters
    locations = []
    for i in range(0, len(text)):
        place = all_d.index(text[i])
        #locations.append(place)
        output_d.append(all_r[place])
        output_r.append(text[i])
    return([output_r, output_d])

# make parse and switch functions work together
def romanize(dev_text):
    return(switch(parse(dev_text), len(dev_text)))

columns = ['Singular','Dual','Plural']
index = ['First','Second','Third']

def conjugate(verb, verb_class):
    vowels = ["a", "ī"]
    guna = ["a", "e"]
    if verb_class == "1" or verb_class == "I":
        first = ["āmi", "āvaḥ", "āmaḥ"]
        second = ["asi", "athaḥ", "atha"]
        third = ["ati", "ataḥ", "anti"]
        splitted = list(verb)
        vowels = ["a", "ī", "ā", "i", "u", "ū", "ṛ", "ṝ", "ḷ"]
        guna = ["a", "e", "a", "e", "o", "o", "ar", "ar", "al"]
        for i in range(0, len(splitted)):
            if splitted[i] in vowels:
                splitted[i] = guna[vowels.index(splitted[i])]
        if splitted[len(splitted)-1:][0] == "e":
            splitted[len(splitted)-1:] = "ay"
        elif splitted[len(splitted)-1:][0] == "o":
            splitted[len(splitted)-1:] = "av"
        elif splitted[len(splitted)-1:][0] == "ai":
            splitted[len(splitted)-1:] = "āy"
        together = ''.join(str(x) for x in splitted)
        for i in range(0, len(first)):
            first[i] = together + first[i]
            second[i] = together + second[i]
            third[i] = together + third[i]
        return(pd.DataFrame([first, second, third], index=index, columns=columns))

    if verb_class == "6" or verb_class == "VI":
        first = ["āmi", "āvaḥ", "āmaḥ"]
        second = ["āsi", "āthaḥ", "ātha"]
        third = ["āti", "ātaḥ", "ānti"]
        chopped = verb[:len(verb)-3]
        for i in range(0, len(first)):
            first[i] = chopped + first[i]
            second[i] = chopped + second[i]
            third[i] = chopped + third[i]
        return(pd.DataFrame([first, second, third], index=index, columns=columns))

conjugate("nī", "1")

# some examples
# decline("phala", "neut")
# romanize("कठोपनिषद")
