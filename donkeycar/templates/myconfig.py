# """ 
# My CAR CONFIG 

# This file is read by your car application's manage.py script to change the car
# performance

# If desired, all config overrides can be specified here. 
# The update operation will not touch this file.
# """

DRIVE_LOOP_HZ = 20      # the vehicle loop will pause if faster than this speed.

# Sim
DONKEY_GYM = False

# Camera
CAMERA_TYPE = "MOCK"   # (PICAM|WEBCAM|CVCAM|CSIC|V4L|D435|MOCK|IMAGE_LIST)
CAMERA_INDEX = 0

# Joystick
USE_JOYSTICK_AS_DEFAULT = True      #when starting the manage.py, when True,$
JOYSTICK_MAX_THROTTLE = 0.7         #this scalar is multiplied with the -1 to$
JOYSTICK_STEERING_SCALE = 1.0       #some people want a steering that is less$
# AUTO_RECORD_ON_THROTTLE = True      #if true, we will record whenever throttl$
CONTROLLER_TYPE = 'F710'            #(ps3|ps4|xbox|pigpio_rc|nimbus|wiiu|F710$

# VESC
DRIVE_TRAIN_TYPE = "VESC" 
VESC_MAX_SPEED_PERCENT =.2 ## Max speed as a percent of actual max speed 
VESC_SERIAL_PORT= "/dev/ttyACM0" ## check this val with ls /dev/tty* 
VESC_HAS_SENSOR= True 
VESC_START_HEARTBEAT= True 
VESC_BAUDRATE= 115200 
VESC_TIMEOUT= 0.05 
VESC_STEERING_SCALE = .5
VESC_STEERING_OFFSET = .5

SHOW_FPS = False
