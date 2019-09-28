read = open("words_alpha.txt","r")
write = open("cleaned_list.txt","w+")
for lines in read:
    print(lines)
    line = lines.strip(" ")
    if len(line) == 5:
        print(line.upper())
        write.write(line.upper())
read.close()
write.close()