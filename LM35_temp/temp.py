import time
import smbus

Address = 0x48
A0 = 0x40

bus = smbus.SMBus(1)

while True:
  bus.write_byte(Address, A0)
  value = bus.read_byte(Address)
  value = (500*value)/256
  print(value)
  time.sleep(0.2)

