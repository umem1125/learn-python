umur = int(input("Masukan umur: "))
punya_sim = input("Punya SIM? (Ya/Tidak): ")

if umur >= 17 and punya_sim == "Ya":
    print("Boleh mengendarai motor!")
else:
    print("ANDA JOKOWI")