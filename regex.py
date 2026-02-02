tree = ' eatoinshrdlcumwfgypbvkjxqz'

out = open('1mb_cleaned.txt','w')

file = open('1mb.txt')

for i in file.read():
    if i in tree:
        out.write(i)