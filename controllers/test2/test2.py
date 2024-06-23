"""test2 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
from math import pi, sin
from enum import Enum

TIME_STEP = 16
robot = Robot()
kij_motor = robot.getDevice("kij_motor")
kij_position = robot.getDevice("kij_position")

arm_motor = robot.getDevice("rotational motor")

kij_position.enable(1000)

class Angle():
    val = 0

    def set_val(self, val):
        self.val = val*pi
        return self.val


F = 2.0   # frequency 2 Hz
t = 0.0   # elapsed simulation time
angle = Angle()

arm_motor.setPosition(1)


to_pos = 3.14
starting_pos = False
while robot.step(TIME_STEP) != -1:
    pos = kij_position.getValue()
    print(pos)

    if not starting_pos:
        kij_motor.setPosition(-1)
        if pos <= 0.0:
            starting_pos = True
        continue

    if pos >= 3.13 or pos <= -3.13:
        to_pos = -to_pos
    kij_motor.setPosition(0.0)
