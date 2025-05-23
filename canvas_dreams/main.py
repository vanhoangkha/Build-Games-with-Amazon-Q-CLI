import pygame
import sys
import random
import math
from pygame import gfxdraw
import os

# Disable audio to prevent ALSA errors
os.environ['SDL_AUDIODRIVER'] = 'dummy'

# Initialize Pygame with specific subsystems
pygame.init()
pygame.display.init()
pygame.font.init()

# Constants
WIDTH, HEIGHT = 900, 700
FPS = 60
TITLE = "Canvas Dreams - Interactive Art Creation"
SIDEBAR_WIDTH = 200
CANVAS_WIDTH = WIDTH - SIDEBAR_WIDTH
CANVAS_HEIGHT = HEIGHT - 60
CANVAS_TOP = 0
CANVAS_LEFT = SIDEBAR_WIDTH
FOOTER_HEIGHT = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
COLORS = [
    (255, 105, 97),  # Coral
    (255, 180, 128),  # Peach
    (248, 243, 141),  # Pale Yellow
    (66, 214, 164),  # Mint
    (8, 126, 139),   # Teal
    (89, 69, 164),   # Purple
    (233, 78, 119),  # Pink
    (255, 145, 77),  # Orange
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
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
show_help = False
save_message = ""
save_message_time = 0

# Font setup
title_font = pygame.font.SysFont('Arial', 24, bold=True)
font = pygame.font.SysFont('Arial', 18)
small_font = pygame.font.SysFont('Arial', 14)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, action=None, icon=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.action = action
        self.icon = icon
        self.is_hovered = False
        
    def draw(self):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=5)
        pygame.draw.rect(screen, LIGHT_GRAY, self.rect, 2, border_radius=5)
        
        if self.text:
            text_surf = font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)
            
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.action:
                return self.action()
        return False

# Particle class
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
        if (CANVAS_LEFT <= self.x <= CANVAS_LEFT + CANVAS_WIDTH and 
            CANVAS_TOP <= self.y <= CANVAS_TOP + CANVAS_HEIGHT):
            alpha = int(255 * (self.life / self.original_life))
            color_with_alpha = (*self.color[:3], alpha)
            gfxdraw.filled_circle(screen, int(self.x), int(self.y), int(self.size), color_with_alpha)

# Create buttons
def create_buttons():
    buttons = []
    
    # Mode buttons
    mode_y = 80
    mode_height = 40
    mode_spacing = 10
    
    buttons.append(Button(20, mode_y, 160, mode_height, "Standard Drawing (1)", DARK_GRAY, GRAY, WHITE, lambda: set_mode("draw")))
    buttons.append(Button(20, mode_y + mode_height + mode_spacing, 160, mode_height, "Spray Paint (2)", DARK_GRAY, GRAY, WHITE, lambda: set_mode("spray")))
    buttons.append(Button(20, mode_y + (mode_height + mode_spacing) * 2, 160, mode_height, "Kaleidoscope (3)", DARK_GRAY, GRAY, WHITE, lambda: set_mode("kaleidoscope")))
    buttons.append(Button(20, mode_y + (mode_height + mode_spacing) * 3, 160, mode_height, "Gravity (4)", DARK_GRAY, GRAY, WHITE, lambda: set_mode("gravity")))
    
    # Tool buttons
    tool_y = 280
    tool_height = 40
    tool_spacing = 10
    
    buttons.append(Button(20, tool_y, 160, tool_height, "Clear Canvas (C)", DARK_GRAY, GRAY, WHITE, clear_canvas))
    buttons.append(Button(20, tool_y + tool_height + tool_spacing, 160, tool_height, "Save Artwork (S)", DARK_GRAY, GRAY, WHITE, save_artwork))
    buttons.append(Button(20, tool_y + (tool_height + tool_spacing) * 2, 160, tool_height, "Toggle Background (B)", DARK_GRAY, GRAY, WHITE, toggle_background))
    buttons.append(Button(20, tool_y + (tool_height + tool_spacing) * 3, 160, tool_height, "Help", DARK_GRAY, GRAY, WHITE, toggle_help))
    
    # Size adjustment buttons
    size_y = 450
    size_btn_width = 40
    size_btn_height = 40
    
    buttons.append(Button(20, size_y, size_btn_width, size_btn_height, "-", DARK_GRAY, GRAY, WHITE, decrease_brush_size))
    buttons.append(Button(140, size_y, size_btn_width, size_btn_height, "+", DARK_GRAY, GRAY, WHITE, increase_brush_size))
    
    # Symmetry adjustment buttons (for kaleidoscope)
    sym_y = 520
    sym_btn_width = 40
    sym_btn_height = 40
    
    buttons.append(Button(20, sym_y, sym_btn_width, sym_btn_height, "-", DARK_GRAY, GRAY, WHITE, decrease_symmetry))
    buttons.append(Button(140, sym_y, sym_btn_width, sym_btn_height, "+", DARK_GRAY, GRAY, WHITE, increase_symmetry))
    
    return buttons

