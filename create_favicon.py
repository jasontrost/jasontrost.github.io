#!/usr/bin/env python3
import struct
import io

def create_ico_file(size=32):
    """Create an ICO file with serif-style JT on black background"""

    # BMP header for 32x32 image
    width, height = size, size

    # Create pixel data for black background with white JT
    pixels = []

    # Create serif-style JT pattern
    for y in range(height):
        row = []
        for x in range(width):
            # Black background
            pixel = (0, 0, 0, 255)

            # J letter with serifs (positioned on left)
            # J top serif
            if 8 <= y <= 9 and 11 <= x <= 15:
                pixel = (255, 255, 255, 255)
            # J vertical stem
            elif 8 <= y <= 20 and 12 <= x <= 13:
                pixel = (255, 255, 255, 255)
            # J curve at bottom
            elif 19 <= y <= 20 and 10 <= x <= 12:
                pixel = (255, 255, 255, 255)
            elif 20 <= y <= 21 and 9 <= x <= 12:
                pixel = (255, 255, 255, 255)
            elif 21 <= y <= 22 and 9 <= x <= 11:
                pixel = (255, 255, 255, 255)

            # T letter with serifs (positioned on right)
            # T top bar
            elif 8 <= y <= 9 and 16 <= x <= 23:
                pixel = (255, 255, 255, 255)
            # T vertical stem
            elif 8 <= y <= 23 and 19 <= x <= 20:
                pixel = (255, 255, 255, 255)
            # T bottom serifs
            elif 22 <= y <= 23 and 17 <= x <= 22:
                pixel = (255, 255, 255, 255)

            row.append(pixel)
        pixels.append(row)

    # Create ICO file structure
    ico_header = struct.pack('<HHH', 0, 1, 1)  # Reserved, Type (1=ICO), Count

    # Image directory entry
    img_offset = 6 + 16  # Header + one directory entry
    dir_entry = struct.pack('<BBBBHHII',
        width if width < 256 else 0,  # Width
        height if height < 256 else 0,  # Height
        0,  # Color palette
        0,  # Reserved
        1,  # Color planes
        32,  # Bits per pixel
        width * height * 4 + 40,  # Image size (pixels + DIB header)
        img_offset  # Image offset
    )

    # DIB header (BITMAPINFOHEADER)
    dib_header = struct.pack('<IiiHHIIIIII',
        40,  # Header size
        width,  # Width
        height * 2,  # Height (doubled for AND mask)
        1,  # Planes
        32,  # Bits per pixel
        0,  # Compression (BI_RGB)
        width * height * 4,  # Image size
        0,  # X pixels per meter
        0,  # Y pixels per meter
        0,  # Colors used
        0   # Important colors
    )

    # Convert pixels to bytes (BGRA format, bottom-up)
    pixel_data = b''
    for y in range(height - 1, -1, -1):
        for x in range(width):
            r, g, b, a = pixels[y][x]
            pixel_data += struct.pack('BBBB', b, g, r, a)

    # AND mask (all transparent)
    and_mask_size = ((width + 31) // 32) * 4 * height
    and_mask = b'\x00' * and_mask_size

    # Combine all parts
    ico_data = ico_header + dir_entry + dib_header + pixel_data + and_mask

    return ico_data

# Create and save the ICO file
ico_data = create_ico_file(32)
with open('favicon.ico', 'wb') as f:
    f.write(ico_data)

print("Created favicon.ico with elegant serif JT design")