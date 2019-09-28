import itertools
import numpy

password = input("ENTER ZEH PASSWORD: ")
print("Muhchines arr fihring, Mahster: " + password)

M1 = [["B", "D", "G", "H", "L", "M", "P", "R", "S", "T"], ["A", "E", "H", "I", "L", "N", "O", "R", "U", "Y"]
    , ["A", "C", "E", "L", "N", "O", "R", "S", "T", "U"]
    , ["A", "D", "E", "K", "L", "N", "S", "T", "Y", ""]]
count = 0



# write = open("possible_outcomes.txt","w+")

for x in numpy.array(numpy.meshgrid(*M1)).T.reshape(-1,len(M1)):
    if x[3] != "":
        count += 1.5
    else:
        count += 1

    if ''.join(x) == password:
        print(count)
        exit(0)

    #Create file of possible outcomes
    # write.write(''.join(x) + "\n")

#   inOrder
for new in itertools.product(*M1):
    # print(new)
    if new[3] != "":
        count += 1.5
    else:
        count += 1

    if ''.join(new) == password:
        print(count)
        exit(0)

# # print(list(itertools.product(*M1)))
#   inOrder