import time
import picounicorn
import framebuf

picounicorn.init()

def rgb565_to_rgb888(rgb565):
        r8 = (((rgb565 & 0xf800) >> 11) * 527 + 23 ) >> 6
        g8 = (((rgb565 & 0x07e0) >> 5) * 259 + 33 ) >> 6
        b8 = ((rgb565 & 0x001f) * 527 + 23 ) >> 6
        return r8, g8, b8

width = picounicorn.get_width()   #16 
height = picounicorn.get_height() #7

# FrameBuffer needs 2 bytes for every RGB565 pixel
buf_width = width * 7
fbuf = framebuf.FrameBuffer(bytearray(buf_width * height * 2), buf_width, height, framebuf.RGB565)
fbuf.fill(0)
fbuf.text('Hello World!', 16, 0, 0xf81f)

scroll_width = 0

while scroll_width < buf_width:
    for x in range(width):
        for y in range(height):
            r, g, b = rgb565_to_rgb888(fbuf.pixel(x, y))
            picounicorn.set_pixel(x, y, r, g, b)

    fbuf.scroll(-1,0)
    scroll_width += 1
    time.sleep_ms(75)