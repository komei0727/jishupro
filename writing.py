#!/usr/bin/python
import time
from PCA9685 import PCA9685
from module.inverse_kinematics import inverse_kinematics

def _down():
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)
  for i in range(60, 39, -1):
    pulse = pwm.ConvertPulse(i)
    pwm.setServoPulse(2, pulse)
    time.sleep(0.02)

def _up():
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)
  for i in range(40, 60, 1):
    pulse = pwm.ConvertPulse(i)
    pwm.setServoPulse(2, pulse)
    time.sleep(0.02)

def あ(dx, dy):
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

  angles1 = inverse_kinematics('data/あ_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/あ_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/あ_3.csv', dx, dy)
  _up()
  for i in range(len(angles1)):
      pulse1 = pwm.ConvertPulse(float(angles1[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles1[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)
      if i==0:
          _down()

  _up()
  for i in range(len(angles2)):
      pulse1 = pwm.ConvertPulse(float(angles2[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles2[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)
      if i==0:
          _down()

  _up()
  for i in range(len(angles3)):
      pulse1 = pwm.ConvertPulse(float(angles3[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles3[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)
      if i==0:
          _down()

def い(dx, dy):
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

  angles1 = inverse_kinematics('data/い_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/い_2.csv', dx, dy)
  for i in range(len(angles1)):
      pulse1 = pwm.ConvertPulse(float(angles1[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles1[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

  for i in range(len(angles2)):
      pulse1 = pwm.ConvertPulse(float(angles2[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles2[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

def う(dx, dy):
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

  angles1 = inverse_kinematics('data/う_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/う_2.csv', dx, dy)
  for i in range(len(angles1)):
      pulse1 = pwm.ConvertPulse(float(angles1[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles1[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

  for i in range(len(angles2)):
      pulse1 = pwm.ConvertPulse(float(angles2[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles2[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

def え(dx, dy):
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

  angles1 = inverse_kinematics('data/え_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/え_2.csv', dx, dy)
  for i in range(len(angles1)):
      pulse1 = pwm.ConvertPulse(float(angles1[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles1[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

  for i in range(len(angles2)):
      pulse1 = pwm.ConvertPulse(float(angles2[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles2[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

def お(dx, dy):
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

  angles1 = inverse_kinematics('data/お_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/お_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/お_3.csv', dx, dy)
  for i in range(len(angles1)):
      pulse1 = pwm.ConvertPulse(float(angles1[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles1[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

  for i in range(len(angles2)):
      pulse1 = pwm.ConvertPulse(float(angles2[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles2[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)

  for i in range(len(angles3)):
      pulse1 = pwm.ConvertPulse(float(angles3[i][0]))
      pulse2 = pwm.ConvertPulse(float(angles3[i][1]))
      pwm.setServoPulse(0, pulse1)
      pwm.setServoPulse(1, pulse2)
      time.sleep(0.001)
