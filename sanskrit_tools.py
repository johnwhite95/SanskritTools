import pandas as pd

# text database
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

# pairs for sandhi stuff
pairs11 = [
    ["a", "a"], ["a", "i"], ["i", "ī"], ["i", "a"],
    ["h", "s"], ["u", "u"], ["m", "s"], ["t", "j"],
    ["ṭ", "h"], ["n", "t"], ["a", "ḥ"], ["a", "aḥ"],
    ["a", "an"]
]

# sandhi joinings
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

columns = ['Singular','Dual','Plural']
index = ['First','Second','Third']

# masculine a-stem declensions
singdec_ma = ["aḥ", "a", "am", "ena", "āya", "āt", "asya", "e"]
dualdec_ma = ["au", "au", "au", "ābhyām", "ābhyām", "ābhyām", "ayoḥ", "ayoḥ"]
plurdec_ma = ["āḥ", "āḥ", "ān", "aiḥ", "ebhyaḥ", "ebhyaḥ",
              "ānām", "eṣu"]
# neuter a-stem declensions
singdec_na = ["am", "a", "am", "ena", "āya", "āt", "asya", "e"]
dualdec_na = ["e", "e", "e", "ābhyām", "ābhyām", "ābhyām",
              "ayoḥ", "ayoḥ"]
plurdec_na = ["āni", "āni", "āni", "aiḥ", "ebyaḥ", "ebyaḥ",
              "ānām", "eṣu"]

# masculine i-stem declensions
singdec_mi = ["is", "e", "im", "inā", "aye", "es", "es", "au"]
dualdec_mi = ["ī", "ī", "ī", "ibhyām", "ibhyām", "ibhyām",
              "yos", "yos"]
plurdec_mi = ["ayas", "ayas", "īn", "ibhis", "ibhyas",
              "ibhyas", "īnām", "iṣu"]
# neuter i-stem declensions
singdec_ni = ["i", "i/-e", "i", "iṇā", "iṇe", "iṇas", "iṇas", "iṇi"]
dualdec_ni = ["iṇī", "iṇī", "iṇī", "ibhyām", "ibhyām",
              "ibhyām", "iṇnos", "iṇnos"]
plurdec_ni = ["īṇī", "īṇī", "īṇī", "ibhis", "ibhyas",
              "ibhyas", "īṇām", "iṣu"]
# feminine i-stem declensions
singdec_fi = ["is", "e", "im", "yā", "aye", "es", "es", "au"]
dualdec_fi = ["ī", "i", "ī", "ibhyām", "ibhyām", "ibhyām",
              "yos", "yos"]
plurdec_fi = ["ayas", "aya", "is", "ibhis", "ibhyas",
              "ibhyas", "īnām", "iṣu"]

# masculine u-stem declensions
singdec_mu = ["us", "um", "unā", "ave", "os", "os", "au", "o"]
dualdec_mu = ["ū", "ū", "ubhyām", "ubhyām", "ubhyām", "vos", "vos", "u"]
plurdec_mu = ["avas", "ūn", "ubhis", "ubhyas", "ubhyas", "ūnām", "uṣu", "avas"]
# neuter u-stem declensions
singdec_nu = ["u", "u", "unā", "une", "unas", "unas", "uni", "u/o"]
dualdec_nu = ["unī", "unī", "ubhyām", "ubhyām", "ubhyām", "unos", "unos", "uni"]
plurdec_nu = ["ūni", "ūni", "ubhis", "ubhyas", "ubhyas", "ūnām", "uṣu", "ūni"]
# feminine u-stem declensions
singdec_fu = ["us", "um", "vā", "ave", "os", "os", "au", "o"]
dualdec_fu = ["ū", "ū", "ubhyām", "ubhyām", "ubhyām", "vos", "vos", "ū"]
plurdec_fu = ["avas", "ūs", "ubhis", "ubhyas", "ubhyas", "unam", "usu", "avas"]

# masculine ṛ-stem agent declensions
agent_r_masc_s = ["ā", "āram", "rā", "re", "ur", "ur", "ari", "ar"]
agent_r_masc_d = ["ārau", "ārau", "ṛbhyām", "ṛbhyām", "ṛbhyām", "ros", "ros", "arau"]
agent_r_masc_p = ["āras", "ṛn", "ṛbhis", "ṛbhyas", "ṛbhyas", "ṛnām", "ṛṣu", "āras"]
# masculine ṛ-stem relationship declensions
rela_r_masc_s = ["ā", "aram", "rā", "re", "ur", "ur", "ari", "ar"]
rela_r_masc_d = ["arau", "arau", "bhyām", "bhyām", "bhyām", "ros", "ros", "arau"]
rela_r_masc_p = ["aras", "ṛn", "ṛbhis", "ṛbhyas", "ṛbhyas", "ṛnām", "ṛṣu", "aras"]
#feminine ṛ-stem agent declensions
agent_r_fem_s = ["rīā", "rīaram", "rīrā", "rīre", "rīur", "rīur", "rīari", "rīar"]
agent_r_fem_d = ["rīarau", "rīarau", "rīṛbhyām", "rīṛbhyām", "rīṛbhyām",
                 "rīros", "rīros", "rīarau"]
