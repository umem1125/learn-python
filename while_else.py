print("-" * 50)
print("Mencari password yg benar dengan batas percobaan")
print("-" * 50)

password_benar = "rahasia"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("masukan password: ")
    percobaan += 1

    if password == password_benar:
        print("Login berhasil!")
        break
    else:
        print("Password salah. Sisa Percobaan: ", max_percobaan - percobaan)
else:
    print("Terlalu banyak percobaan gagal. Akses ditolak!")
