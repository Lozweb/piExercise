from xbox360controller import Xbox360Controller


class Manette:
    def __init__(self, port):
        self.port = port
        self.controler = Xbox360Controller(self.port, axis_threshold=0.2)
        self.l_dead_zone_min, self.l_dead_zone_max = (-0.5, 0.5)
        self.lx_pos = 0
        self.ly_pos = 0
        self.trig_lt_pos = 0
        self.trig_rt_pos = 0
        self.direction = "forward"

    def on_axis_l_moved(self, axis):
        if axis.x < 0:
            self.lx_pos = axis.x if axis.x < self.l_dead_zone_min else 0
        else:
            self.lx_pos = axis.x if axis.x > self.l_dead_zone_max else 0
        if axis.y < 0:
            self.ly_pos = axis.y if axis.y < self.l_dead_zone_min else 0
        else:
            self.ly_pos = axis.y if axis.y > self.l_dead_zone_max else 0

    def on_trigger_lt_moved(self, axis):
        self.trig_lt_pos = axis.value

    def on_trigger_rt_moved(self, axis):
        self.trig_rt_pos = axis.value

    def on_button_x_release(self, button):
        print(button.name)
        if self.direction == "forward":
            self.direction = "backward"
        else:
            self.direction = "forward"
