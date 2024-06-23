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
kij_brake = robot.getDevice("kij_brake")
rotation = robot.getDevice("rotational motor")

kij_position.enable(1000)
kij_brake.setDampingConstant(0)

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
returning = False


class History():
    _number = 0
    array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def avg(self):
        sum = 0
        i = 0
        while i < len(self.array):
            sum += self.array[i]
            i += 1
        return sum/len(self.array)
        
    def new(self, val):
        self.array[self._number] = val
        self._number += 1
        if self._number == len(self.array):
            self._number = 0

history = History()

while robot.step(TIME_STEP) != -1:
    pos = kij_position.getValue()
    
    history.new(pos)
    print(to_pos)
    
    if starting_pos == False:
        kij_motor.setPosition(-1)
        if pos <= 0.0:
            starting_pos = True
        continue
            
    if pos >= 1.1 or pos <= -1.1:
        returning = True
        kij_brake.setDampingConstant(5000)

    if returning:
        rotation.setPosition(pi/2)
        returning = False
        to_pos = 0
    
    if returning == False and 0.01 >= history.avg() >= -0.01:
        starting_pos = False
        rotation.setPosition(0)
        kij_brake.setDampingConstant(0)
    
    kij_motor.setPosition(to_pos)
    pass
