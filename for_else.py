# mencari huruf dalam kata
print("-" * 30)
print("mencari huruf dalam kata")
print("-" * 30)

kata = input("Masukan kata: ")
huruf_dicari = input("Masukan huruf yg dicari: ")

for huruf in kata:
    if huruf == huruf_dicari:
        print("Huruf", huruf_dicari, "ditemukan dalam kata!")
        break
else:
    print("Huruf", huruf_dicari, "TIDAK ditemukan dalam kata!")
