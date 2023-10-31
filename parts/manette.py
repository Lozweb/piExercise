from xbox360controller import Xbox360Controller


class Manette:
    def __init__(self, port):
        self.port = port
        self.controler = Xbox360Controller(self.port, axis_threshold=0.2)
        self.lx_pos = 0
        self.ly_pos = 0
        self.trig_lt_pos = 0
        self.trig_rt_pos = 0
        self.direction = "forward"

    def on_axis_l_moved(self, axis):
        self.lx_pos = axis.x
        self.ly_pos = axis.y

    def on_trigger_lt_moved(self, axis):
        self.trig_lt_pos = axis.value

    def on_trigger_rt_moved(self, axis):
        self.trig_rt_pos = axis.value

    def on_button_trigger_r_released(self):
        if self.direction == "forward":
            self.direction = "backward"
        else:
            self.direction = "forward"
