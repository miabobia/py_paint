'''
layer class
'''

from typing import List
from pygame import Surface, PixelArray, surfarray
import numpy as np
import uuid

# Add this function above your main loop
def save_layer_as_array(layer, filename):
    pixel_array = surfarray.array3d(layer.surface)
    pixel_array = np.transpose(pixel_array, (1, 0, 2))
    np.save(filename, pixel_array)

class Layer:
    z_level: int # 0 is at the very front
    surface: Surface
    opacity: int
    id: str

    def __init__(self, surface: Surface, z_level: int, base_color: int = -1, id: str = '', opacity: int = 255) -> None:
        self.surface = surface
        self.z_level = z_level
        self.base_color = base_color
        self.opacity = opacity
        if not id: self.id = uuid.uuid4()

        # set base color
        with PixelArray(self.surface) as px_arr:
            px_arr[:, :] = (base_color, base_color, base_color)

    def set_pixels(self, pixels: List[tuple]):
        # pixels [(x, y, color), ...]
        with PixelArray(self.surface) as px_arr:
            for x, y, color, alpha in pixels:
                self.set_px(x, y, color, alpha, px_arr)

    def set_px(self, x: int, y: int, color: int, alpha: int, px_arr: PixelArray):
        if not self.bounds_check(x, y):
            return
        px_arr[x, y] = (color, color, color, alpha)

    def bounds_check(self, x: int, y: int) -> bool:
        w, h = self.surface.get_size()
        return not (x >= w or x < 0 or y >= h or y < 0)


    
