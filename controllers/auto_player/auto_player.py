"""auto_player controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Camera
from controller import Supervisor


# create the Robot instance.
# robot = Robot()
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


kamera = robot.getDevice("camera") # 64x64
kamera.enable(100)
kij_motor = robot.getDevice("kij_motor")
kij_position = robot.getDevice("kij_position")
kij_brake = robot.getDevice("kij_brake")
kij_brake.setDampingConstant(0)
kij_position.enable(1000)

kij_motor.setVelocity(0.0)
# robot.step(16*128*timestep)
# kij_motor.setVelocity(0.3)
# kij_motor.setPosition(1.0)

arm_motor = robot.getDevice("rotational motor")
arm_motor.setVelocity(2.0)

final_block = robot.getDevice(f"ball top block q")

top_blocks = []

for i in range(3):
    top_blocks.append(robot.getDevice(f"ball top block {i}"))

# arm_motor.setPosition(1.0)

_counter = 0
def get_next_ball():
    global _counter

    top_blocks[_counter].setPosition(0.13)
    # print(f"Remove {i}")
    # robot.getFromDef("ROBOT").remove()
    if _counter <= 2:
        _counter = _counter + 1
    robot.step(32*128*timestep)
    kamera.saveImage(f"test{_counter}.jpg", 50)
    
    img = kamera.getImage()
    
    r = kamera.imageGetRed(img, 64, 16, 32)
    g = kamera.imageGetGreen(img, 64, 16, 32)
    b = kamera.imageGetBlue(img, 64, 16, 32)
    
    print(f"r{r}, g{g}, b{b}")
    robot.step(32*128*timestep)
    
    return { "r": r, "g": g, "b": b}


def reales_ball():
    final_block.setPosition(-0.3)
    robot.step(16*128*timestep)
    final_block.setPosition(0.3)
    robot.step(timestep)

position_counter = 0

def arm_turn_right():
    global position_counter
    if position_counter % 2 == 0:    
        position_counter = position_counter + 1
    else:
        return None
    arm_motor.setPosition(-1.57)
    robot.step(512*timestep)
    
def arm_turn_left():
    global position_counter
    if position_counter % 2 != 0:    
        position_counter = position_counter - 1
    else:
        return None
    arm_motor.setPosition(0.0)
    robot.step(512*timestep)

def swing():
    kij_motor.setVelocity(1.0)
    robot.step(timestep)
    kij_motor.setPosition(0.0)
    robot.step(128*timestep)
    kij_motor.setPosition(-2.0)
    robot.step(512*timestep)
    kij_motor.setPosition(1.0)
    robot.step(128*timestep)
    print("Neutral")
    kij_motor.setPosition(0.0)
    robot.step(2048*timestep)
    kij_brake.setDampingConstant(500)
    robot.step(2*2048*timestep)
    kij_motor.setVelocity(0.0)
    print("halt")


# piłki zielone #00d700 char: g77
# piłki czerwone #d70000 char: r72

# arm_turn_right()
# arm_turn_right()

# get_next_ball()
# reales_ball()
# get_next_ball()
# reales_ball()
# get_next_ball()
# reales_ball()


# swing()
# kamera.saveImage("test.jpg", 50)
# print("click")

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    color_dict = get_next_ball()
    if color_dict["r"] < 50:
        print("G")
        if position_counter % 2 == 0:
            arm_turn_right()
        reales_ball()
        swing()
    elif color_dict["r"] >= 50:
        print("R")
        if position_counter % 2 != 0:
            arm_turn_left()
        reales_ball()
        swing()
    else:
        print("N")
        continue

    # print(kij_position.getValue())
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
