#practice penghitungan temperature
print ("\nPROGRAM TEMPERATURE\n")

##celcius
celcius = float(input("masukan suhu dalam bentuk celcius :"))
print ("suhu adalah",celcius, "celcius")
#reamer
reamer = (4/5) * celcius
print ("suhu adalah",reamer, "reamer")
#Fahrenheit
Fahrenheit = (9/5) * celcius
print ("suhu adalah",Fahrenheit, "Fahrenheit")
#kelvin
kelvin = celcius+273
print ("suhu adalah",kelvin, "kelvin")

##reamure
reamer = float(input("masukan suhu dalam bentuk reamer :"))
#celcius
celcius = (5/4) * reamer
print ("suhu adalah",celcius, "celcius")
#reamer
print ("suhu adalah",reamer, "reamer")
#Fahrenheit
Fahrenheit = (9/4)*reamer +32
print ("suhu adalah",Fahrenheit, "Fahrenheit")
#kelvin
kelvin = (5/4)*reamer +273
print ("suhu adalah",kelvin, "kelvin")

##Fahrenheit
reamer = float(input("masukan suhu dalam bentuk Fahrenheit :"))
#celcius
celcius = (5/9) * (Fahrenheit-32)
print ("suhu adalah",celcius, "celcius")
#reamer
celcius = (4/9) * (Fahrenheit-12)
print ("suhu adalah",reamer, "reamer")
#Fahrenheit
print ("suhu adalah",Fahrenheit, "Fahrenheit")

##kelvin
reamer = float(input("masukan suhu dalam bentuk kelvin :"))
#celcius
celcius = kelvin-273
print ("suhu adalah",celcius, "celcius")
#reamer
celcius = (4/5) * (kelvin-273)
print ("suhu adalah",reamer, "reamer")
#Fahrenheit
print ("suhu adalah",kelvin, "kelvin")