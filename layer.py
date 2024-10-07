'''
layer class
'''

from typing import List
import pygame
import numpy as np

# Add this function above your main loop
def save_layer_as_array(layer, filename):
    pixel_array = pygame.surfarray.array3d(layer.surface)
    pixel_array = np.transpose(pixel_array, (1, 0, 2))
    np.save(filename, pixel_array)

class Layer:
    z_level: int # 0 is at the very front
    surface: Surface

    def __init__(self, surface: Surface, z_level: int, base_color: int = 255) -> None:
        self.surface = surface
        self.z_level = z_level
        self.base_color = base_color

        # set base color
        with PixelArray(self.surface) as px_arr:
            px_arr[:, :] = (base_color, base_color, base_color)

    def set_pixels(self, pixels: List[tuple]):
        # pixels [(x, y, color), ...]
        with PixelArray(self.surface) as px_arr:
            print(len(pixels))
            for x, y, color in pixels:
                self.set_px(x, y, color, px_arr)

    def set_px(self, x: int, y: int, color: int, px_arr: PixelArray):
        if not self.bounds_check(x, y):
            return
        px_arr[x, y] = (color, color, color, 255)

    def bounds_check(self, x: int, y: int) -> bool:
        w, h = self.surface.get_size()
        return not (x >= w or x < 0 or y >= h or y < 0)


    
