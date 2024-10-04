'''
class for handling ui boxes
'''
from pygame import Surface, PixelArray

class UI:
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