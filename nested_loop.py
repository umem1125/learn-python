# perulangan bersarang

print("-" * 30)
print("Tabel perkalian lengkap!")
print("-" * 30)

print("Tabel Perkalian 1-5: ")
for i in  range(1,  11):
    for j in range(1, 11):
        hasil = i * j
        print(i, "x", j, "=", hasil)
    print("---")