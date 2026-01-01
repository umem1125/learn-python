# function ditulis menggunakan def lalu diikuti nama function nya dan diakhiri dengan kurung buka dan tutup
# contoh def addItem():

def sayHi():
    print("Halo Jokowi")

# memanggil function
sayHi()

print("-" * 30)
print("Function dengan parameter!")
print("-" * 30)

def orang(name):
    print("halo..", name)
    print("Kapan diadili?")

orang("Jokowi")

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang: ", luas)

hitung_luas_persegi_panjang(220, 49)

print(" " * 30)
print("-" * 30)
print("Function dengan return value!")
print("-" * 30)
print(" " * 30)

# function dengan return value
def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas

luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(9)

print("Luas lingkaran 5: ", luas1)
print("Luas lingkaran 9: ", luas2)

print(" " * 30)
print("-" * 30)
print("Function dengan default value/parameter!")
print("-" * 30)
print(" " * 30)
# Function dengan default value/parameter
def presiden(nama = "Jokowi"):
    print("Haloooo pak pres! ", nama)

presiden()

print(" " * 30)
print("-" * 30)
print("Function argument!")
print("-" * 30)
print(" " * 30)

def perkenalan(nama, umur, kota):
    print("Nama: ", nama)
    print("Umur: ", umur)
    print("Kota: ", kota)

# Positional arguments (urutan  harus seuuai)
perkenalan("Jokowi", 66, "Solo")

# Keyword arguments (urutan  bebas)
perkenalan(nama="Gibran", kota="Tegal", umur=90)

def buat_profile(nama, umur, kota="Solo", pekerjaan="Koruptor"):
    print(f"=== PROFIL {nama.upper()} ===")
    print(f"Umur: {umur} tahun")
    print(f"Kota: {kota}")
    print(f"Pekerjaan: {pekerjaan}")

buat_profile("jokowi", 88)
buat_profile("gibran", 34, kota="Tegal", pekerjaan="Anaknya Jokowi")

print("-" * 30)
print("Function dengan parameter  dinamis!")
print("-" * 30)

# item = ()
def cetak_list(*list):
    for item in list:
        print(item)

cetak_list("Joko",2,3,4,5,6)

def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

cetak_dict(nama="Bobi", umur=26, kota="Solo")