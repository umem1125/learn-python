def tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan = 0
    while tebakan < maksimal_tebakan:
        tebakan += 1
        try:
            angka_user = int(input("Masukan angka: "))
            if angka_user > angka_acak:
                print("Angka terlalu besar")
            elif angka_user < angka_acak:
                print("Angka terlalu kecil")
            else:
                print("Selamat, anda benar")
                break
        except ValueError:
            print("Mohon masukan angka yg valid!")
    else:
        print("Kamu telah melewati batas maksimal tebakan anda.")
        print("Angka Acak adalah: ", angka_acak)
  
    input("Tekan enter untuk lanjut")

def app_menu():
    while True:
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")
        print("1. Tebak angka")
        print("2. Keluar")
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")

        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            tebak_angka()
        elif pilihan == 2:
            print("=== SELESAI ===")
            break
        else:
            print("Pilihan tidak valid")

app_menu()
        