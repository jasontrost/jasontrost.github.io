#!/usr/bin/env python3
import struct
import io

def create_ico_file(size=32):
    """Create a simple ICO file with JT text on black background - large and centered"""

    # BMP header for 32x32 image
    width, height = size, size

    # Create pixel data for black background with white JT
    pixels = []

    # Create larger, centered JT letters
    for y in range(height):
        row = []
        for x in range(width):
            # Create bold JT pattern - much larger and centered
            if 7 <= y <= 23:  # Vertical range for letters
                # J shape - larger and bolder
                if ((9 <= x <= 11 and 7 <= y <= 20) or  # J vertical stem (3 pixels wide)
                    (9 <= x <= 15 and 7 <= y <= 9) or  # J top bar (3 pixels tall)
                    (5 <= x <= 9 and 18 <= y <= 20) or  # J bottom curve
                    (5 <= x <= 8 and 19 <= y <= 21)):  # J hook
                    row.append((255, 255, 255, 255))  # White
                # T shape - larger and bolder
                elif ((17 <= x <= 19 and 10 <= y <= 23) or  # T vertical stem (3 pixels wide)
                      (14 <= x <= 22 and 7 <= y <= 9)):  # T horizontal bar (3 pixels tall)
                    row.append((255, 255, 255, 255))  # White
                else:
                    row.append((26, 26, 26, 255))  # Dark gray (#1a1a1a)
            else:
                row.append((26, 26, 26, 255))  # Dark gray
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

print("Created favicon.ico with bold, centered JT design")