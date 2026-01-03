import qrcode

"""Operasi Dasar Gambar"""
# pastikan ada gambar untuk demo
print("=== IMAGE PROCESSING DEMO ===")

img = qrcode.make("https://github.com/umem1125")
img.save("qrcode.png")