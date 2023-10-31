from xbox360controller import Xbox360Controller


class Manette:
    def __init__(self, port):
        self.port = port
        self.controler = Xbox360Controller(self.port, axis_threshold=0.2)
        self.lx_pos = 0
        self.ly_pos = 0
        self.trig_lt_pos = 0
        self.trig_rt_pos = 0
        self.trig_l_press = False
        self.trig_r_press = False

    def on_axis_l_moved(self, axis):
        self.lx_pos = axis.x
        self.ly_pos = axis.y

    def on_trigger_lt_moved(self, axis):
        self.trig_lt_pos = axis.value

    def on_trigger_rt_moved(self, axis):
        self.trig_rt_pos = axis.value

    def on_trigger_l_pressed(self):
        self.trig_l_press = True

    def on_trigger_l_released(self):
        self.trig_l_press = False

    def on_trigger_r_pressed(self):
        self.trig_r_press = True

    def on_trigger_r_released(self):
        self.trig_r_press = False