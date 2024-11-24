from PIL import Image
import numpy as np
import os

def convert_png_to_mapped_pixels(image_path, output_width, output_height, x_offset=0, y_offset=0):
    # Load the image
    image = Image.open(image_path).convert("RGB")
    
    # Resize image to specified dimensions
    resized_image = image.resize((output_width, output_height), Image.Resampling.LANCZOS)
    print(resized_image)
    # Convert the image to numpy array
    pixel_array = np.array(resized_image)
    
    # Process pixels
    results = []
    for y in range(output_height):
        for x in range(output_width):
            r, g, b = pixel_array[y, x]
            
            # # Convert white to black
            # if (r, g, b) == (255, 255, 255):
            #     r, g, b = 0, 0, 0
            
            # Convert RGB to hexadecimal format
            color_value = f"0x{r:02x}{g:02x}{b:02x}"
            
            # Add offsets to coordinates
            offset_x = x + x_offset
            offset_y = y + y_offset
            
            # Append to results with offset coordinates
            results.append((offset_x, offset_y, color_value))
    
    return results

# Example usage
image_path = "paused.png"  # Replace with the path to your PNG
output_width =  40 # Desired width
output_height = 7  # Desired height
x_offset = 12  # Starting X position in bitmap
y_offset = 0  # Starting Y position in bitmap

pixel_data = convert_png_to_mapped_pixels(image_path, output_width, output_height, x_offset, y_offset)

# Create output filename by replacing .png with .asm
output_path = os.path.splitext(image_path)[0] + '.asm'

# Save in MIPS-compatible format
with open(output_path, "w") as file:
    # Write x-coordinates array
    file.write("x_coords: .word ")
    file.write(", ".join(str(x) for x, _, _ in pixel_data))
    file.write("\n\n")
    
    # Write y-coordinates array
    file.write("y_coords: .word ")
    file.write(", ".join(str(y) for _, y, _ in pixel_data))
    file.write("\n\n")
    
    # Write color values array with hex format
    file.write("colors: .word ")
    file.write(", ".join(color for _, _, color in pixel_data))
    file.write("\n")

print(f"MIPS pixel data saved to '{output_path}'")
