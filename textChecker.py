file1 = open("possible_outcomes.txt","r")
file2 = open("cleaned_list.txt","r")
file3 = open("results.txt","w")
word = file1.readline()
for lines in file1:
    file2.close()
    file2 = open("cleaned_list.txt", "r")
    for searcher in file2:
        if lines == searcher:
            file3.write(lines)
file3.close()
file2.close()
file1.close()