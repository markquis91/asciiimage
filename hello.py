from PIL import Image
with Image.open("oddrey.jpeg") as od:
    print("Successfully loaded image!")
    print(od.height, 'x', od.width)