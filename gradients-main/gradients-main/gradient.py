import sys
import struct

def clamp(value):
    return max(0, min(255, value))

def parse_color_point(point):
    coords, color = point.split('=')
    x, y = map(int, coords.split(','))
    r, g, b = map(int, color.split(','))
    return (x, y), (clamp(r), clamp(g), clamp(b))

def linear_interpolate(color1, color2, t):
    return (
        clamp(int(color1[0] + (color2[0] - color1[0]) * t)),
        clamp(int(color1[1] + (color2[1] - color1[1]) * t)),
        clamp(int(color1[2] + (color2[2] - color1[2]) * t))
    )

def create_gradient(point1, color1, point2, color2):
    width, height = 100, 100
    image = []

    for y in range(height):
        for x in range(width):
            dx = point2[0] - point1[0]
            dy = point2[1] - point1[1]
            if dx == 0 and dy == 0:
                t = 0
            else:
                t = ((x - point1[0]) * dy - (y - point1[1]) * dx) / (dx * dy + dy * dx)

            t = clamp(int(t * 255)) / 255.0
            color = linear_interpolate(color1, color2, t)
            image.append(color)

    return image

def write_bmp(filename, image):
    width, height = 100, 100
    row_size = (width * 3 + 3) // 4 * 4
    padding_size = row_size - width * 3
    
    bmp_file_header = struct.pack('<2sIHHIiiiHHIIII',
                                   b'BM',  # Signature
                                   54 + row_size * height,  # File size
                                   0,  # Reserved1
                                   0,  # Reserved2
                                   54,  # Offset to pixel data
                                   40,  # DIB header size
                                   width,  # Width
                                   height,  # Height (negative for top-down bitmap)
                                   1,  # Number of color planes
                                   24,  # Bits per pixel
                                   0,  # Compression
                                   row_size * height,  # Image size
                                   0,  # Horizontal resolution
                                   0)  # Vertical resolution

    with open(filename, 'wb') as f:
        f.write(bmp_file_header)

        for y in range(height):
            for x in range(width):
                r, g, b = image[y * width + x]
                f.write(struct.pack('BBB', b, g, r)) 
            f.write(b'\x00' * padding_size)

def main():
    if len(sys.argv) < 4:
        print("Usage: python gradient.py x1,y1=r1,g1,b1 x2,y2=r2,g2,b2 -o output.bmp")
        return

    point1, color1 = parse_color_point(sys.argv[1])
    point2, color2 = parse_color_point(sys.argv[2])
    output_file = sys.argv[4]

    gradient_image = create_gradient(point1, color1, point2, color2)
    write_bmp(output_file, gradient_image)

if __name__ == "__main__":
    main()
