import json

file = open("contoh.json", "r")
text = file.read()
file.close()

print(text)

murid = json.loads(text)
print(type(murid)) # jadi dictionary/dict
print(murid.get("nama"))
print(murid.get("umur"))
print(murid.get("lahir"))

# bikin json
sekolah = {
    "nama": "Universitas Joko Widodo",
    "alamat": "jl. Lingkar Solo",
    "telp": 1129990,
    "jurusan": [
        "Teknik Korupsi",
        "Teknik 3 Periode"
    ]
}

text_json = json.dumps(sekolah)
print(text_json)

# jadiin file .txt
# file = open("sekolah.txt", "w")

# jadiin file .json
file = open("owi.json", "w")
file.write(text_json)
file.close()