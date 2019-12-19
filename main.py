#!/usr/bin/python

import time
import csv
from PCA9685 import PCA9685
from module.inverse_kinematics import inverse_kinematics

if __name__=='__main__':

  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

  #with open('angle_data/a_1.csv') as f:
  #    reader = csv.reader(f)
  #    angles = [row for row in reader]
  angles = inverse_kinematics('data/あ_1.csv', 55, 45)
  for i in range(len(angles)):
      pulse1 = pwm.ConvertPulse(float(angles[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

  #with open('angle_data/a_2.csv') as f:
  #    reader = csv.reader(f)
  #    angles = [row for row in reader]

  angles = inverse_kinematics('data/あ_2.csv', 55, 45)
  for i in range(len(angles)):
      pulse1 = pwm.ConvertPulse(float(angles[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

  #with open('angle_data/a_3.csv') as f:
  #    reader = csv.reader(f)
  #    angles = [row for row in reader]

  angles = inverse_kinematics('data/あ_3.csv', 55, 45)
  for i in range(len(angles)):
      pulse1 = pwm.ConvertPulse(float(angles[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

