# break digunakan untuk keluar dari perulangan


print("-" * 50)
print("Game tebak angka dengan break")
print("-" * 50)

angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka (1-10):"))

    if tebakan == angka_rahasia:
        print("Selamat anda BENAR")
        break
    else:
        print("Salah, coba  lagi!")
print("PROGRAM FINISH")
