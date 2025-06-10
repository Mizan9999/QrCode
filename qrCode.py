import qrcode
img = qrcode.make(input("Text : "))
type(img)  # qrcode.image.pil.PilImage
png_name = input("Save file name : ")
img.save(f"{png_name}.png")
print(f"{png_name}.png")