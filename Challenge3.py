#instead of bruteforcing, this will analyze the dictionary by used characters in accordance to each index
#this will produce almost instantaneous results while still actively calculating each run
#if implemented with dicSorter, you can have a dynamic dictionary while still producing fast results
#taken one step further, dicSorter could be run on an interval. basically caching the most work-heavy calculations (which are stil quick)
def main():
    # n = amount of characters in a word
    n = setVar("n","above 0")
    # m = amount of characters per character slot
    m = setVar("m","above or equal to 2 and below or equal to 26")
    everyCombo(n,m)

def everyCombo(n,m):
    #creating a dictionary
    characters = {}
    #opening up the dictionary of n letters
    allWords = open("{}.txt".format(n),"r")
    #go down each word
    for lines in allWords:
        #starts at index 0
        indexCount = 0
        #break down the words by individual characters
        for chars in lines.strip(" ").strip("\n"):
            #dictionary key is the index + the character (ex 0A)
            dicValue = str(indexCount)+chars
            #check if there is already a dictionary entry for that value
            if dicValue in characters:
                #if there is, increment by 1 (increments each finding)
                characters[dicValue] += 1
            else:
                #if there is not, set it to 1
                characters[dicValue] = 1
            #each loop is an index, so we increment
            indexCount += 1
    #verbose print of the raw dictionary
    print(characters)
    #now we sort and print our heatmap. this for loop loops n times (1 for each index)
    for index in range(0,n):
        #verbose print of the current index number
        print("Index",index)
        #creating an array so that we can easily print and remove the printed values
        indexListed = []
        #one loop for each letter of the alphabet to check each heat map entry
        for charNum in range(0,26):
            #converting each loop to a character by utilizing the ASCII table
            actualChar = chr(charNum + 65)
            #simple error handling. if non existant, just continue
            try:
                #add the dictionary values to the array
                indexListed.append([characters[str(index) + actualChar],actualChar])
            except:
                continue
        #now we sort and list out the "m" most used characters for the given index
        for mloop in range(0,m):
            #error handling
            try:
                #print out the maximum value and remove it from the array (so that we will get the top most used characters.. our heatmap)
                print(max(indexListed))
                indexListed.remove(max(indexListed))
            except:
                continue

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
