import numpy

generatedlock = [['S', 'C', 'A', 'B', 'T', 'P', 'M', 'D', 'G', 'F'], ['A', 'O', 'E', 'I', 'U', 'R', 'L', 'H', 'N', 'T'],
                 ['R', 'A', 'I', 'N', 'O', 'L', 'E', 'U', 'T', 'S'], ['E', 'A', 'I', 'T', 'N', 'L', 'O', 'R', 'S', 'U'],
                 ['S', 'E', 'Y', 'A', 'T', 'N', 'R', 'D', 'L', 'O']]

count = 0

for x in numpy.array(numpy.meshgrid(*generatedlock)).T.reshape(-1, len(generatedlock)):
    combination = ''.join(x)
    read = open("5.txt", "r")
    write = open("challenge3compatible.txt", "w")
    for word in read.read().split("\n"):
        if combination == word:
            print(word)
            write.write(word + "\n")

    write.close()