#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import json

orthography = json.load(open("./data/orthography.json", "r"))
sandhi_data = json.load(open("./data/sandhi_data.json", "r"))
a_stem_declensions = json.load(open("./data/a_stem_declensions.json", "r"))
i_stem_declensions = json.load(open("./data/i_stem_declensions.json", "r"))
u_stem_declensions = json.load(open("./data/u_stem_declensions.json", "r"))
r_stem_declensions = json.load(open("./data/r_stem_declensions.json", "r"))
agent_nouns = open("./data/agent_nouns.csv", "r")
relationship_nouns = open("./data/relationship_nouns.csv", "r")
pres_ten_end = json.load(open("./data/pres_ten_end.json", "r"))

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

# masculine a-stem declensions
singdec_ma = a_stem_declensions["singdec_ma"]
dualdec_ma = a_stem_declensions["dualdec_ma"]
plurdec_ma = a_stem_declensions["plurdec_ma"]
# neuter a-stem declensions
singdec_na = a_stem_declensions["singdec_na"]
dualdec_na = a_stem_declensions["dualdec_na"]
plurdec_na = a_stem_declensions["plurdec_na"]

# masculine i-stem declensions
singdec_mi = i_stem_declensions["singdec_mi"]
dualdec_mi = i_stem_declensions["dualdec_mi"]
plurdec_mi = i_stem_declensions["plurdec_mi"]
# neuter i-stem declensions
singdec_ni = i_stem_declensions["singdec_ni"]
dualdec_ni = i_stem_declensions["dualdec_ni"]
plurdec_ni = i_stem_declensions["plurdec_ni"]
# feminine i-stem declensions
singdec_fi = i_stem_declensions["singdec_fi"]
dualdec_fi = i_stem_declensions["dualdec_fi"]
plurdec_fi = i_stem_declensions["plurdec_fi"]

# masculine u-stem declensions
singdec_mu = u_stem_declensions["singdec_mu"]
dualdec_mu = u_stem_declensions["dualdec_mu"]
plurdec_mu = u_stem_declensions["plurdec_mu"]
# neuter u-stem declensions
singdec_nu = u_stem_declensions["singdec_nu"]
dualdec_nu = u_stem_declensions["dualdec_nu"]
plurdec_nu = u_stem_declensions["plurdec_nu"]
# feminine u-stem declensions
singdec_fu = u_stem_declensions["singdec_fu"]
dualdec_fu = u_stem_declensions["dualdec_fu"]
plurdec_fu = u_stem_declensions["plurdec_fu"]

# masculine ṛ-stem agent declensions
agent_r_masc_s = r_stem_declensions["agent_r_masc_s"]
agent_r_masc_d = r_stem_declensions["agent_r_masc_d"]
agent_r_masc_p = r_stem_declensions["agent_r_masc_p"]
# masculine ṛ-stem relationship declensions
rela_r_masc_s = r_stem_declensions["rela_r_masc_s"]
rela_r_masc_d = r_stem_declensions["rela_r_masc_d"]
rela_r_masc_p = r_stem_declensions["rela_r_masc_p"]
#feminine ṛ-stem agent declensions
agent_r_fem_s = r_stem_declensions["agent_r_fem_s"]
agent_r_fem_d = r_stem_declensions["agent_r_fem_d"]
agent_r_fem_p = r_stem_declensions["agent_r_fem_p"]
#feminine ṛ-stem relationship declensions
rel_r_fem_s = r_stem_declensions["rel_r_fem_s"]
rel_r_fem_d = r_stem_declensions["rel_r_fem_d"]
rel_r_fem_p = r_stem_declensions["rel_r_fem_p"]
#neuter ṛ-stem declensions
singdec_nr = r_stem_declensions["singdec_nr"]
dualdec_nr = r_stem_declensions["dualdec_nr"]
plurdec_nr = r_stem_declensions["plurdec_nr"]

# combined declensions
ma_dec = [a_stem_declensions["singdec_ma"], a_stem_declensions["dualdec_ma"], a_stem_declensions["plurdec_ma"]]
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

#agent_nouns = ["boddhṛ", "dātṛ", "kartṛ"]
#relationship_nouns = ["pitṛ", "matṛ"]

persons = ["third", "second", "first"]
pres_ten_end = pres_ten_end["pres_ten_end"]

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

romanize("सत्यमेव जयते")

print(decline("datṛ", "neut"))
conjugate("nṛt", "IV")