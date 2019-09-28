def main():
    # n = amount of characters in a word
    n = setVar("n","above 0")
    # m = amount of characters per character slot
    m = setVar("m","above or equal to 2 and below or equal to 26")
    everyCombo(n,m)

def everyCombo(n,m):
    characters = {}
    allWords = open("{}.txt".format(n),"r")
    wordCount = 0
    for lines in allWords:
        print(lines)
        indexCount = 0
        for chars in lines.strip(" ").strip("\n"):
            dicValue = str(indexCount)+chars
            if dicValue in characters:
                characters[dicValue] += 1
            else:
                characters[dicValue] = 0
            indexCount += 1
        wordCount += 1
    print(characters)
    for index in range(0,n):
        for charNum in range(0,26):
            actualChar = chr(charNum + 65)
            print(characters[str(index) + actualChar])

def setVar(name,requirements):
    var = None
    try:
        var = int(input("Enter %s: " % name))
    except:
        print("Please enter an integer %s" % requirements)
        setVar(name, requirements)
    if name == "n":
        if var <= 0:
            print("Please enter an integer %s" % requirements)
            setVar(name, requirements)
    else:
        if var < 2 or var > 26:
            print("Please enter an integer %s" % requirements)
            setVar(name, requirements)
    return var



if __name__== "__main__":
  main()
