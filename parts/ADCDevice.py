import smbus


class ADCDevice(object):
    def __init__(self):
        self.address = 0x4b
        self.bus = smbus.SMBus(1)

    def detect_i2_c(self, addr):
        try:

            self.bus.write_byte(addr, 0)
            print("Found device in address 0x%x" % addr)
            return True

        except:
            print("Not found device in address 0x%x" % addr)
            return False

    def close(self):
        self.bus.close()


class ADS7830(ADCDevice):
    def __init__(self):
        super(ADS7830, self).__init__()
        self.address = 0x4b

    def analog_read(self, chn):
        return self.bus.read_byte_data(self.address, 0x84 | (((chn << 2 | chn >> 1) & 0x07) << 4))

    def get_y(self):
        return self.bus.read_byte_data(self.address, 0x84)

    def get_x(self):
        return self.bus.read_byte_data(self.address, 0xc4)
