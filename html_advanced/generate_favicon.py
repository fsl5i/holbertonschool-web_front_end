from PIL import Image

img = Image.open("favicon.jpg")
img.save("favicon.ico", format="ICO", sizes=[(32,32)])
img.save("favicon.png", format="PNG")
