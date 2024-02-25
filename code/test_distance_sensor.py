from src import distance_sensor as distance_sensor_module
import time
import matplotlib.pyplot as plt


if __name__ == '__main__':

    total_seconds = 30
    sample_hz = 24

    distance_sensor1 = distance_sensor_module.DistanceSensor({
        "pins": {
            "echo": 23,
            "trigger": 24
        }
    })

    distance_sensor2 = distance_sensor_module.DistanceSensor({
        "pins": {
            "echo": 17,
            "trigger": 27
        }
    })
    
    start_time = time.time()

    timestamps = []
    distances1 = []
    distances2 = []

    while time.time() - start_time < total_seconds:
        loop_start = time.time()

        # Collect data
        timestamp = time.time() - start_time
        distance1 = distance_sensor1.distance
        distance2 = distance_sensor2.distance

        # Print data
        print(1, distance1)
        print(2, distance2)

        # Append data to lists
        timestamps.append(timestamp)
        distances1.append(distance1)
        distances2.append(distance2)

        # Sleep to maintain sample rate
        time.sleep(max(0, 1/sample_hz - (time.time() - loop_start)))

    # Plotting
        plt.plot(timestamps, distances1, label='Distance Sensor 1')
        plt.plot(timestamps, distances2, label='Distance Sensor 2')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Distance (cm)')
        plt.title('Distance vs Time')
        plt.legend()
        plt.pause(0.001)
        plt.clf()
        # plt.grid(True)
        # plt.show()

    # start_time = time.time()
    # while time.time() - start_time < total_seconds:

    #     loop_start = time.time()

    #     print(1, distance_sensor1.distance)
    #     print(2, distance_sensor2.distance)

    #     time.sleep(max(0, 1/sample_hz -
    #                    (time.time() - loop_start)))
