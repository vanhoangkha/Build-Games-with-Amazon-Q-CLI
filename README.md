# Building Games with Amazon Q CLI

This project demonstrates how Amazon Q CLI can help you build creative applications like games. In this example, we've created "Canvas Dreams" - an interactive art creation game using Pygame.

![Canvas Dreams](https://placeholder-for-screenshot.png)

## How Amazon Q Helped

Amazon Q CLI assisted in:

1. **Project Setup**: Created the project structure and virtual environment
2. **Dependency Management**: Installed and configured Pygame
3. **Code Generation**: Created the game code with multiple drawing modes and features
4. **UI Design**: Built an intuitive user interface with sidebar, buttons, and controls
5. **Documentation**: Generated comprehensive README files and instructions
6. **Troubleshooting**: Fixed audio initialization issues for environments without sound hardware

## Canvas Dreams Game

Canvas Dreams is an interactive art creation game with a modern UI that allows users to:

### Features
- **Professional Interface**: Sidebar with controls, dedicated canvas area, and color palette
- **Multiple Drawing Modes**: Standard drawing, spray paint, kaleidoscope patterns, and gravity effects
- **Customization Options**: Adjustable brush sizes, symmetry levels, and background colors
- **Interactive Controls**: Both button-based UI and keyboard shortcuts
- **Help System**: Built-in help overlay with instructions
- **Artwork Saving**: Save your creations as PNG files

### Technical Highlights
- Particle systems with physics simulation
- Symmetrical pattern generation algorithms
- Interactive UI with button components
- Color manipulation and blending effects
- Canvas isolation for clean exports

## Installation

### Prerequisites
- Python 3.x
- Pygame library

### Setup
1. Clone this repository:
   ```
   git clone https://github.com/vanhoangkha/Build-Games-with-Amazon-Q-CLI.git
   ```
2. Create a virtual environment and install dependencies:
   ```
   cd Build-Games-with-Amazon-Q-CLI
   python3 -m venv venv
   source venv/bin/activate
   pip install pygame
   ```

## Running the Game

To run the game:

1. Navigate to the canvas_dreams directory
2. Execute the run.sh script:
   ```
   cd canvas_dreams
   ./run.sh
   ```

## Game Controls

### Mouse Controls
- **Left Mouse Button**: Draw on canvas
- **Right Mouse Button**: Change to a random color
- **Click on Color Palette**: Select specific colors
- **Click on Buttons**: Activate various functions

### Keyboard Shortcuts
- **1-4 Keys**: Switch between drawing modes
- **Up/Down Arrows**: Increase/decrease brush size
- **Left/Right Arrows**: Decrease/increase symmetry (in kaleidoscope mode)
- **C Key**: Clear the canvas
- **S Key**: Save your artwork
- **B Key**: Toggle background color (black/white)
- **H Key**: Show/hide help overlay

## Interface Elements

- **Sidebar**: Contains all controls and mode selections
- **Canvas Area**: The main drawing space
- **Color Palette**: Located at the bottom for easy color selection
- **Mode Buttons**: Select between different drawing styles
- **Tool Buttons**: Access functions like clear, save, and help
- **Size Controls**: Adjust brush size and symmetry levels

## Development Journey

This project showcases how Amazon Q CLI can assist in creative application development:

1. **Initial Concept**: Started with a basic idea for an art creation game
2. **Core Implementation**: Built the fundamental drawing mechanics and particle systems
3. **UI Enhancement**: Added a professional interface with controls and visual feedback
4. **Refinement**: Fixed issues and optimized for different environments
5. **Documentation**: Created comprehensive guides and instructions

## Future Enhancements

Potential features for future development:
- Animation recording capabilities
- Additional drawing modes and effects
- Layer system for complex artwork
- Collaborative drawing features
- Custom brush shapes and patterns

## Enjoy Creating!

Let your imagination flow and create beautiful digital art with Canvas Dreams!
