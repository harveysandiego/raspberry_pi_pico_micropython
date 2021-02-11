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

width = picounicorn.get_width()
height = picounicorn.get_height()

print("Running!")

while not picounicorn.is_pressed(picounicorn.BUTTON_A):  # Wait for Button A to be pressed
    # Scroll red across
    for x in range(width):
        for y in range(height):
            r, g, b = [int(c * 255) for c in hsv_to_rgb(x / width, 1.0, 1.0)]
            picounicorn.set_pixel(x, y, r, g, b)
        time.sleep_ms(50)
        
    # Clear the display
    for x in range(width):
        for y in range(height):
            picounicorn.set_pixel(x, y, 0, 0, 0)
        time.sleep_ms(50)

for x in range(width):
    for y in range(height):
        picounicorn.set_pixel(x, y, 0, 0, 0)

print("Ended!")