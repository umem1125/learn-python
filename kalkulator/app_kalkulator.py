def penjumlahan():
    try:
        angka1 = int(input("Masukan angka 1: "))
        angka2 = int(input("Masukan angka 2: "))
        hasil = angka1 + angka2
        print("Hasil penjumlahan: ", hasil)
    except ValueError:
        print("Mohon masukan angka yg valid!")
    except:
        print("Something went wrong")
    print("=== PROGRAM SELESAI ===")
    


def pengurangan():
    try:
        angka1 = int(input("Masukan angka 1: "))
        angka2 = int(input("Masukan angka 2: "))
        hasil = angka1 - angka2
        print("Hasil pengurangan: ", hasil)
    except ValueError:
        print("Mohon masukan angka yg valid!")
    except:
        print("Something went wrong")
    print("=== PROGRAM SELESAI ===")

def perkalian():
    try:
        angka1 = int(input("Masukan angka 1: "))
        angka2 = int(input("Masukan angka 2: "))
        hasil = angka1 * angka2
        print("Hasil perkalian: ", hasil)
    except ValueError:
        print("Mohon masukan angka yg valid!")
    except:
        print("Something went wrong")
    print("=== PROGRAM SELESAI ===")

def pembagian():
    try:
        angka1 = int(input("Masukan angka 1: "))
        angka2 = int(input("Masukan angka 2: "))
        hasil = angka1 / angka2
        print("Hasil pembagian: ", hasil)
    except ValueError:
        print("Mohon masukan angka yg valid!")
    except ZeroDivisionError:
        print("Tidak bisa dibagi dengan Nol!")
    except:
        print("Something went wrong")
    print("=== PROGRAM SELESAI ===")

def app_menu():
    print("PROGRAM KALKULATOR SEDERHANA")
    print("1. Penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. Keluar")

    while True:
        pilihan = int(input("Pilihan: "))
        if pilihan == 1:
            penjumlahan()
        elif pilihan == 2:
            pengurangan()
        elif pilihan == 3:
            perkalian()
        elif pilihan == 4:
            pembagian()
        elif pilihan == 5:
            print("KELUAR")
            break

app_menu()