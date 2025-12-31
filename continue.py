# continue digunakan untuk melanjutkan ke iterasi selanjutnya

print("-" * 50)
print("Mencetak angka ganjil saja")
print("-" * 50)

for i in range(21):
    if i % 2 ==  0: # Jika genap
        continue # Lewati, lanjut ke angka berikutnya
    print(i) # Hanya mencetak angka ganjil