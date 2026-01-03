# main.py

import matematika

if __name__ == "__main__":
    # gunakan function dari modules
    hasil1 = matematika.tambah(6,9)
    hasil2 = matematika.kurang(19,7)
    hasil3 = matematika.kali(7,8)
    hasil4 = matematika.bagi(10,4)

    print("Hasil 6 + 9:", hasil1)
    print("Hasil 19 - 7:", hasil2)
    print("Hasil 7 x 8:", hasil3)
    print("Hasil 10 / 4:", hasil4)

    # Gunakan variables dari module
    print("Nilai PI:", matematika.PI)
    print("Created By:", matematika.NAMA_PEMBUAT)