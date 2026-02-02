tree = ' eatoinshrdlcumwfgypbvkjxqz'

file = open('1mb_cleaned.txt','r').read()

print(sorted([(i,file.count(i)) for i in tree],key=lambda x:x[1]))