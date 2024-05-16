# Network: TELLO-D3BBEC

from djitellopy import Tello

drone = Tello()

drone.connect()
drone.takeoff()

def flip_forward(self):
    """Flip forward."""
    self.flip("f")
   
flip_forward()

drone.land()