# print("=== MENAMPILKAN DATA NILAI ===")

# file = open("nilai_siswa.txt", "r")

# for line in file:
#     data = line.strip().split(",")
#     print(data[0].capitalize(), ":", data[1])

# file.close()

# print("=== SELESAI ===")

# menggunakan with statement (diremokendasikan karena tidak perlu khawatir lagi dengan close())
print("=== MENAMPILKAN DATA NILAI ===")

try:
    with open("nilai_siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0].capitalize(), ":", data[1])
except FileNotFoundError:
    print("file nilai_siswa.txt tidak ditemukan")
print("=== SELESAI ===")