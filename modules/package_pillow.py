from PIL import Image, ImageDraw

"""Operasi Dasar Gambar"""
# pastikan ada gambar untuk demo
print("=== IMAGE PROCESSING DEMO ===")

# buat gambar baru
img = Image.new('RGB', (400, 300), color='lightblue')

# tambahkan teks
draw = ImageDraw.Draw(img)
draw.text((50,50), "Hello  PIL!", fill='black')
draw.rectangle([50, 100, 350, 200], outline='red', width=3)
draw.ellipse([100,150,300,250], fill='yellow')

# simpan gambar
img.save("demo_img.png")
print("demo_img has been created.")