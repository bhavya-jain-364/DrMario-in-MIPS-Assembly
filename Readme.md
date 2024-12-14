# Dr. Mario Assembly Implementation

A MIPS assembly implementation of the classic Nintendo game Dr. Mario, featuring custom sprites, background music, and authentic gameplay mechanics.

![Dr Mario Game](game.png)

## Overview

This project recreates Dr. Mario in MIPS assembly, implementing core gameplay mechanics while adding unique visual touches and sound effects. The game features custom-designed sprites created on pixilart.org and converted using a custom Python script.

## Features

### Implemented Milestones
- **Core Mechanics**
  - Capsule movement and rotation
  - Virus elimination system
  - Color matching logic
  - Collision detection

- **Advanced Features**
  - Gravity simulation with increasing speed
  - Game over and retry functionality
  - Pause system with visual display
  - Background music implementation
  - Custom sprite rendering for Dr. Mario and viruses

### Audio System
- Background music using MIDI conversion
- Sound effects for:
  - Capsule movement
  - Capsule rotation
  - Game over states

## Controls
- `W` - Rotate capsule
- `A` - Move left
- `S` - Move down (fast drop)
- `D` - Move right
- `P` - Pause game
- `Q` - Quit game
- `R` - Restart game

## Technical Implementation

### Graphics Pipeline
- Sprites designed on pixilart.org
- Custom Python script (`png_to_mips.py`) for sprite conversion:
  ```python
  def convert_png_to_mapped_pixels(image_path, output_width, output_height, x_offset=0, y_offset=0):
      # Converts PNG images to MIPS-compatible pixel arrays
      # Outputs coordinate and color data in assembly format
  ```
- Unique visual elements:
  - Custom Dr. Mario sprite with ginger hair
  - Attempted Goomba artwork on medicine bottle
  - Modified color palette for better visibility

### Display Configuration
- Resolution: 64x128 pixels
- Unit size: 1x1 pixel
- Base Address: 0x10008000

### Sound Implementation
- MIDI file conversion to component arrays:
  - Duration
  - Timing
  - Velocity
  - Instrument
- Real-time playback using MIPS syscalls

## Setup Instructions

1. Install Saturn MIPS simulator
2. Clone this repository
3. Configure display settings:
   - Width: 64 pixels
   - Height: 128 pixels
   - Unit Size: 1x1
   - Base Address: 0x10008000

## Project Structure

```
.
├── drmario.asm              # Main game logic
├── Resources/
│   ├── data/               # Sprite and sound data
│   └── png_to_mips.py      # Sprite conversion utility
├── LICENSE                 # MIT License
└── README.md              # This file
```

## Development Tools

- pixilart.org for sprite design
- Custom Python scripts for asset conversion
- Saturn MIPS simulator for development and testing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Bhavya Jain

---

*Note: This is an educational project created for learning purposes and is not affiliated with Nintendo or the original Dr. Mario game.* 