'''
StateBuffer contains multiple CanvasStates
CanvasState contains multiple LayerStates
'''

from typing import List
from dataclasses import dataclass

@dataclass
class LayerState:
    pixels: List[List[int]]
    z_level: int

@dataclass
class CanvasState:
    layers: List[LayerState]

class StateBuffer:
    canvas_states: List[CanvasState]

    def add_canvas_state(self):
        pass

    def remove_canvas_state(self):
        pass
