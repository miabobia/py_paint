'''
class for handling ui boxes
'''
from pygame import Surface, PixelArray, draw, SRCALPHA
from layer import Layer
from typing import List
from config import config

class ColorPicker:
    z_level: int # 0 is at the very front
    surface: Surface

    def __init__(self, size: tuple[int, int]) -> None:
        self.size = size
        self.surface = self.create_image()
    
    def create_image(self) -> Surface:
        width, height = self.size
        print(width, height)
        surface = Surface(self.size)
        with PixelArray(surface) as px_arr:
            for col in range(width):
                # Calculate the grayscale value based on the column index
                gray_value = int((col / (width - 1)) * 255)  # Normalize to [0, 255]
                rgb_value = (gray_value, gray_value, gray_value)  # Create RGB tuple
                
                for row in range(height):
                    px_arr[col, row] = rgb_value
        return surface

    def get_color(self, mouse_x: int) -> tuple[int, int, int]:
        width, _ = self.size
        color_val = int((mouse_x/ (width - 1)) * 255)
        return (color_val, color_val, color_val)
    
'''
lets start out with a set amount of layers
'''
class LayerHandler:
    layers: List[Layer]
    surface: Surface
    width: int
    height: int

    def __init__(self, layers: List[Layer]) -> None:
        self.layers = layers
        self.width = config.get('window').get('width') - config.get('layer').get('width')
        self.height = config.get('layer').get('height')
        self.surface = Surface((self.width, self.height), SRCALPHA)

        # set base color
        with PixelArray(self.surface) as px_arr:
            px_arr[:, :] = (20, 200, 10, 0)

    def update_layer_widgets(self):
        for layer in self.layers:
            self.show_layer_widget(layer)

    def show_layer_widget(self, layer: Layer):
        w = self.width
        h = self.height//len(self.layers)
        y = h * layer.z_level
        # l_rect = [x, y, w ,h]
        l_rect = [0, y, w, h]
        

        draw.rect(self.surface, (255, 0, 0, 255), l_rect)
        pass

    def update_layer_data(self):
        pass
