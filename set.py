# set adalah kumpulan data yg tidak beraturan dan tidak memiliki elemen duplikat
# set ditulis dengan kurung kurawal {} atau dengan fungsi bawaan set()

# angka =  {1}

# angka.add(2)
# angka.add(3)
# angka.add(100)

buah = {"jeruk", "apel", "pisang"}
print(buah)

buah.add("mangga")
print(buah)
buah.remove("jeruk")
print(buah)

for i in buah:
    print(i)