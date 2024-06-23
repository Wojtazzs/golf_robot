"""caddie_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from time import sleep

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

ball_lock = robot.getDevice("ball block")
ball_push = robot.getDevice("ball push")
ball_top_lock = robot.getDevice("ball top block")

def next_ball():
    robot.step(128*timestep)
    ball_lock.setPosition(-0.6)
    robot.step(128*timestep)
    ball_push.setPosition(-0.3)
    robot.step(128*timestep)
    ball_lock.setPosition(-0.2)
    robot.step(128*timestep)
    ball_push.setPosition(0.0)
    robot.step(128*timestep)
    ball_top_lock.setPosition(-0.1)
    robot.step(timestep)
    ball_top_lock.setForce(10.0)
    ball_top_lock.setPosition(0.2)
    robot.step(128*timestep)

for _ in range(3):
    next_ball()

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
