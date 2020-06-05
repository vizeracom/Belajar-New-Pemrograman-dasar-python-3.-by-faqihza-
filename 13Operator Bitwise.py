#Operator Bitwise

a = 9
b = 5

#bitwise OR
c = a | b
print ("=======Or=========")
print ("Nilai :",a,"binary",format(a,'08b'))
print ("Nilai :",b,"binary",format(b,'08b'))
print ("=====================================")
print ("Nilai :",c,"binary",format(c,'08b'))

#bitwise AND (&)
c = a & b
print ("=======AND=========")
print ("Nilai :",a,"binary",format(a,'08b'))
print ("Nilai :",b,"binary",format(b,'08b'))
print ("=====================================")
print ("Nilai :",c,"binary",format(c,'08b'))

#bitwise XOR(^)
c = a ^ b
print ("=======XOR=========")
print ("Nilai :",a,"binary",format(a,'08b'))
print ("Nilai :",b,"binary",format(b,'08b'))
print ("=====================================")
print ("Nilai :",c,"binary",format(c,'08b'))

#bitwise NOT(~)
c = ~a
print ("=======NOT=========")
print ("Nilai :",a,"binary",format(a,'08b'))

print ("=====================================")
print ("Nilai :",c,"binary",format(c,'08b'))

#counter
d = 0b0000001001
e = 0b1111111111
print ("nilai",'binary',format(e^d,'08b'))

#shift right
c = a >> 1
print ("======>>=======")
print ("Nilai :",a,"binary",format(a,'08b'))
print ("=====================================>>")
print ("Nilai :",c,"binary",format(c,'08b'))

#shift left
c = a << 2
print ("======<<=======")
print ("Nilai :",a,"binary",format(a,'08b'))
print ("=====================================>>")
print ("Nilai :",c,"binary",format(c,'08b'))