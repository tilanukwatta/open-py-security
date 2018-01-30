#!/usr/bin/env python

from datetime import timedelta, datetime
import time
import picamera


if __name__ == '__main__':
    
    print(datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0))
    
    camera = picamera.PiCamera()

    record = True
    while record:
      image_name = "image.jpg"
      camera.capture()
      time.sleep(60)  

    #import ipdb; ipdb.set_trace() # debugging code

