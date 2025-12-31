hari = input("Masukan hari: ").lower() # dijadikan huruf kecil semua ketika diinput

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("KERJAA WOY")
    case "sabtu" | "minggu":
        print("LIBURRRRRRR COY")
    case _:
        print("NGETIK APAAN LU??")