# Canvas Dreams - Interactive Art Creation Game


Canvas Dreams is an interactive art creation game that allows users to create beautiful digital artwork. With multiple drawing modes, particle effects, and customization tools, Canvas Dreams offers an engaging creative experience for everyone.

## Key Features

### Professional Interface
- **Sidebar**: Contains all controls and options
- **Canvas Area**: Clearly separated with borders
- **Color Palette**: Located at the bottom for easy color selection
- **Help System**: Displays detailed instructions when needed

### Multiple Drawing Modes
- **Standard Drawing**: Basic drawing with high precision
- **Spray Paint**: Creates soft spray effects with particle system
- **Kaleidoscope**: Automatically generates beautiful symmetrical patterns
- **Gravity**: Creates fountain-like effects with physics-based particles

### Flexible Customization
- Adjustable brush sizes
- Rich color palette
- Adjustable symmetry levels for kaleidoscope mode
- Toggle between black and white backgrounds

### Two Versions
- **Desktop Version**: Uses Pygame, runs as a standalone application
- **Web Version**: Uses HTML5 Canvas, runs in a web browser

## Installation

### System Requirements
- Python 3.x
- Pygame (for desktop version)
- Flask and Werkzeug (for web version)

### Installation Steps
1. Clone this repository:
   ```
   git clone https://github.com/vanhoangkha/Build-Games-with-Amazon-Q-CLI.git
   ```

2. Navigate to the project directory:
   ```
   cd Build-Games-with-Amazon-Q-CLI
   ```

3. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install required libraries:
   ```
   pip install pygame
   ```

   For the web version, install additional libraries:
   ```
   pip install flask==2.0.1 werkzeug==2.0.1
   ```

## Running the Game

### Desktop Version
1. Navigate to the canvas_dreams directory:
   ```
   cd canvas_dreams
   ```

2. Run the run.sh script:
   ```
   ./run.sh
   ```

   Or run directly:
   ```
   python main.py
   ```

### Web Version
1. Navigate to the canvas_dreams_web directory:
   ```
   cd canvas_dreams_web
   ```

2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

3. Run the run.sh script:
   ```
   ./run.sh
   ```

   Or run directly:
   ```
   python server.py
   ```

4. Open your web browser and go to:
   ```
   http://localhost:1313
   ```

## User Guide

### Mouse Controls
- **Left Mouse Button**: Draw on canvas
- **Right Mouse Button**: Change to random color
- **Click on Color Palette**: Select specific color
- **Click on Buttons**: Activate various functions

### Keyboard Shortcuts
| Key | Function |
|-----|----------|
| 1-4 | Switch between drawing modes |
| Up/Down Arrows | Increase/decrease brush size |
| Left/Right Arrows | Adjust symmetry level (in kaleidoscope mode) |
| C | Clear canvas |
| S | Save artwork as PNG |
| B | Toggle background color (black/white) |
| H | Show/hide help |

### Drawing Modes
1. **Standard Drawing (key 1)**: Basic drawing mode with continuous strokes
2. **Spray Paint (key 2)**: Creates spray effects with small particles
3. **Kaleidoscope (key 3)**: Creates symmetrical patterns around the canvas center
4. **Gravity (key 4)**: Creates fountain-like effects with particles affected by gravity

## Creative Tips

- Combine multiple drawing modes for unique effects
- Experiment with different symmetry levels in kaleidoscope mode
- Use different brush sizes within the same artwork
- Try both black and white backgrounds for contrast effects
- Save your work frequently to build a collection

## Troubleshooting

### Desktop Version
- **ALSA Audio Errors**: Resolved by disabling audio in the source code
- **Interface Not Displaying**: Check Pygame installation and Python environment

### Web Version
- **ImportError with Flask**: Ensure correct versions of Flask and Werkzeug are installed
  ```
  pip install flask==2.0.1 werkzeug==2.0.1
  ```
- **Cannot access localhost:1313**: Check if the server is running and no other application is using port 1313

## Technical Information

### Technologies Used
- **Desktop Version**: Python, Pygame
- **Web Version**: HTML5, CSS, JavaScript, Flask

### Project Structure
```
Build-Games-with-Amazon-Q-CLI/
├── canvas_dreams/           # Desktop version
│   ├── main.py              # Main source code
│   ├── run.sh               # Game run script
│   └── README.md            # Instructions
│
├── canvas_dreams_web/       # Web version
│   ├── server.py            # Flask server
│   ├── requirements.txt     # Required libraries
│   ├── run.sh               # Server run script
│   ├── templates/           # HTML templates
│   │   └── index.html
│   ├── static/              # Static resources
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── canvas_dreams.js
│   └── README.md            # Instructions
│
└── README.md                # Main documentation
```

## Future Development

Planned features for future development:
- Animation recording capabilities
- Additional drawing modes and effects
- Layer system for complex artwork
- Collaborative drawing features
- Custom brush shapes
- Mobile optimization

## About the Project

Canvas Dreams was developed to demonstrate how Amazon Q CLI can assist in building creative applications. This project exemplifies how AI can help create interactive games with professional user interfaces and rich features.

## Author

Developed with the assistance of Amazon Q CLI.

## License

Source code is provided for educational and non-commercial purposes.

## Let Your Creativity Flow!

Let your imagination soar and create beautiful digital artwork with Canvas Dreams!
