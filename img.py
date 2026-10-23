from PIL import Image
import random
width = 320
height = 180
for i in range(1, 7):
    col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    output = f"img_{i}.png"
    I = Image.new("RGB", (width, height), col)
    I.save("images/" + output)