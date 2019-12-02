#!/usr/bin/python

import time
import csv
from PCA9685 import PCA9685

if __name__=='__main__':

  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

  with open('data/sample.csv') as f:
      reader = csv.reader(f)
      angles = [row for row in reader]

  for i in range(len(angles)):
      pulse1 = pwm.ConvertPulse(int(angles[i][0]))
      pulse2 = pwm.ConvertPulse(int(angles[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.02)
