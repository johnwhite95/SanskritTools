#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import necessary libraries
import pandas as pd
import json

# Load data
orthography = json.load(open("./data/orthography.json", "r"))
sandhi_data = json.load(open("./data/sandhi_data.json", "r"))
a_stem_declensions = json.load(open("./data/a_stem_declensions.json", "r"))
i_stem_declensions = json.load(open("./data/i_stem_declensions.json", "r"))
u_stem_declensions = json.load(open("./data/u_stem_declensions.json", "r"))
r_stem_declensions = json.load(open("./data/r_stem_declensions.json", "r"))
agent_nouns = open("./data/agent_nouns.csv", "r")
agent_nouns = agent_nouns.read()
relationship_nouns = open("./data/relationship_nouns.csv", "r")
relationship_nouns = relationship_nouns.read()
pres_ten_end = json.load(open("./data/pres_ten_end.json", "r"))
verb_classes = open("./data/verbs_classes.csv", "r")
verb_classes = verb_classes.read()

# text database
D_vowel = orthography["D_vowel"]
R_vowel = orthography["R_vowel"]
dia_d = orthography["dia_d"]
dia_r = orthography["dia_r"]
D_cons = orthography["D_cons"]
R_cons = orthography["R_cons"]
R_cons_na = orthography["R_cons_na"]

# combine all devanagari characters and diacritics
all_d = D_cons + D_vowel + dia_d
# combine romanizations of all devanagari characters and diacritics
all_r = R_cons + R_vowel + dia_r
# combine romanizations of all devanagari characters and diacritics, where the consonant characters
# have the implied *a dropped
all_na = R_cons_na + R_vowel + dia_r

# pairs for sandhi stuff
pairs11 = sandhi_data["pairs11"]
# sandhi joinings
joins11 = sandhi_data["joins11"]
pairs21 = sandhi_data["pairs21"]
joins21 = sandhi_data["joins21"]
pairs22 = sandhi_data["pairs22"]
joins22 = sandhi_data["joins22"]

cases = ["Nom.", "Voc.", "Acc.", "Ins.", "Dat.", "Abl.",
         "Gen.", "Loc."]
columns = ['Singular','Dual','Plural']
index = ['First','Second','Third']
persons = ["third", "second", "first"]

pres_ten_end = pres_ten_end["pres_ten_end"]

# combined declensions
ma_dec = [a_stem_declensions["singdec_ma"], a_stem_declensions["dualdec_ma"], a_stem_declensions["plurdec_ma"]]
na_dec = [a_stem_declensions["singdec_na"], a_stem_declensions["dualdec_na"], a_stem_declensions["plurdec_na"]]
mi_dec = [i_stem_declensions["singdec_mi"], i_stem_declensions["dualdec_mi"], i_stem_declensions["plurdec_mi"]]
ni_dec = [i_stem_declensions["singdec_ni"], i_stem_declensions["dualdec_ni"], i_stem_declensions["plurdec_ni"]]
fi_dec = [i_stem_declensions["singdec_fi"], i_stem_declensions["dualdec_fi"], i_stem_declensions["plurdec_fi"]]
mu_dec = [u_stem_declensions["singdec_mu"], u_stem_declensions["dualdec_mu"], u_stem_declensions["plurdec_mu"]]
nu_dec = [u_stem_declensions["singdec_nu"], u_stem_declensions["dualdec_nu"], u_stem_declensions["plurdec_nu"]]
fu_dec = [u_stem_declensions["singdec_fu"], u_stem_declensions["dualdec_fu"], u_stem_declensions["plurdec_fu"]]
agent_r_masc = [r_stem_declensions["agent_r_masc_s"], r_stem_declensions["agent_r_masc_d"], r_stem_declensions["agent_r_masc_p"]]
rel_r_masc = [r_stem_declensions["rela_r_masc_s"], r_stem_declensions["rela_r_masc_d"], r_stem_declensions["rela_r_masc_p"]]
agent_r_fem = [r_stem_declensions["agent_r_fem_s"], r_stem_declensions["agent_r_fem_d"], r_stem_declensions["agent_r_fem_p"]]
rel_r_fem = [r_stem_declensions["rel_r_fem_s"], r_stem_declensions["rel_r_fem_d"], r_stem_declensions["rel_r_fem_p"]]
nr_dec = [r_stem_declensions["singdec_nr"], r_stem_declensions["dualdec_nr"], r_stem_declensions["plurdec_nr"]]


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

# determine which declensions to use
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

# Some examples
romanize("सत्यमेव जयते")

print(decline("Śiva", "masc"))
print(conjugate("nṛt", "IV"))

print(verb_classes)
