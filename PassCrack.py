import itertools
import numpy


def randomSearch(arr, key):
    count = 0.0

    for x in numpy.array(numpy.meshgrid(*arr)).T.reshape(-1, len(arr)):
        combination = ''.join(x)
        read = open("challenge2.txt", "r")
        for word in read.read().split("\n"):
            if combination == word:
                if combination == key:
                    read.close()
                    return count
                else:
                    if x[3] != "":
                        count += 1.5
                        read.close()
                        continue

                    else:
                        count += 1.0
                        read.close()
                        continue
            else:
                continue

    return 0.0

        # Create file of possible outcomes
        # write.write(''.join(x) + "\n")


# not linear
# def linearSearch(arr, key):
#     count = 0
#
#     for x in itertools.product(*arr):
#         if x[3] != "":
#             count += 1.5
#         else:
#             count += 1
#
#         if ''.join(x) == key:
#             return count
#
#     # # print(list(itertools.product(*M1)))
