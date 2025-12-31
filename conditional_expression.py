angka = int(input("Masukan angka: "))
hasil = ""
# dengan if-else biasa:
# if angka > 0:
#     hasil = "Positif"
# else:
#     hasil = "Non-positif"

# dengan ternary operator (lebih singkat)
hasil = "Positif" if angka > 0 else "Non-positif"

print("Angka tersebut adalah =", hasil)