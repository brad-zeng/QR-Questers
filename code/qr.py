import cv2
import numpy as np
import time
from src import camera as camera_module


if __name__ == '__main__':
    qcd = cv2.QRCodeDetector()
    total_seconds = 1000
    sample_hz = 200

    camera = camera_module.Camera({
        "show_preview": True
    })
    start_time = time.time()

    while time.time() - start_time < total_seconds:
        camera.capture()
        frame = camera.image_array
        frame = np.array(frame)
        
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        
        if ret_qr:
            avg = [sum(x) / len(x) for x in points]
            print(avg)
            for s, p in zip(decoded_info, points):
                if s:
                    print(s)
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        
        # Display the frame
        cv2.imshow('Live Feed', frame)
        time.sleep(max(0, 1/sample_hz - (time.time() - start_time)))


# while True:
#     ret, frame = cap.read()
#     print(frame)
#     frame = np.array(frame)

#     if ret:
#         ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
#         if ret_qr:
#             avg = [sum(x) / len(x) for x in points]
#             print(avg)
#             for s, p in zip(decoded_info, points):
#                 if s:
#                     print(s)
#                     color = (0, 255, 0)
#                 else:
#                     color = (0, 0, 255)
#                 frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
#         cv2.imshow(window_name, frame)

#     if cv2.waitKey(delay) & 0xFF == ord('q'):
#         break

# cv2.destroyWindow(window_name)