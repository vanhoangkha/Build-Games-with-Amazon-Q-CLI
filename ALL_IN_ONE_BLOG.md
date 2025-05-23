# Canvas Dreams: Building a Creative Art Game with Amazon Q CLI - A Complete Guide

## Introduction

In this comprehensive guide, I'll walk you through my journey of creating Canvas Dreams, an interactive art creation game, using Amazon Q CLI. We'll cover everything from initial setup to deployment, including both desktop and web versions of the game.

![Canvas Dreams](https://placeholder-for-screenshot.png)

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setting Up Your Environment](#setting-up-your-environment)
3. [Building the Desktop Version](#building-the-desktop-version)
4. [Creating the Web Version](#creating-the-web-version)
5. [Game Features and Implementation](#game-features-and-implementation)
6. [Troubleshooting Common Issues](#troubleshooting-common-issues)
7. [Future Development](#future-development)

## Project Overview

Canvas Dreams is an interactive art creation game that lets users express their creativity through various drawing modes and effects. The project demonstrates how Amazon Q CLI can assist in building creative applications efficiently.

### Key Features
- Multiple drawing modes (Standard, Spray, Kaleidoscope, Gravity)
- Real-time particle effects
- Symmetrical pattern generation
- Professional UI with sidebar controls
- Cross-platform support (Desktop and Web)

## Setting Up Your Environment

### 1. Installing Amazon Q CLI
```bash
# Install AWS CLI first
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Install Amazon Q CLI
curl -L https://d2eo22ngex1n9g.cloudfront.net/Documentation/CLI/q-cli-installer.sh | sh

# Configure
aws configure
q configure
```

### 2. Project Setup
```bash
# Create project directory
mkdir Build-Games-with-Amazon-Q-CLI
cd Build-Games-with-Amazon-Q-CLI

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pygame
pip install flask==2.0.1 werkzeug==2.0.1
```

## Building the Desktop Version

### 1. Initial Prompt
Start by asking Amazon Q CLI to create a creative game:
```
Build a game Creative and Artistic Games use Pygame
```

### 2. Project Structure
```
canvas_dreams/
├── main.py
├── run.sh
└── README.md
```

### 3. Key Code Components

#### Particle System
```python
class Particle:
    def __init__(self, x, y, color, size=3, velocity=(0, 0), life=100):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.velocity = velocity
        self.life = life
        self.original_life = life
        self.gravity = 0.1 if mode == "gravity" else 0
    
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1] + self.gravity
        self.life -= 1
        self.size = max(1, self.size * (self.life / self.original_life))
```

#### Symmetrical Pattern Generation
```python
def create_symmetric_points(x, y, num_symmetry=8):
    points = []
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    dx, dy = x - center_x, y - center_y
    radius = math.sqrt(dx*dx + dy*dy)
    
    if radius < 5:  # Avoid drawing at the very center
        return points
        
    angle = math.atan2(dy, dx)
    
    for i in range(num_symmetry):
        new_angle = angle + (2 * Math.PI * i / num_symmetry)
        new_x = center_x + radius * math.cos(new_angle)
        new_y = center_y + radius * math.sin(new_angle)
        points.append((new_x, new_y))
    
    return points
```

## Creating the Web Version

### 1. Web Conversion Prompt
```
Có thể viết dạng localhost:1313 không?
```

### 2. Web Project Structure
```
canvas_dreams_web/
├── server.py
├── requirements.txt
├── run.sh
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── canvas_dreams.js
```

### 3. Key Web Components

#### Flask Server
```python
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=1313, debug=True)
```

#### HTML5 Canvas Implementation
```javascript
const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');

function draw(x, y) {
    if (mode === 'draw') {
        ctx.beginPath();
        ctx.arc(x, y, brushSize, 0, Math.PI * 2);
        ctx.fillStyle = currentColor;
        ctx.fill();
    }
    // ... other drawing modes
}
```

## Game Features and Implementation

### 1. Drawing Modes
- **Standard Drawing**: Basic brush strokes
- **Spray Paint**: Particle-based spray effect
- **Kaleidoscope**: Symmetrical pattern generation
- **Gravity**: Physics-based particle effects

### 2. User Interface
- Sidebar with controls
- Color palette
- Brush size adjustment
- Symmetry controls
- Help overlay

### 3. Controls
```
Mouse Controls:
- Left Button: Draw
- Right Button: Random Color

Keyboard Shortcuts:
- 1-4: Switch Modes
- Up/Down: Brush Size
- Left/Right: Symmetry Level
- C: Clear Canvas
- S: Save Artwork
- B: Toggle Background
- H: Help
```

## Troubleshooting Common Issues

### 1. Pygame Audio Issues
Solution: Disable audio initialization
```python
os.environ['SDL_AUDIODRIVER'] = 'dummy'
pygame.display.init()
pygame.font.init()
```

### 2. Flask Version Compatibility
Solution: Use specific versions
```
flask==2.0.1
werkzeug==2.0.1
```

## Future Development

### Planned Features
1. Animation recording
2. Layer system
3. Collaborative drawing
4. Mobile optimization
5. Custom brush shapes
6. Cloud save integration

## Conclusion

Building Canvas Dreams with Amazon Q CLI demonstrated the power of AI-assisted development in creating creative applications. The combination of Pygame for the desktop version and Flask/HTML5 Canvas for the web version provides a versatile platform for digital art creation.

## Resources

- [GitHub Repository](https://github.com/vanhoangkha/Build-Games-with-Amazon-Q-CLI)
- [Amazon Q CLI Documentation](https://aws.amazon.com/q/cli/)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## Share Your Experience

If you build something with Amazon Q CLI, share your experience using the hashtag #AmazonQCLI. Your insights could help others in their creative coding journey!

---

*This blog post was created with the assistance of Amazon Q CLI.*

#AmazonQCLI #GameDev #CreativeCoding #Python #WebDevelopment
