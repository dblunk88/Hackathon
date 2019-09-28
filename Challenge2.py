import itertools
import numpy
import PassCrack

password = input("ENTER ZEH PASSWORD: ")
print("Muhchines arr fihring, Mahster: " + password)

M1 = [["B", "D", "G", "H", "L", "M", "P", "R", "S", "T"], ["A", "E", "H", "I", "L", "N", "O", "R", "U", "Y"]
    , ["A", "C", "E", "L", "N", "O", "R", "S", "T", "U"]
    , ["A", "D", "E", "K", "L", "N", "S", "T", "Y", ""]]
count = 0

print(PassCrack.randomSearch(M1, "BURY"))
# PassCrackClass.linearSearch()