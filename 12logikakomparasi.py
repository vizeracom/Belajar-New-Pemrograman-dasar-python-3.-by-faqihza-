#Episode Logika dan Komparasi

#membuat gabungan area rentang dari angka

#++++++++3--------10+++++++++
InputUser = float(input("Masukan angka yang bernilai \nkurang dari 3 \natau lebih dari 10\n: "))

#Memeriksa Kurang dari 3
isUserKurang = (InputUser < 3)
print ("Kurang dari 3 = ",isUserKurang)

#Memeriksa lebih dari 10
isUserLebih = (InputUser > 10)
print ("Lebih dari 10 = ", isUserLebih)

#Gabungan ++++3------10+++++++
isCorrect = isUserKurang or isUserLebih
print (" Hasilnya = ", isCorrect)

#--------3++++++++10----------
InputUser = float(input("Masukan angka yang bernilai \nLebih dari 3 \natau Kurang dari 10\n: "))
#Memeriksa lebih dari 3
#-----------3+++++++++++
isUserLebih3 = (InputUser > 3)
print ("Lebih dari 3 = ", isUserLebih3)

#memeriksa kurang dari 10
#+++++++++++10----------
isUserKurang10 = (InputUser < 10)
print ("Kurang dari 10 = ", isUserKurang10)

#Gabungan ----3+++++++10--------
isCorrect = isUserLebih3 and isUserKurang10
print (" Hasilnya = ", isCorrect)
