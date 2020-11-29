#operasi logika Dan bolean
#not, or, and ,xor

#not
print ("====NOT====")
a=True
c=not a
print ("data a=",a)
print ("------- NOT")
print ("data c=",c)

#or (jika salah satu true maka jadi true)
print ("====or====")
a=True
b=False
c= a or b
print (a,"or",b," =",c)
a=True
b=True
c= a or b
print (a,"or",b,"  =",c)
a=False
b=False
c= a or b
print (a,"or",b,"=",c)
a=False
b=True
c= a or b
print (a,"or",b," =",c)

#AND (harus dua duanya true=true)
print ("====AND====")
a=True
b=False
c= a and b
print (a,"AND",b," =",c)
a=True
b=True
c= a and b
print (a,"AND",b,"  =",c)
a=False
b=False
c= a and b
print (a,"AND",b,"=",c)
a=False
b=True
c= a and b
print (a,"AND",b," =",c)

#XOR (hanya jika ada satu true=true)
print ("====XOR====")
a=True
b=False
c= a ^ b
print (a,"XOR",b," =",c)
a=True
b=True
c= a ^ b
print (a,"XOR",b,"  =",c)
a=False
b=False
c= a ^ b
print (a,"XOR",b,"=",c)
a=False
b=True
c= a ^ b
print (a,"XOR",b," =",c)