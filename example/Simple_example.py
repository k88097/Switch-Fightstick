from NXController import Controller
import time

ctr = Controller()
## Or use your serial port if you have many
# ctr = Controller('/dev/tty.usbserial-AO0099VT'); 

#連續按 10次 A鍵

for i in range (10):
	ctr.A()
ctr.close()