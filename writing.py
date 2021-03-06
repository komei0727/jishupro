#!/usr/bin/python
import time
from PCA9685 import PCA9685
from module.inverse_kinematics import inverse_kinematics

def _down():
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)
  for i in range(60, 38, -1):
    pulse = pwm.ConvertPulse(i)
    pwm.setServoPulse(2, pulse)
    time.sleep(0.02)

def _up():
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)
  for i in range(38, 60, 1):
    pulse = pwm.ConvertPulse(i)
    pwm.setServoPulse(2, pulse)
    time.sleep(0.02)

def _writing(angles):
    pwm = PCA9685(0x40, debug=False)
    pwm.setPWMFreq(60)
    for i in range(len(angles)):
        _up()
        for j in range(len(angles[i])):
            pulse1 = pwm.ConvertPulse(float(angles[i][j][0]))
            pulse2 = pwm.ConvertPulse(float(angles[i][j][1]))
            pwm.setServoPulse(0, pulse1)
            pwm.setServoPulse(1, pulse2)
            time.sleep(0.001)
            if j==0:
                _down()



def あ(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/あ_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/あ_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/あ_3.csv', dx, dy)
  angles = [angles1, angles2, angles3]
  _writing(angles)
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

def い(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/い_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/い_2.csv', dx, dy)
  angles = [angles1, angles2]
  _writing(angles)
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

def う(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/う_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/う_2.csv', dx, dy)
  angles = [angles1, angles2]
  _writing(angles)
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

def え(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/え_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/え_2.csv', dx, dy)
  angles = [angles1, angles2]
  _writing(angles)
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

def お(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/お_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/お_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/お_3.csv', dx, dy)
  angles = [angles1, angles2, angles3]
  _writing(angles)
  pwm = PCA9685(0x40, debug=False)
  pwm.setPWMFreq(60)

def か(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/か_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/か_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/か_3.csv', dx, dy)
  angles = [angles1, angles2, angles3]
  _writing(angles)

def き(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/き_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/き_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/き_3.csv', dx, dy)
  angles = [angles1, angles2, angles3]
  _writing(angles)

def く(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/く_1.csv', dx, dy)
  angles = [angles1]
  _writing(angles)

def け(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/け_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/け_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/け_3.csv', dx, dy)
  angles = [angles1, angles2, angles3]
  _writing(angles)

def こ(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/こ_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/こ_2.csv', dx, dy)
  angles = [angles1, angles2]
  _writing(angles)

def さ(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/さ_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/さ_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/さ_3.csv', dx, dy)
  angles = [angles1, angles2, angles3]
  _writing(angles)

def よ(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/よ_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/よ_2.csv', dx, dy)
  angles = [angles1, angles2]
  _writing(angles)

def な(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/な_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/な_2.csv', dx, dy)
  angles3 = inverse_kinematics('data/な_3.csv', dx, dy)
  angles4 = inverse_kinematics('data/な_4.csv', dx, dy)
  angles = [angles1, angles2, angles3, angles4]
  _writing(angles)

def ら(dx, dy):
  _up()
  angles1 = inverse_kinematics('data/ら_1.csv', dx, dy)
  angles2 = inverse_kinematics('data/ら_2.csv', dx, dy)
  angles = [angles1, angles2]
  _writing(angles)
