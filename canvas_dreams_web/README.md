# Canvas Dreams Web Version

This is the web version of Canvas Dreams, an interactive art creation game. This version runs in a web browser using HTML5 Canvas and JavaScript.

## Features

All the features of the desktop version, plus:
- **Browser-based**: No need for Pygame installation
- **Accessible**: Works on any device with a modern web browser
- **Shareable**: Easy to share with others via URL
- **Familiar Interface**: Web-friendly UI with the same functionality

## Installation

### Prerequisites
- Python 3.x
- Flask

### Setup
1. Make sure you have Python installed
2. Install Flask:
   ```
   pip install flask
   ```

## Running the Web Version

1. Navigate to the canvas_dreams_web directory:
   ```
   cd canvas_dreams_web
   ```

2. Run the server:
   ```
   ./run.sh
   ```
   
   Or manually:
   ```
   python server.py
   ```

3. Open your web browser and go to:
   ```
   http://localhost:1313
   ```

## Controls

The web version supports the same controls as the desktop version:

### Mouse Controls
- **Left Mouse Button**: Draw on canvas
- **Right Mouse Button**: Change to a random color
- **Click on Color Palette**: Select specific colors
- **Click on Buttons**: Activate various functions

### Keyboard Shortcuts
- **1-4 Keys**: Switch between drawing modes
- **Up/Down Arrows**: Increase/decrease brush size
- **Left/Right Arrows**: Adjust symmetry (in kaleidoscope mode)
- **C Key**: Clear the canvas
- **S Key**: Save your artwork
- **B Key**: Toggle background color (black/white)
- **H Key**: Show/hide help overlay

## Technical Implementation

The web version uses:
- **HTML5 Canvas**: For drawing and rendering
- **JavaScript**: For game logic and interactivity
- **CSS**: For styling and layout
- **Flask**: For serving the web application

## Enjoy Creating!

Let your imagination flow and create beautiful digital art with Canvas Dreams!
