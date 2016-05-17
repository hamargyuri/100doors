#!/usr/bin/env python3

print ("Which doors will stay open:")

list = [0] * 100 #creates list of 100 0s

for a in range (1, 101):
    for b in range (100):
        if (b + 1) % a == 0: #need b+1 here, because python gives indexes 0-99
            if list[b] == 0:
                list[b] = 1
            else:
                list[b] = 0

for c in range(100):
    if list[c] == 1:
        print (c+1) #c+1 here again because of python indexing
