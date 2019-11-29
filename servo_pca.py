import sys
import pigpio
from pca9685 import pca9685

PCA9685_ADDR = 0x40
pwm_freq = 50

pi = pigpio.pi()

servo_drv = pca9685( pi, PCA9685_ADDR )
servo_drv.set_freq( pwm_freq )

args = sys.argv

f = 0
if ( len( args ) > 2 ):
	if ( args[2].isdecimal() ):
		p_width = int( args[2] )
		ch = int( args[1] )
		if ( p_width >= 500 and p_width <= 2500 ):
			if ( ch >= 0 and ch < 0x10 ):
				f = 1

if ( f == 1 ):
	print ("Servo set", p_width , "to CH" , ch )

	servo_drv.set_pulse_t( ch, p_width )

else:
	print ("USAGE: python3 servo_pca.py CHANNEL PULSE_WIDTH")
	print ("  PULSE_WHDHT : Pulse range is 500-2500.")

