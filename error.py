# penanganan error

# print("=== APLIKASI KALKULATOR ===")

# try:
#     angka1 = int(input("Masukan angka 1: "))
#     angka2 = int(input("Masukan angka 2: "))
#     hasil = angka1 + angka2
#     print("Hasil: ", hasil)
# except:
#     print("Something went wrong")

# print("=== PROGRAM SELESAI ===")

# spesifik error
# print("=== APLIKASI KALKULATOR ===")

# try:
#     angka1 = int(input("Masukan angka 1: "))
#     angka2 = int(input("Masukan angka 2: "))
#     hasil = angka1 / angka2
#     print("Hasil: ", hasil)
# except ValueError:
#     print("Mohon masukan angka yg valid!")
# except ZeroDivisionError:
#     print("Tidak bisa dibagi dengan Nol!")
# except:
#     print("Something went wrong")

# print("=== PROGRAM SELESAI ===")

# error try-except-else

print("=== APLIKASI KALKULATOR ===")

try:
    angka = int(input("Masukan angka: "))
except ValueError:
    print("Input harus angka!")
else:
    print("Angka yg anda masukan adalah: ", angka)
    if angka > 0:
        print("Angka Positif")
    elif angka < 0:
        print("Angka Negatif")
    else:
        print("ANDA JOKOWI, O")
finally:
    print("=== PROGRAM SELESAI ===")
