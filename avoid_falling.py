#import libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# initialize brick, motors, and sensor
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ultrasonic_sensor = UltrasonicSensor(Port.S4)

wheel_diameter = 5.6 #input wheel dimension

def drive_forward(distance, speed):
    degrees = distance / (3.14 * wheel_diameter) * 360 #wheel diameter
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    while left_motor.angle() < degrees and right_motor.angle() < degrees:
        #checking for obstacles
        reflected_light_intensity = ColorSensor.reflection()
        if reflected_light_intensity < 10:  # Adjust this threshold based on your table and environment
            left_motor.stop()
            right_motor.stop()
            ev3.speaker.beep()
            return  # Stop the loop
        
        left_motor.run(speed)
        right_motor.run(speed)
        wait(10)
    
    left_motor.stop()
    right_motor.stop()

def turn_right(angle, speed):
    left_motor.run_angle(speed, angle, then=Stop.HOLD, wait=True)
    right_motor.run_angle(-speed, angle, then=Stop.HOLD, wait=True) 

#execute 
drive_forward(50, 200)
wait(1000)
turn_right(180, 100)
wait(1000)
drive_forward(50, 200)