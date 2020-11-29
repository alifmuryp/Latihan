#operasi komparasi
#<,>,<=,>=,==,!=
a=4
b=2
#kurang Dari <
print ("====kurang Dari <")
hasil=a < 3
print (a,"<",3,"adalah",hasil)
hasil=b < 3
print (b,"<",3,"adalah",hasil)
hasil= b < 2
print (b,"<",2,"adalah",hasil)

#lebih Dari >
print ("====lebih Dari >")
hasil=a > 3
print (a,">",3,"adalah",hasil)
hasil=b > 3
print (b,">",3,"adalah",hasil)
hasil= b > 2
print (b,">",2,"adalah",hasil)

#kurang Dari samadengan <=
print ("====kurang Dari samadengan <=")
hasil=a <= 3
print (a,"<=",3,"adalah",hasil)
hasil=b <= 3
print (b,"<=",3,"adalah",hasil)
hasil= b <= 2
print (b,"<=",2,"adalah",hasil)

#kurang Dari samadengan >=
print ("====lebih Dari samadengan >=")
hasil=a >= 3
print (a,">=",3,"adalah",hasil)
hasil=b >= 3
print (b,">=",3,"adalah",hasil)
hasil= b >= 2
print (b,">=",2,"adalah",hasil)

#samadengan ==
print ("====samadengan ==")
hasil=a == 3
print (a,"==",3,"adalah",hasil)
hasil=b == 3
print (b,"==",3,"adalah",hasil)
hasil= b == 2
print (b,"==",2,"adalah",hasil)

#kurang Dari !=
print ("====bukan samadengan !=")
hasil=a != 3
print (a,"!=",3,"adalah",hasil)
hasil=b != 3
print (b,"!=",3,"adalah",hasil)
hasil= b != 2
print (b,"!=",2,"adalah",hasil)

#'is' sebagai komparasi identity
x=5
y=5
print ('nilai x =',x,'id',hex(id(x)))
print ('nilai y =',y,'id',hex(id(y)))
hasil = x is 5
print ("hasil x is 5 =",hasil)
#beda
x=5
y=6
print ('nilai x =',x,'id',hex(id(x)))
print ('nilai y =',y,'id',hex(id(y)))
hasil = x is y
print ("hasil x is y =",hasil)