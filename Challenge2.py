import PassCrack

M1 = [["B", "D", "G", "H", "L", "M", "P", "R", "S", "T"]
    , ["A", "E", "H", "I", "L", "N", "O", "R", "U", "Y"]
    , ["A", "C", "E", "L", "N", "O", "R", "S", "T", "U"]
    , ["A", "D", "E", "K", "L", "N", "S", "T", "Y", ""]]
count = 0
read = open("challenge2testinputs.txt", "r")

for word in read.read().split("\n"):
    print("testing: " + word + "...")
    count += PassCrack.randomSearch(M1, word)

read.close()
print("Average time to crack: " + str((count/50)/60) + " minutes.")



#TODO: get time averages with words for challenge 2

# write = open("possible_outcomes.txt","w+")
#
# print(PassCrack.randomSearch(M1, "BURY"))
