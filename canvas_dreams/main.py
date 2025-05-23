import pygame
import sys
import random
import math
from pygame import gfxdraw
import os

# Disable audio to prevent ALSA errors
os.environ['SDL_AUDIODRIVER'] = 'dummy'

# Initialize Pygame with specific subsystems, excluding audio
pygame.display.init()
pygame.font.init()
pygame.key.init()
pygame.mouse.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
TITLE = "Canvas Dreams - Interactive Art Creation"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 105, 97),  # Coral
    (255, 180, 128),  # Peach
    (248, 243, 141),  # Pale Yellow
    (66, 214, 164),  # Mint
    (8, 126, 139),   # Teal
    (89, 69, 164),   # Purple
    (233, 78, 119),  # Pink
    (255, 145, 77)   # Orange
]

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Game state
current_color = random.choice(COLORS)
brush_size = 15
particles = []
mode = "draw"  # Modes: "draw", "spray", "kaleidoscope", "gravity"
symmetry = 8   # For kaleidoscope mode
background_color = BLACK

# Font setup
font = pygame.font.SysFont('Arial', 20)

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
        
    def draw(self):
        alpha = int(255 * (self.life / self.original_life))
        color_with_alpha = (*self.color[:3], alpha)
        gfxdraw.filled_circle(screen, int(self.x), int(self.y), int(self.size), color_with_alpha)

def draw_ui():
    # Draw mode indicator
    mode_text = font.render(f"Mode: {mode.capitalize()}", True, WHITE)
    screen.blit(mode_text, (10, 10))
    
    # Draw brush size indicator
    size_text = font.render(f"Brush Size: {brush_size}", True, WHITE)
    screen.blit(size_text, (10, 40))
    
    # Draw color palette
    for i, color in enumerate(COLORS):
        rect = pygame.Rect(10 + i * 30, HEIGHT - 40, 25, 25)
        pygame.draw.rect(screen, color, rect)
        if color == current_color:
            pygame.draw.rect(screen, WHITE, rect, 2)

def create_symmetric_points(x, y, num_symmetry=8):
    points = []
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    dx, dy = x - center_x, y - center_y
    radius = math.sqrt(dx*dx + dy*dy)
    
    if radius < 5:  # Avoid drawing at the very center
        return points
        
    angle = math.atan2(dy, dx)
    
    for i in range(num_symmetry):
        new_angle = angle + (2 * math.pi * i / num_symmetry)
        new_x = center_x + radius * math.cos(new_angle)
        new_y = center_y + radius * math.sin(new_angle)
        points.append((new_x, new_y))
    
    return points

def create_particles(x, y, count=10):
    for _ in range(count):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(0.5, 2)
        velocity = (math.cos(angle) * speed, math.sin(angle) * speed)
        size = random.uniform(brush_size * 0.2, brush_size * 0.5)
        life = random.randint(30, 100)
        
        # Create a slightly varied color
        color_variation = 20
        base_color = current_color
        varied_color = (
            max(0, min(255, base_color[0] + random.randint(-color_variation, color_variation))),
            max(0, min(255, base_color[1] + random.randint(-color_variation, color_variation))),
            max(0, min(255, base_color[2] + random.randint(-color_variation, color_variation))),
        )
        
        particles.append(Particle(x, y, varied_color, size, velocity, life))

def handle_drawing(pos):
    x, y = pos
    
    if mode == "draw":
        pygame.draw.circle(screen, current_color, (x, y), brush_size)
    
    elif mode == "spray":
        create_particles(x, y, count=5)
    
    elif mode == "kaleidoscope":
        points = create_symmetric_points(x, y, symmetry)
        for point_x, point_y in points:
            pygame.draw.circle(screen, current_color, (int(point_x), int(point_y)), brush_size)
            create_particles(point_x, point_y, count=2)
    
    elif mode == "gravity":
        for _ in range(3):
            angle = random.uniform(-math.pi/4, math.pi/4)  # Upward spray
            speed = random.uniform(1, 5)
            velocity = (math.cos(angle) * speed, -math.sin(angle) * speed * 2)
            size = random.uniform(brush_size * 0.3, brush_size * 0.7)
            life = random.randint(50, 150)
            
            varied_color = (
                max(0, min(255, current_color[0] + random.randint(-20, 20))),
                max(0, min(255, current_color[1] + random.randint(-20, 20))),
                max(0, min(255, current_color[2] + random.randint(-20, 20))),
            )
            
            particles.append(Particle(x, y, varied_color, size, velocity, life))

def save_artwork():
    timestamp = pygame.time.get_ticks()
    filename = f"canvas_dreams_{timestamp}.png"
    pygame.image.save(screen, filename)
    print(f"Artwork saved as {filename}")

def main():
    global current_color, brush_size, mode, symmetry, background_color
    
    # Fill the screen with the background color
    screen.fill(background_color)
    
    running = True
    drawing = False
    
    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    # Clear screen
                    screen.fill(background_color)
                    particles.clear()
                elif event.key == pygame.K_s:
                    # Save artwork
                    save_artwork()
                elif event.key == pygame.K_1:
                    mode = "draw"
                elif event.key == pygame.K_2:
                    mode = "spray"
                elif event.key == pygame.K_3:
                    mode = "kaleidoscope"
                elif event.key == pygame.K_4:
                    mode = "gravity"
                elif event.key == pygame.K_UP:
                    brush_size = min(50, brush_size + 1)
                elif event.key == pygame.K_DOWN:
                    brush_size = max(1, brush_size - 1)
                elif event.key == pygame.K_RIGHT:
                    symmetry = min(16, symmetry + 1)
                elif event.key == pygame.K_LEFT:
                    symmetry = max(2, symmetry - 1)
                elif event.key == pygame.K_b:
                    # Toggle background color
                    background_color = WHITE if background_color == BLACK else BLACK
                    screen.fill(background_color)
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    drawing = True
                    handle_drawing(event.pos)
                elif event.button == 3:  # Right mouse button
                    # Pick a random color
                    current_color = random.choice(COLORS)
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    handle_drawing(event.pos)
        
        # Update particles
        for particle in particles[:]:
            particle.update()
            if particle.life <= 0:
                particles.remove(particle)
            else:
                particle.draw()
        
        # Draw UI elements
        draw_ui()
        
        # Update the display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
