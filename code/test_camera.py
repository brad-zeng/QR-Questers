from src import camera as camera_module
import time
import cv2
# import pyrealsense2 as rs

if __name__ == '__main__':

    total_seconds = 60
    sample_hz = 10

    camera = camera_module.Camera({
        "show_preview": True
    })
    start_time = time.time()
    
    # if camera.cam is not None:
    #     try:
    #         while True:
    #             camera.capture()
    #             # frame = camera.image_array[..., [2, 1, 0, 3]]
    #             # # Display the frame
    #             # cv2.imshow('Live Feed', frame)
    #             if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
    #                 break
    #     finally:
    #         camera.cam.stop()
    #         cv2.destroyAllWindows()
    # else:
    #     print("Camera not initialized properly.")

    
    # camera.capture()
    print(camera.image_array)
    # data_bgra = camera.image_array[..., [2, 1, 0, 3]]
    # image = cv2.imwrite('output.png', data_bgra )
    # cv2.imshow('Image', image)

    while time.time() - start_time < total_seconds:
        camera.capture()
        print(camera.image_array)

        time.sleep(max(0, 1/sample_hz -
                       (time.time() - start_time)))
