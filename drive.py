import RPi.GPIO as GPIO
import time 

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)    # ENDB
    GPIO.setup(11, GPIO.OUT)    # logic 1
    GPIO.setup(13, GPIO.OUT)    # logic 2
    GPIO.setup(22, GPIO.OUT)    # ENDA
    GPIO.setup(15, GPIO.OUT)    # logic 3
    GPIO.setup(29, GPIO.OUT)    # logic 4

def move_forward_full_speed(): # Both spinn clockwise at full speed
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)

def stop():
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)

def main():
    move_forward_full_speed()
    sleep(1)
    stop()

if __name__ == "__main__":
    # execute only if run as a script
    main()


