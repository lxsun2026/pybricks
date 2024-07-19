# Import libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait

# Initialize brick, motors, and sensors
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S3)

wheel_diameter = 5.6

def move_forward(distance, speed):
    degrees = distance / (3.14 * wheel_diameter) * 360  
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    while left_motor.angle() < degrees and right_motor.angle() < degrees:
        left_motor.run(speed)
        right_motor.run(speed)
        wait(10)
    
    left_motor.stop()
    right_motor.stop()

def move_backward(distance, speed):
    degrees = distance / (3.14 * wheel_diameter) * 360
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    while left_motor.angle() > -degrees and right_motor.angle() > -degrees:
        left_motor.run(-speed)
        right_motor.run(-speed)
        wait(10)
    
    left_motor.stop()
    right_motor.stop()

def turn_right(angle, speed):
    left_motor.run_angle(speed, angle, then=Stop.HOLD, wait=True)
    right_motor.run_angle(-speed, angle, then=Stop.HOLD, wait=True)

def turn_left(angle, speed):
    left_motor.run_angle(-speed, angle, then=Stop.HOLD, wait=True)
    right_motor.run_angle(speed, angle, then=Stop.HOLD, wait=True)

def pick_up_object():
    arm_motor.run_angle(500, 90, then=Stop.HOLD, wait=True) 
    wait(500)

def drop_object():
    arm_motor.run_angle(-500, 90, then=Stop.HOLD, wait=True)  
    wait(500)

def return_to_start():
    turn_right(180, 100)
    move_backward(30, 200)  
    turn_left(180, 100)  

def sort_colors():
    while True:
        move_forward(10, 200) 
        detected_color = color_sensor.color()
        
        if detected_color == Color.RED:
            ev3.speaker.beep()
            pick_up_object()
            move_forward(20, 200)  
            drop_object()
            return_to_start() 
        elif detected_color == Color.GREEN:
            ev3.speaker.beep()
            pick_up_object()
            turn_left(90, 100)
            move_forward(20, 200) 
            drop_object()
            return_to_start()  
        elif detected_color == Color.BLUE:
            ev3.speaker.beep()
            pick_up_object()
            turn_right(90, 100)
            move_forward(20, 200) 
            drop_object()
            return_to_start() 
        else:
            ev3.speaker.beep(frequency=400, duration=1000)  #error beep

#run sorting
sort_colors()
