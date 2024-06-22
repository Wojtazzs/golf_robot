"""test controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
from math import pi, sin
from enum import Enum

TIME_STEP = 16
robot = Robot()
kij_motor = robot.getDevice("kij_motor")
kij_position = robot.getDevice("kij_position")

kij_position.enable(1000)

class Angle():
    val = 0
    def set_val(self, val):
        self.val = val*pi
        return self.val
    

F = 2.0   # frequency 2 Hz
t = 0.0   # elapsed simulation time
angle = Angle()

to_pos = 3.14
starting_pos = False
while robot.step(TIME_STEP) != -1:
    pos = kij_position.getValue()
    
    if starting_pos == False:
        kij_motor.setPosition(-1)
        if pos <= 0.0:
            starting_pos = True
        continue
            
    if pos >= 3.13 or pos <= -3.13:
        to_pos = -to_pos
    kij_motor.setPosition(to_pos)   
    #if kij_motor.
    #position = angle.set_val(t)
    #print(position)
    #kij_motor.setPosition(position)
    #kij_motor.setVelocity(10.0)
    #t += TIME_STEP / 100.0

    pass
