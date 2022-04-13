#if elif else statements
#loop: for-in loop 

if True:
    print("true!")
else:
    print("false!")
 
a = 15   
if a == 5:
    print("a is 5")
elif a == 6:
    print("a is 6")
elif a == 7:
    print("a is 7")
else:
    print(" a is not 5, 6, or 7")
    
print("it is", a)

print("-------------> For-in loop:", "change to upper case")

#change to upper case
for letters in ('a', 'b', 'c', 'd', 'e'):
    #print(letters.upper())
    print(letters.capitalize())

