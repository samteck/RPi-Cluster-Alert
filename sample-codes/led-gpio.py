#importing the library to use GPIO pins and time
import RPi.GPIO as IO
import time

# setting mode for GPIO pins and disabling intial GPIO warnings
IO.setwarnings(False)
IO.setmode(IO.BCM)

# initializing variables
led = 2
i = 0

IO.setup(led,IO.OUT)

while (i<5) :
    IO.output(led,IO.HIGH)
    time.sleep(0.5)
    IO.output(led,IO.LOW)
    time.sleep(0.5)
    i+=1

IO.cleanup()
