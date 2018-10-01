import json

sandhi_data = json.load(open("./data/sandhi.json", "r"))

def sandhi(x):
    return sandhi_data.get(x, " | sandhi error | ") 

def make_it(x, y):

    if x[len(x) - 2:] == "ai" or x[len(x) - 2:] == "au":

        if y[0:2] == "ai" or y[0:2] == "au":
            join = sandhi(x[len(x) - 2:] + " " + y[0:2])
            return(x[0:len(x) - 2] + join + y[2:])

        else:
            join = sandhi(x[len(x) - 2:] + " " + y[0])
            return(x[0:len(x) - 2] + join + y[1:])

    elif y[0:2] == "ai" or y[0:2] == "au":

        if x[len(x) - 2:] == "ai" or x[len(x) - 2:] == "au":
            join = sandhi(x[len(x) - 2:] + " " + y[0:2])
            return(x[0:len(x) - 2] + join + y[2:])

        else:
            join = sandhi(x[len(x) - 1:] + " " + y[0:2])
            return(x[0:len(x) - 1] + join + y[2:])

    else:
        join = sandhi(x[len(x) - 1:] + " " + y[0])
        return(x[0:len(x) - 1] + join + y[1:])

print(make_it("gacchatai", "auśvaraḥ"))