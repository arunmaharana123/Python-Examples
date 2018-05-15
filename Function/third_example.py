

sentence = "This is My name"

def splitIt(stuff):
    return stuff.split(" ")

def sortIt(stuff):
    return sorted(stuff)

print sortIt(splitIt(sentence))
