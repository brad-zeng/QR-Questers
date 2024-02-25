from . import base
import time
import numpy as np
import cv2


class Config(base.Config):
    pass


class Brain(base.Brain):

    """The autonomous Brain object, drives the vehicle autonomously based on information gathered by the sensors"""

    def __init__(self, config: Config, *arg):
        super().__init__(config, *arg)

    def logic(self):
        """If anything is detected by the distance_sensors, stop the car"""

        # # if anything is detected by the sensors, stop the car
        # self.vehicle.stop()
        # self.camera.capture()
        frame = self.camera.image_array
        frame = np.array(frame)
        qcd = cv2.QRCodeDetector()
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        stop = False
        
        if ret_qr:
            avg = [sum(x) / len(x) for x in points]
            print(avg)
            avgx = avg[0][0]
            if avgx < 280:
                self.vehicle.pivot_right()
                time.sleep(0.07)
            elif avgx > 360:
                self.vehicle.pivot_left()
                time.sleep(0.07)
            
            self.vehicle.drive_forward()
            # for s, p in zip(decoded_info, points):
            #     if s:
            #         print(s)
            #         color = (0, 255, 0)
            #     else:
            #         color = (0, 0, 255)
            #     frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        else:
            self.vehicle.stop()
            stop = True
        # Display the frame
        
        # cv2.imshow('Live Feed', frame)
        
        # time.sleep(max(0, 1/sample_hz - (time.time() - start_time)))
        
        
        for distance_sensor in self.distance_sensors:
            if distance_sensor.distance < 0.18:
                self.vehicle.stop()
                stop = True

        if not stop:
            self.vehicle.drive_forward()
            # time.sleep(0.03)
