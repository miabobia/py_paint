import pygame
from pygame import Surface, SRCALPHA

class Buffer:
    def __init__(self, width: int, height: int):
        self.surface = Surface((width, height), SRCALPHA)
        self.clear()  # Fill the buffer with transparent pixels

    def clear(self):
        self.surface.fill((0, 0, 0, 0))  # Fully transparent

    def set_pixel(self, x: int, y: int, color: tuple[int, int, int, int]):
        if 0 <= x < self.surface.get_width() and 0 <= y < self.surface.get_height():
            self.surface.set_at((x, y), color)  # Set the pixel color

    def get_painted_pixels(self) -> tuple[int, int, int]:
        pixels = []
        w, h = self.surface.get_size()
        print(w, h)
        for y in range(h):
            for x in range(w):
                # only need one color value since all colors are grayscaled
                r, _, _, a = tuple(self.get_surface().get_at((x, y)))
                if a == 0: continue
                pixels.append((x, y, r))

        return pixels

    def get_surface(self) -> Surface:
        return self.surface