# Button actions
def set_mode(new_mode):
    global mode
    mode = new_mode
    return True

def clear_canvas():
    global particles
    # Only clear the canvas area, not the UI
    pygame.draw.rect(screen, background_color, (CANVAS_LEFT, CANVAS_TOP, CANVAS_WIDTH, CANVAS_HEIGHT))
    particles.clear()
    return True

def save_artwork():
    global save_message, save_message_time
    # Create a new surface for just the canvas
    canvas_surface = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
    canvas_surface.blit(screen, (0, 0), (CANVAS_LEFT, CANVAS_TOP, CANVAS_WIDTH, CANVAS_HEIGHT))
    
    timestamp = pygame.time.get_ticks()
    filename = f"canvas_dreams_{timestamp}.png"
    pygame.image.save(canvas_surface, filename)
    
    save_message = f"Saved as {filename}"
    save_message_time = pygame.time.get_ticks()
    return True

def toggle_background():
    global background_color
    background_color = WHITE if background_color == BLACK else BLACK
    # Only clear the canvas area, not the UI
    pygame.draw.rect(screen, background_color, (CANVAS_LEFT, CANVAS_TOP, CANVAS_WIDTH, CANVAS_HEIGHT))
    return True

def toggle_help():
    global show_help
    show_help = not show_help
    return True

def increase_brush_size():
    global brush_size
    brush_size = min(50, brush_size + 1)
    return True

def decrease_brush_size():
    global brush_size
    brush_size = max(1, brush_size - 1)
    return True

def increase_symmetry():
    global symmetry
    symmetry = min(16, symmetry + 1)
    return True

def decrease_symmetry():
    global symmetry
    symmetry = max(2, symmetry - 1)
    return True

def draw_ui(buttons, mouse_pos):
    # Draw sidebar background
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, SIDEBAR_WIDTH, HEIGHT))
    
    # Draw footer background
    pygame.draw.rect(screen, DARK_GRAY, (0, HEIGHT - FOOTER_HEIGHT, WIDTH, FOOTER_HEIGHT))
    
    # Draw canvas border
    pygame.draw.rect(screen, LIGHT_GRAY, (CANVAS_LEFT-2, CANVAS_TOP-2, CANVAS_WIDTH+4, CANVAS_HEIGHT+4), 2)
    
    # Draw title
    title_text = title_font.render("Canvas Dreams", True, WHITE)
    screen.blit(title_text, (20, 20))
    subtitle_text = small_font.render("Interactive Art Creation", True, LIGHT_GRAY)
    screen.blit(subtitle_text, (20, 50))
    
    # Draw current mode
    mode_text = font.render(f"Current Mode:", True, WHITE)
    screen.blit(mode_text, (20, 400))
    active_mode_text = font.render(mode.capitalize(), True, LIGHT_GRAY)
    screen.blit(active_mode_text, (120, 400))
    
    # Draw brush size
    size_text = font.render(f"Brush Size: {brush_size}", True, WHITE)
    screen.blit(size_text, (70, 460))
    
    # Draw symmetry (only relevant for kaleidoscope)
    if mode == "kaleidoscope":
        sym_text = font.render(f"Symmetry: {symmetry}", True, WHITE)
    else:
        sym_text = font.render(f"Symmetry: {symmetry}", True, GRAY)
    screen.blit(sym_text, (70, 530))
    
    # Draw color palette in footer
    palette_text = font.render("Color Palette:", True, WHITE)
    screen.blit(palette_text, (20, HEIGHT - FOOTER_HEIGHT + 10))
    
    color_size = 30
    color_spacing = 5
    palette_y = HEIGHT - FOOTER_HEIGHT + 25
    
    for i, color in enumerate(COLORS):
        rect = pygame.Rect(20 + i * (color_size + color_spacing), palette_y, color_size, color_size)
        pygame.draw.rect(screen, color, rect, border_radius=3)
        if color == current_color:
            pygame.draw.rect(screen, WHITE, rect, 2, border_radius=3)
            
    # Draw save message if needed
    if save_message and pygame.time.get_ticks() - save_message_time < 3000:  # Show for 3 seconds
        save_text = font.render(save_message, True, WHITE)
        screen.blit(save_text, (CANVAS_LEFT + 10, HEIGHT - FOOTER_HEIGHT + 20))
    
    # Draw buttons
    for button in buttons:
        button.check_hover(mouse_pos)
        button.draw()
    
    # Draw help overlay if active
    if show_help:
        draw_help_overlay()

