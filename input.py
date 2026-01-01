# w = write -> membaca file yg sudah ada
# r = read -> menulis file baru atau menimpa file lama
# a = append -> menambahkan data di akhir file
# x = create -> membuat file  baru,  error jika sudah ada

print("=== SIMPAN DATA NILAI ===")

file = open("nilai_siswa.txt", "w")

while True:
    nama = input("Masukan nama siswa (tekan enter  untuk selesai): ")
    if nama == "":
        break

    nilai = input("Nilai: ")

    # tulis ke file
    file.write(nama  + "," + nilai + "\n")
    print("Data", nama, "berhasil disimpan!")

file.close()
print("Semua  data berhasil disimpan ke nilai_siswa.txt")