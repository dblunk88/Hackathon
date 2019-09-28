import itertools
import numpy


def randomSearch(arr, key):
    count = 0

    for x in numpy.array(numpy.meshgrid(*arr)).T.reshape(-1, len(arr)):
        if x[3] != "":
            count += 1.5
        else:
            count += 1

        if ''.join(x) == key:
            return count

        # Create file of possible outcomes
        # write.write(''.join(x) + "\n")


def linearSearch(arr, key):
    count = 0

    for x in itertools.product(*arr):
        if x[3] != "":
            count += 1.5
        else:
            count += 1

        if ''.join(x) == key:
            return count

    # # print(list(itertools.product(*M1)))
