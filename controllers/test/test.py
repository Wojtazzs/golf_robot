"""test controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
from math import pi, sin
from enum import Enum

TIME_STEP = 64
robot = Robot()
kij_motor = robot.getDevice("kij_motor")
#kij_motor.setAcceleration(10)
kij_motor.setTorque(3000)
kij_motor.setPosition(float('inf'))
kij_motor.setVelocity(0.0)

class Angle():
    val = 0
    def set_val(self, val):
        self.val = val*pi
        return self.val
    

F = 2.0   # frequency 2 Hz
t = 0.0   # elapsed simulation time
angle = Angle()
while robot.step(TIME_STEP) != -1:
    kij_motor.setVelocity(10.0)
    
    #if kij_motor.
    #position = angle.set_val(t)
    #print(position)
    #kij_motor.setPosition(position)
    #kij_motor.setVelocity(10.0)
    #t += TIME_STEP / 100.0

    pass
