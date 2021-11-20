import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

motor1 = [32,36,38,40]
motor2 = [31,33,35,37]

for pin in motor1:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
    
for pin in motor2:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
    
seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1],]

rev = [[0,0,0,1],
       [0,0,1,1],
       [0,0,1,0],
       [0,1,1,0],
       [0,1,0,0],
       [1,1,0,0],
       [1,0,0,0],
       [1,0,0,1],]

for i in range(32):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(motor1[pin],seq[halfstep][pin])
            GPIO.output(motor2[pin],seq[halfstep][pin])
        time.sleep(0.001)
        
time.sleep(1)      

 
GPIO.cleanup()
