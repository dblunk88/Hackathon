read = open("words_alpha.txt","r")
write = open("words_alpha_uppercase.txt","w")
for lines in read:
    write.write(lines.upper())