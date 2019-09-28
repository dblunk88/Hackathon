dictionary = open("words_alpha_uppercase.txt","r")
for lines in dictionary:
    length = len(lines) - 1
    write = open("{}.txt".format(length),"a")
    write.write(lines)
    write.close()