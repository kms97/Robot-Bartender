import time
import argparse
import RPi.GPIO as GPIO

parser = argparse.ArgumentParser(description='How long to run the pump in seconds')
parser.add_argument('-f','--foo', help='Description for foo argument', required=True)
args = parser.parse_args()
timer = args.foo

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

time.sleep(int(timer))

GPIO.output(17, GPIO.HIGH)
GPIO.cleanup()
print("Exited")