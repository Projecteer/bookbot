def sorter(sort):
    return sort["c"]

def wordCount(text):
    totalWords = len(text.split())
    print(f"Found {totalWords} total words")
def charCount(text):
    charDict = {}
    for char in text:
        char = char.lower()
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    #charDict.sort(reverse=True, key=sorter)
    #print(charDict)
    return charDict

def sort_on(item):
    return item["num"]

def sortDict(dict):
    #charDict2 = dict
    #charDict2 = [{"char" : "", "num" : 0}]
    charDict2 = []
    #for i in len(dict):
    #    charDict2[i] = dict[i]
    #print(dict)
    #dict.sort(reverse=True, key=sort_on)
    #print(dict)
    #print(charDict2)
    for inp in dict:
        #charDict2[] = inp
        number = dict[inp]
        charDict2.append({"char": inp, "num" : number})
    #print(charDict2)
    charDict2.sort(reverse=True, key=sort_on)
    #print(charDict2)
    for dictInp in charDict2:
        print(f"{dictInp["char"]}: {dictInp["num"]}")
    #for char in text:
    #    char = char.lower()
    #    if char == charDict2["char"]:
    #        print()
    #print(dict.sort(reverse=True, key=sortOn))