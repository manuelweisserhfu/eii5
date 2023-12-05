a = False
b = False
c = False
d = False
v = False

print((not a and not b) or (a and b))           #1
print((a and (b or c)) or (b and not c))        #2
print(False)                                    #3
print(a or (not b and not (a or c)))            #4
print(a and not b)                              #5
print(c or d)                                   #6
print(not a or not c or (not b and v))          #7  
print(not(not a or not b or c) or (a and c))    #8 