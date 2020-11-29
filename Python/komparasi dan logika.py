#latihan komparasi
#membuat gabungan area rentang Dari angka
#+++++3------10+++++
inputUser = float(input('masukkan angka yang bernilai kurang Dari 3\natau\nlebih Dari 10:\n'))
#++++3-----
iskurangdari = (inputUser < 3)
print ("hasilnya kurang dari=",iskurangdari)
#-----10+++++
islebihdari = (inputUser >10)
print ("hasilnya kurang dari=",islebihdari)
#+++++3------10+++++
iscorrect = iskurangdari or islebihdari
print ("hasil =",iscorrect)

print ("\n",20*"-","\n")

#------3+++++++++10------
inputUser = float(input('masukkan angka yang bernilai kurang Dari 10\ndan\nlebih Dari 3:\n'))
#----3++++++
islebihdari = (inputUser > 3)
print ("lebih Dari 3=",islebihdari)
#+++++++10-----
iskurangdari = (inputUser <10)
print ("kurang dari 10=",islebihdari)
#+++++3------10+++++
iscorrect = iskurangdari and islebihdari
print ("hasil =",iscorrect)

print ("\n",20*"-","\n")


inputUser = float(input('masukkan angka yang bernilai 0-5 Dan 8-11 :\n'))
#----0++++
islebihdari = (inputUser > 0)
print ("lebih Dari 0=",islebihdari)
#++++5----
iskurangdari = (inputUser <5)
print ("kurang dari 5=",iskurangdari)
#----0+++++5----
nol_five = iskurangdari and islebihdari
print ("hasil 0-5 =",nol_five)
#----8++++
islebihdari = (inputUser > 8)
print ("lebih Dari 8=",islebihdari)
#++++11----
iskurangdari = (inputUser <11)
print ("kurang dari 11=",iskurangdari)
#----8+++++11----
eigh_eleven = iskurangdari and islebihdari
print ("hasil 8-11 =",eigh_eleven)
#----0++++5----8++++++11----
hasil = eigh_eleven or nol_five
print ("hasil 0-5 or 8-11 =",hasil)