# operator aritmatika: digunakan untuk operasi matimatika

a = 10
b  = 3

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a // b)
print(a % b)


# operator assignment

a = 5
a += 10
print(a)

a = 5
a -= 10
print(a)

a = 5
a *= 10
print(a)

a = 5
a /= 10
print(a)

nama1 = "Jokowi"
nama2 = "Gibra"
nama3 = "Jokowi"

print(nama1 != nama2)
print(nama1 == nama3)
print(nama3 != nama2)
print(nama3 == nama1)

# operator khusus string
nama_depan = "Joko"
nama_blkng = "Widodo"
nama_lngkp = nama_depan + " "  + nama_blkng
print(nama_lngkp)

kali = "Helo"
print(kali  * 3)

garis = "-"
print(garis * 20)

kalimat = "Jokowi adalah pembohong"
print("Jokowi" in kalimat) # True
print("Joko" in kalimat) # True
print("wi" in kalimat) # True
print("Gibran" in kalimat) # False
print("pembohong" in kalimat) # True