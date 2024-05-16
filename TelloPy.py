# Network: TELLO-D3BBEC

from djitellopy import Tello

drone = Tello()

drone.connect()
drone.takeoff()

drone.flip('f')

drone.land()