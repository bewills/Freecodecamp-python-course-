#write a program to open a file and read through and print line by line all in upper case. 

userin = input ('Enter a file name:')
fhand = open(userin)
for line in fhand:
    x = line.rstrip()
    print(x.upper())