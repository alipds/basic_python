# 1
print("**Soal 1**")
nama = input("Nama: ")
umur = int(input("Umur: "))
tinggi = float(input("Tinggi: "))
print("Nama saya", nama, ", umur saya", umur, "tahun dan tinggi saya", tinggi, "cm.")
print("")

# 2
print("**Soal 2**")
r = int(input("Jari-jari lingkaran (cm): "))

luas_lingkaran = round((22/7)*(r**2), 2)

print("Luas lingkaran dengan jari-jari", r, "cm adalah", luas_lingkaran, "cm\u00b2")
print("")

# 3
print("**Soal 3**")
teori = float(input("Nilai ujian teori: "))
praktek = float(input("Nilai ujian praktek: "))

if teori >= 70 and praktek >= 70:
   print("Selamat, anda lulus!")
elif teori >= 70 and praktek < 70:
   print("Anda harus mengulang ujian praktek.")
elif teori < 70 and praktek >= 70:
   print("Anda harus mengulang ujian teori.")
else:
   print("Anda harus mengulang ujian teori dan praktek.")
print("")

# Bonus
print("**Soal Bonus**")
tinggi = int(input("Tinggi piramid: "))
spasi = tinggi - 1

for i in range(tinggi):
    for j in range(spasi):
        print(" ", end="")
    spasi -= 1
    for j in range(i + 1):
        print("* ", end="")
    print("")
