#Logika Boolean

#Not, or adn xor

#Not
a = True

c = not a
print ("NIlai :", a)

print ("hasil Not :", c)

# OR
print ("=====OR======")
a = False
b = False
c = a or b
print (a,"OR",b,"=",c)
a = False
b = True
c = a or b
print (a,"OR",b,"=",c)
a = True
b = False
c = a or b
print (a,"OR",b,"=",c)
a = True
b = True
c = a or b
print (a,"OR",b,"=",c)

# AND

print ("======AND=======")
a = False
b = False
c = a and b
print (a,"AND",b,"=",c)
a = False
b = True
c = a and b
print (a,"AND",b,"=",c)
a = True
b = False
c = a and b
print (a,"AND",b,"=",c)
a = True
b = True
c = a and b
print (a,"AND",b,"=",c)

#XOR
print ("======XOR=======")
a = False
b = False
c = a ^ b
print (a,"XOR",b,"=",c)
a = False
b = True
c = a ^ b
print (a,"XOR",b,"=",c)
a = True
b = False
c = a ^ b
print (a,"XOR",b,"=",c)
a = True
b = True
c = a ^ b
print (a,"XOR",b,"=",c)