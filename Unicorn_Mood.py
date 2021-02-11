import time
import picounicorn

picounicorn.init()

# From CPython Lib/colorsys.py
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0)
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

width = picounicorn.get_width()   #16 
height = picounicorn.get_height() #7

hue = 0.0
while not picounicorn.is_pressed(picounicorn.BUTTON_B):
    while picounicorn.is_pressed(picounicorn.BUTTON_A):
        print(hue)
        r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
        for x in range(width):
            for y in range(height):
                picounicorn.set_pixel(x, y, r, g, b)
        hue += 0.01
        if hue > 1.1:
            hue = 0.0
        time.sleep_ms(50)

# Clear the display
for x in range(width):
    for y in range(height):
        picounicorn.set_pixel(x, y, 0, 0, 0)

print("Stopped!")
        