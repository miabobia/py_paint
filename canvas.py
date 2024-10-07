import pygame
import sys
import yaml
from layer import Layer
from ui import UI
from buffer import Buffer
import numpy as np

# Load the configuration from YAML file
with open("config.yaml", 'r') as file:
    config = yaml.safe_load(file)

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# set up config values

# window config
WINDOW_WIDTH = config['window']['width']
WINDOW_HEIGHT = config['window']['height']
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(config['window']['title'])

# Colors from the config file
BACKGROUND_COLOR = config['colors']['background']
CIRCLE_COLOR = config['colors']['circle']
CIRCLE_RADIUS = config['circle']['radius']

# getting layer values from config
LAYER_WIDTH = config['layer']['width']
LAYER_HEIGHT = config['layer']['height']

# layer variables
current_layer = 0

# setup layer(s)
layers = [
    Layer(
    pygame.Surface((LAYER_WIDTH, LAYER_HEIGHT)),
    z_level=0,
    base_color=200
    )
]
# setup ui elements
color_picker = UI((WINDOW_WIDTH, WINDOW_HEIGHT - LAYER_HEIGHT))

# canvas variables
brush_size = config['brush']['radius']
brush_color = config['colors']['brush_default']

# init buffer
buffer = Buffer(LAYER_WIDTH, LAYER_HEIGHT)
buffer_has_data = False

# mouse state variables
current_mouse: tuple[int, int] = ()
old_mouse: tuple[int, int]

# pixel copy
pixel_copy_arr = np.zeros([LAYER_WIDTH, LAYER_HEIGHT], np.uint32)


# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse state
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_x, mouse_y = mouse_pos = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # draw layers
    for layer in layers:
        screen.blit(layer.surface, (0, 0))

    # draw buffer
    screen.blit(buffer.get_surface(), (0, 0))

    # draw ui
    screen.blit(color_picker.surface, (0, LAYER_HEIGHT))

    # mouse
    if mouse_buttons[0]:
        # left click
        if current_mouse:
            old_mouse = current_mouse
        else:
            old_mouse = mouse_pos

        current_mouse = mouse_pos

        # interact with ui
        if mouse_y > LAYER_HEIGHT and mouse_x >= 0: # change color
            brush_color = color_picker.get_color(mouse_x)
        else:
            buffer_has_data = True
            pygame.draw.line(
                surface=buffer.get_surface(),
                color=brush_color,
                start_pos=old_mouse,
                end_pos=current_mouse,
                width=brush_size
            )
    elif mouse_buttons[2]:
        print(pixel_copy_arr)
        # right click
        pygame.pixelcopy.surface_to_array(
            array=pixel_copy_arr,
            surface=layers[current_layer].surface,
        )

        print(pixel_copy_arr)

    else:
        # no mouse pressed
        current_mouse = ()
        pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)

        # push buffer contents to current layer
        if buffer_has_data:
            layers[current_layer].set_pixels(buffer.get_painted_pixels())
            buffer.clear()
            buffer_has_data = False
    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
