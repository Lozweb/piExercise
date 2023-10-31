import signal
from xbox360controller import Xbox360Controller


class Manette:
    def __init__(self, port):
        self.port = port
        self.controler = Xbox360Controller(self.port, axis_threshold=0.2)
        self.current_lx_pos = 0
        self.current_ly_pos = 0

    def on_axis_l_moved(self, axis):
        self.current_lx_pos = axis.x
        self.current_ly_pos = axis.y
