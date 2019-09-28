def main():
    n = setVar("n","above 0")
    m = setVar("m","above or equal to 2 and below or equal to 26")

    
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