agent_r_fem_p = ["rīaras", "rīṛs", "rīṛbhis", "rīṛbhyas", "rīṛbhyas",
                 "rīṛnām", "rīṛṣu", "rīaras"]
#feminine ṛ-stem relationship declensions
rel_r_fem_s = ["ā", "aram", "rā", "re", "ur", "ur", "ari", "ar"]
rel_r_fem_d = ["arau", "arau", "ṛbhyām", "ṛbhyām", "ṛbhyām", "ros", "ros", "arau"]
rel_r_fem_p = ["aras", "ṛs", "ṛbhis", "ṛbhyas", "ṛbhyas", "ṛnām", "ṛṣu", "aras"]
#neuter ṛ-stem declensions
singdec_nr = ["ṛ", "ṛ", "ṛ", "ṛṇā", "ṛṇe", "ṛṇas", "ṛṇas", "ṛṇi"]
dualdec_nr = ["ṛṇī", "ṛṇī", "ṛṇī", "ṛbhyām", "ṛbhyām",
              "ṛbhyām", "ṛṇnos", "ṛṇnos"]
plurdec_nr = ["ṛṇī", "ṛṇī", "ṛṇī", "ṛbhis", "ṛbhyas",
              "ṛbhyas", "ṛṇām", "ṛṣu"]

# combined declensions
ma_dec = [singdec_ma, dualdec_ma, plurdec_ma]
na_dec = [singdec_na, dualdec_na, plurdec_na]
mi_dec = [singdec_mi, dualdec_mi, plurdec_mi]
ni_dec = [singdec_ni, dualdec_ni, plurdec_ni]
fi_dec = [singdec_fi, dualdec_fi, plurdec_fi]
mu_dec = [singdec_mu, dualdec_mu, plurdec_mu]
nu_dec = [singdec_nu, dualdec_nu, plurdec_nu]
fu_dec = [singdec_fu, dualdec_fu, plurdec_fu]
agent_r_masc = [agent_r_masc_s, agent_r_masc_d, agent_r_masc_d]
rel_r_masc = [rela_r_masc_s, rela_r_masc_d, rela_r_masc_p]
agent_r_fem = [agent_r_fem_s, agent_r_fem_d, agent_r_fem_d]
rel_r_fem = [rel_r_fem_s, rel_r_fem_d, rel_r_fem_p]
nr_dec = [singdec_nr, dualdec_nr, plurdec_nr]

agent_nouns = ["boddhṛ", "dātṛ", "kartṛ"]
relationship_nouns = ["pitṛ", "matṛ"]

persons = ["third", "second", "first"]
pres_ten_end = ["ati", "asi", "āmi", "-", "-", "āvaḥ",
                "anti", "-", "āmaḥ"]

# function to process and display declensions
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

# need to complete masculine support as well as implement neuter and feminine
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
    elif stem == "u":
        if gender == "masc":
            output = list_declen(stem_cut, mu_dec)
        elif gender == "neut":
            output = list_declen(stem_cut, nu_dec)
        elif gender == "fem":
            output = list_declen(stem_cut, fu_dec)
    elif stem == "ṛ":
        if gender == "masc":
            if noun in agent_nouns:
                output = list_declen(stem_cut, agent_r_masc)
            elif noun in relationship_nouns:
                output = list_declen(stem_cut, rel_r_masc)
        if gender == "fem":
            if noun in agent_nouns:
                output = list_declen(stem_cut, agent_r_fem)
            elif noun in relationship_nouns:
                output = list_declen(stem_cut, rel_r_fem)
        if gender == "neut":
            output = list_declen(stem_cut, nr_dec)
    else:
        output = "noun not recognized"
    return(output)

def conjugate(verb, verb_class):
    weak_vowels = ["a", "ī", "ā", "i", "u", "ū", "ṛ", "ṝ", "ḷ"]
    guna_vowels = ["a", "e", "a", "e", "o", "o", "ar", "ar", "al"]
    if verb_class == "1" or verb_class == "I":
        first = ["āmi", "āvaḥ", "āmaḥ"]
        second = ["asi", "athaḥ", "atha"]
        third = ["ati", "ataḥ", "anti"]
        splitted = list(verb)
        for i in range(0, len(splitted)):
            if splitted[i] in weak_vowels:
                splitted[i] = guna_vowels[weak_vowels.index(splitted[i])]
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

    if verb_class == "4" or verb_class == "IV":
        first = ["mi", "vaḥ", "maḥ"]
        second = ["si", "thaḥ", "tha"]
        third = ["ti", "taḥ", "nti"]
        splitted = list(verb)
        together = ''.join(str(x) for x in splitted)
        for i in range(0, len(first)):
            first[i] = together + "ya" + first[i]
            second[i] = together + "ya" + second[i]
            third[i] = together + "ya" + third[i]
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

# maybe include an option for clusters
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

decline("datṛ", "neut")
conjugate("nṛt", "IV")
