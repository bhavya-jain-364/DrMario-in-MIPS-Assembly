from PIL import Image
import numpy as np

def convert_png_to_mapped_pixels(image_path, output_width, output_height):
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
            
            # Convert white to black
            if (r, g, b) == (255, 255, 255):
                r, g, b = 0, 0, 0
            
            # Convert RGB to 24-bit color value
            color_value = (r << 16) | (g << 8) | b
            
            # Append to results
            results.append((x, y, color_value))
    
    return results

# Example usage
image_path = "input_image.png"  # Replace with the path to your PNG
output_width = 10  # Desired width
output_height = 10  # Desired height

pixel_data = convert_png_to_mapped_pixels(image_path, output_width, output_height)

# Save in MIPS-compatible format
with open("pixel_data.asm", "w") as file:
    # Write the array size first
    file.write(f"# Array size: {len(pixel_data)}\n\n")
    
    # Write x-coordinates array
    file.write("x_coords: .word ")
    file.write(", ".join(str(x) for x, _, _ in pixel_data))
    file.write("\n\n")
    
    # Write y-coordinates array
    file.write("y_coords: .word ")
    file.write(", ".join(str(y) for _, y, _ in pixel_data))
    file.write("\n\n")
    
    # Write color values array
    file.write("colors: .word ")
    file.write(", ".join(str(color) for _, _, color in pixel_data))
    file.write("\n")

print(f"MIPS pixel data saved to 'pixel_data.asm'")