def draw_help_overlay():
    # Semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    screen.blit(overlay, (0, 0))
    
    # Help content
    help_title = title_font.render("Canvas Dreams - Help", True, WHITE)
    screen.blit(help_title, (WIDTH // 2 - help_title.get_width() // 2, 50))
    
    help_texts = [
        "Mouse Controls:",
        "- Left Mouse Button: Draw on canvas",
        "- Right Mouse Button: Change to random color",
        "",
        "Keyboard Controls:",
        "- 1-4 Keys: Switch between drawing modes",
        "- Up/Down Arrows: Increase/decrease brush size",
        "- Left/Right Arrows: Adjust symmetry (in kaleidoscope mode)",
        "- C Key: Clear canvas",
        "- S Key: Save artwork as PNG",
        "- B Key: Toggle background (black/white)",
        "- H Key: Show/hide this help",
        "",
        "Drawing Modes:",
        "- Standard: Classic brush drawing",
        "- Spray: Create particle spray effects",
        "- Kaleidoscope: Create symmetrical patterns",
        "- Gravity: Create fountain-like particle effects",
        "",
        "Click anywhere or press H to close this help"
    ]
    
    y_pos = 120
    for text in help_texts:
        if text == "":
            y_pos += 10
            continue
            
        help_text = font.render(text, True, WHITE)
        screen.blit(help_text, (WIDTH // 2 - 150, y_pos))
        y_pos += 25

def create_symmetric_points(x, y, num_symmetry=8):
    points = []
    center_x, center_y = CANVAS_LEFT + CANVAS_WIDTH // 2, CANVAS_TOP + CANVAS_HEIGHT // 2
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
    
    # Only draw if within canvas bounds
    if not (CANVAS_LEFT <= x <= CANVAS_LEFT + CANVAS_WIDTH and 
            CANVAS_TOP <= y <= CANVAS_TOP + CANVAS_HEIGHT):
        return
    
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

def handle_color_selection(pos):
    # Check if click is in the color palette area
    palette_y = HEIGHT - FOOTER_HEIGHT + 25
    color_size = 30
    color_spacing = 5
    
    for i, color in enumerate(COLORS):
        rect = pygame.Rect(20 + i * (color_size + color_spacing), palette_y, color_size, color_size)
        if rect.collidepoint(pos):
            return color
    
    return None

def main():
    global current_color, brush_size, mode, symmetry, background_color, show_help
    
    # Create buttons
    buttons = create_buttons()
    
    # Fill the screen with the background color
    screen.fill(DARK_GRAY)
    pygame.draw.rect(screen, background_color, (CANVAS_LEFT, CANVAS_TOP, CANVAS_WIDTH, CANVAS_HEIGHT))
    
    running = True
    drawing = False
    
    # Main game loop
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    clear_canvas()
                elif event.key == pygame.K_s:
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
                    increase_brush_size()
                elif event.key == pygame.K_DOWN:
                    decrease_brush_size()
                elif event.key == pygame.K_RIGHT:
                    increase_symmetry()
                elif event.key == pygame.K_LEFT:
                    decrease_symmetry()
                elif event.key == pygame.K_b:
                    toggle_background()
                elif event.key == pygame.K_h:
                    toggle_help()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_help:
                    show_help = False
                    continue
                    
                if event.button == 1:  # Left mouse button
                    # Check if any button was clicked
                    button_clicked = False
                    for button in buttons:
                        if button.handle_event(event):
                            button_clicked = True
                            break
                    
                    # Check if color palette was clicked
                    color_selected = handle_color_selection(event.pos)
                    if color_selected:
                        current_color = color_selected
                        button_clicked = True
                    
                    # If not clicking UI, start drawing
                    if not button_clicked:
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
        draw_ui(buttons, mouse_pos)
        
        # Update the display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
