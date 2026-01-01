# tuple mirip dengan list, tetapi datanya tidak bisa  diubah setelah dibuat.
# tuple ditulis dengan kurung biasa ()

point = (5, 10)
print(point[0])
print(point[1])

print("-" * 30)
print("Untuk data yg tidak berubah!")
print("-" * 30)

tgl_lahir = (15, 8, 2000) # dd-mm-YYY
print("Tanggal lahir: ", tgl_lahir)

print("-" * 30)
print("Iterasi di Tuple!")
print("-" * 30)

for e in tgl_lahir:
    print(e)

print("-" * 30)
print("Iterasi di Tuple dengan index!")
print("-" * 30)

for i in range(len(tgl_lahir)):
    print(i)
