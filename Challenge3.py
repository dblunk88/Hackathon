def main():
    # n = amount of characters in a word
    n = setVar("n","above 0")
    # m = amount of characters per character slot
    m = setVar("m","above or equal to 2 and below or equal to 26")
    everyCombo(n,m)

def everyCombo(n,m):
    characters = [[0][0]] * 26
    for index in range(0,26):
        print(index)
        characters[index] = [[chr(index+65)][0]]

    print(characters)
    allWords = open("{}.txt".format(n),"r")



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
