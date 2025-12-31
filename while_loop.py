# While loop mengulang kode selama kondisi tertentu masih bernilai True

# print("-" * 30)
# print("mencetak angka 1 sampai 5")
# print("-" * 30)
# angka = 1
# while angka <= 5:
#     print(angka)
#     angka += 1

print("-" * 30)
print("Input sampai benar!")
print("-" * 30)
password = ""
while password != "rahasia":
    password = input("Masukan password: ")
    if password != "rahasia":
        print("Password salah, anda JOKOWI")

print("Password anda benar:", password)