# Dictionary menyimpan data dalam pasangan key-value, mirip seperti Object pada JSON dalam bahasa  pemrograman yg lain
# Dictionary ditulis dengan kurung kurawal {}

# [] kurung kotak untuk List
# () kurung bulat/biasa untuk Tuple
# {} kurung kurawal untuk Dictionary

print("-" * 30)
print("Data Siswa!")
print("-" * 30)

siswa = {
    "nama": "Jokowi",
    "umur": 78,
    "alamat": "Solo",
    "menikah": True
}

siswa["umur"] = 61 # mengubah value
# del siswa["umur"] # menghapus value

print("Namanya: ", siswa["nama"])
print("Umurnya: ", siswa["umur"])
print("Alamat: ", siswa["alamat"])
print("Menikah: ", siswa["menikah"])

print("-" * 30)
print("Mengiterasi Dictionary!")

for key in siswa:
    print(key, ":", siswa[key])

print("-" * 30)
print("Mengiterasi Key-Value pairs!")

for key, value in siswa.items():
    print(key, "=", value)