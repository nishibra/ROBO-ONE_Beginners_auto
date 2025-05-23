import struct, utime
#import constants as const
DIST_LOW =                  0x00   # cm
DIST_HIGH =                 0x01
AMP_LOW =                   0x02
AMP_HIGH =                  0x03
TEMP_LOW =                  0x04   # Unit: 0.01 Celsius
TEMP_HIGH =                 0x05
TICK_LOW =                  0x06   # Timestamp
TICK_HIGH =                 0x07
ERROR_LOW =                 0x08
ERROR_HIGH =                0x09
VERSION_REVISION =          0x0A
VERSION_MINOR =             0x0B
VERSION_MAJOR =             0x0C
SN =                        0x10    # Production code in 14 bytes ASCI code (0x10 is the first byte)
SAVE =                      0x20    # Write 0x01 to save current setting
SHUTDOWN_REBOOT =           0x21    # Write 0x02 to reboot
SLAVE_ADDR =                0x22    # Default: 0x10, Range: [0x08, 0x77]
MODE =                      0x23    # Default: 0x00 | Continuous ranging mode: 0x00  Trigger mode: 0x01
TRIG_ONE_SHOT =             0x24    # 0x01: Trigger once (only on trigger mode)
ENABLE =                    0x25    # Turn on LiDAR: 0x00, Turn off LiDAR: 0x01
FPS_LOW =                   0x26    # Default: 0x64 100Hz, 0xFA 250Hz
FPS_HIGH =                  0x27
LOW_POWER =                 0x28    # Default: 0x00, Normal: 0x00, Power saving mode: 0x01
RESTORE_FACTORY_DEFAULTS =  0x29    # Write 0x01 to restore factory default settings
AMP_THR_LOW =               0x2A    # Default: 0x64, Amp threshold value
MIN_DIST_LOW =              0x2E    # Default: 0x00, Minimum dist in cm, but not working on DUMMY_DIST
MIN_DIST_HIGH =             0x2F    # Default: 0x00
MAX_DIST_LOW =              0x30    # Default: 0x20, Maximum dist in cm, but not working on DUMMY_DIST
MAX_DIST_HIGH =             0x31    # Default: 0x03

class LIDAR:
    '''docstring for LIDAR.'''

    def __init__(self, i2c, addr):
        self.i2c = i2c
        self.addr = addr

    def addr(self):
        return self.addr

    def _read(self, addr, bytes):
        return self.i2c.readfrom_mem(self.addr, addr, bytes)

    def _write(self, addr, value):
        self.i2c.writeto_mem(self.addr, addr,bytearray([ value]))

    def save(self):
        self._write(SAVE, 0x01)
        utime.sleep_ms(100)

    def reboot(self):
        utime.sleep_ms(50)
        self.save()
        self._write(SHUTDOWN_REBOOT, 0x02)

    def _save_reboot(self):
        self.reboot()
        utime.sleep_ms(500)

    def distance(self):
        dist = self._read(DIST_LOW, 2)
        return struct.unpack('<H', dist)[0]

    def signal_amp(self):
        amp = self._read(AMP_LOW, 2)
        return int(struct.unpack('<H', amp)[0])

    def temp(self):
        temp = self._read(TEMP_LOW, 2)
        return int(struct.unpack('<H', temp)[0]) * 0.01

    def version(self):
        v = self._read(VERSION_REVISION, 3)
        return 'LiDAR Version {}.{}.{}'.format(v[2], v[1], v[0])

    def set_frequency(self, freq=0x64):
        self._write(FPS_LOW, freq)
        self._save_reboot()

    def power_saving_mode(self, power_saving_mode=True):
        val = 0x01 if power_saving_mode else 0x00
        self._write(LOW_POWER, val)

    def on_off(self, on=True):
        val = 0x00 if on else 0x01
        self._write(ENABLE, val)

    def reset(self):
        self._write(RESTORE_FACTORY_DEFAULTS, 0x01)
        self._save_reboot()

    def set_min_max(self, min, max):
        min *= 10
        max *= 10

        high, low  = min >> 8, min & 0XFF
        self._write(MIN_DIST_HIGH, high)
        self._write(MIN_DIST_LOW, low)

        high, low  = max >> 8, max & 0XFF
        self._write(MAX_DIST_HIGH, high)
        self._write(MAX_DIST_LOW, low)
        self._save_reboot()

    def read_all(self):
        return 'Distance {}, ChipTemp {}, SignalAmp {}'.format(
        self.distance(),
        self.temp(),
        self.signal_amp())
