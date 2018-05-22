
# coding: utf-8

# Portuguese tools
# version 0.2

# changelog: cleaned up code, made use of more efficient methods from Python's
# functional programming features

# import necessary libraries
import pandas as pd
import numpy as np

# define dictionaries containing verb endings
present_indicative = {"name": "present_indicative",
                      "ar": ["o", "amos", "as", "ais", "a", "am"],
                      "er": ["o", "emos", "es", "eis", "e", "em"],
                      "ir": ["o", "imos", "es", "is", "e", "em"]}
preterit_perfect = {"name": "preterit_perfect",
                    "ar": ["ei", "ámos", "aste", "astes", "ou", "aram"],
                    "er": ["i", "emos", "es", "eis", "e", "em"],
                    "ir": ["i", "imos", "iste", "istes", "iu", "iram"]}

# define dictionaries containing irregular cases of verbs
present_indicative_irregulars = {"estar": {"eu": "estou", "tu": "estás", "ele": "está", "eles": "estão"},
                                 "dar": {"eu": "dou", "tu": "dás", "ele": "dá", "eles": "dão"},
                                 "querer": {"ele": "quer"},
                                 "subir": {"tu": "sobes", "ele": "sobe", "eles": "sobem"},
                                 "ser": {"eu": "sou", "tu": "és", "ele": "é", "nós": "somos", "vós": "sois", "eles": "são"} }

preterit_perfect_irregulars = {"estar": {"eu": "estive", "tu": "estiveste", "ele": "esteve", "nós": "estivemos", "vós": "estivestes", "eles": "estiveram"},
                               "dar": {"tu": "deste", "ele": "deu", "nós": "demos", "vós": "destes", "eles": "deram"},
                               "querer": {"eu": "quis", "tu": "quiseste", "ele": "quis", "nós": "quisemos", "vós": "quisestes", "eles": "quiseram"},
                               "ser": {"eu": "fui", "tu": "foste", "ele": "foi", "nós": "fomos", "vós": "fostes", "eles":"foram"}}

# combine dictionaries of iregulars into a single dictionary
irregulars = {"present_indicative": present_indicative_irregulars,
              "preterit_perfect": preterit_perfect_irregulars}

# create list of pronouns to be a column of a dataframe next to the appropriate verb forms
nominative_pronouns = ["eu", "nós", "tu", "vós", "ele", "eles"]

# define a function to perform the conjugation of a verb, by removing the last two letters of the infinitive
# and concatinating it with the appropriate ending from an endings dictionary
def conjugate(verb, endings): return(list(map(lambda x: ''.join([*verb][0:len(verb) - 2]) + x,
                                              endings[''.join([*verb][len(verb) - 2:len(verb)])])))

# convert conjugated data into a dataframe
def to_dataframe(conjugated): return(pd.DataFrame(np.array(conjugated), index = nominative_pronouns))

# check for an irregular verb; if the verb is irregular, replace the regular forms with the appropriate
# irregular ones
def irregular(verb, x, y, my_dict):
    if (verb in my_dict):
        x.loc[y.index] = y
    return(x)

# take user input and bring all the functions together
def user_in(verb, endings):

    # bring in a dictionary of irregular verbs for the chosen tense
    dict_of_irregs = irregulars[endings["name"]]

    #create dataframe of conjugated verb
    framed = to_dataframe(conjugate(verb, endings)).rename(index=str, columns = {0:verb})

    # if the verb is found to be in the dictionary of irregulars, call the irregular() function to
    # replace the irregular forms and redefine the dataframe of conjugations
    if (verb in dict_of_irregs):
        find_verb = pd.DataFrame(pd.DataFrame(dict_of_irregs)[verb]).dropna()
        framed = irregular(verb, to_dataframe(conjugate(verb, endings)).rename(index = str, columns = {0:verb}),
                           find_verb, dict_of_irregs)

    # print the name of the chosen tense
    print(endings["name"])
    # return the conjugations
    return(framed)

# example of use with the preterit perfect tense of the irregular verb "estar"
print(user_in("estar", preterit_perfect))
