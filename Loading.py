import time
import sys

start_time = time.time()


#class Loading():

def loading(animation = "|/-\\", startTime = 5, text = "Hi. On behalf of Loading Community ! ", speed = 0.2):
        while True:
            for i in range(10):
                time.sleep(speed)  # Feel free to experiment with the speed here
                sys.stdout.write(f"\r{text}" + animation[i % len(animation)])
                sys.stdout.flush()
            sys.stdout.flush()
            if time.time() - start_time > startTime:  # The animation will last for 10 seconds
                sys.stdout.flush()
                break

#loading(text = "Hello..")
