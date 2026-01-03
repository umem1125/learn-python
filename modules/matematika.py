# modules matematika
"""mau pake module matematika"""

PI = 3.14159
NAMA_PEMBUAT = "Umem"

def tambah(a, b):
    """fungsi untuk penjumlahan"""
    return a + b

def kurang(a, b):
    """fungsi untuk pengurangan"""
    return a - b

def kali(a, b):
    """fungsi untuk perkalian"""
    return a * b

def bagi(a, b):
    """fungsi untuk pembagian"""
    if b != 0:
        return a / b
    else:
        print("Tidak Bisa Dibagi 0")

if __name__ == "__main__":
    print("Program ini tidak bisa dijalankan sebagai module")
