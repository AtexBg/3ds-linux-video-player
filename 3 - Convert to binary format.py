import os
from PIL import Image

def compile(image_path, output_path, rotate=False):
    img = Image.open(image_path)
    
    if rotate:
        img = img.rotate(270, expand=True)
    
    img = img.convert("RGB")
    
    pixels = img.load()
    width, height = img.size
    
    bin_data = []
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bin_data.append(chr(b))
            bin_data.append(chr(g))
            bin_data.append(chr(r))
    
    with open(output_path, "wb") as f:
        f.write(bytearray("".join(bin_data), "latin1"))
    print(f"Image saved as {output_path}.")

def process_files(in_dir, out_dir, rotate=False):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    for filename in os.listdir(in_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(in_dir, filename)
            output_path = os.path.join(out_dir, f"{os.path.splitext(filename)[0]}.bin")
            
            compile(image_path, output_path, rotate)

in_dir = 'cropped_frames'
out_dir = 'bin_frames'

process_files(in_dir, out_dir, rotate=True)
