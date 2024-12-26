import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
# tello.set_video_bitrate(Tello.BITRATE_4MBPS)
# tello.set_video_resolution(Tello.RESOLUTION_720P)
# tello.set_video_fps(Tello.FPS_30)
# tello.set_video_direction(Tello.CAMERA_DOWNWARD)
frame_read = tello.get_frame_read()
while True:
    frame = frame_read.frame
    img = cv2.resize(frame, (720, 480))
    cv2.imshow("Tello Stream", img)

    acceleration_x = tello.get_acceleration_x()
    acceleration_y = tello.get_acceleration_y()
    acceleration_z = tello.get_acceleration_z()
    print(f"Acceleration X: {acceleration_x} Y: {acceleration_y} Z: {acceleration_z}")

    speed_x = tello.get_speed_x()
    speed_y = tello.get_speed_y()
    speed_z = tello.get_speed_z()
    print(f"Speed X: {speed_x} Y: {speed_y} Z: {speed_z}")
    
    current_state = tello.get_current_state()
    flight_time = tello.get_flight_time()
    # tello.get_state_field("mid")o
    # print(f"Current State: {current_state}")
    # print(f"Flight Time: {flight_time}")

    pitch = tello.get_pitch()
    roll = tello.get_roll()
    yaw = tello.get_yaw()
    print(f"Pitch: {pitch} Roll: {roll} Yaw: {yaw}")

    temperature = tello.get_temperature()
    temperature_h = tello.get_highest_temperature()
    temperature_l = tello.get_lowest_temperature()
    print(f"Temperature: {temperature} °C {temperature_l} - {temperature_h}")

    battery = tello.get_battery()
    print(f"Battery: {battery}%")

    height = tello.get_height()
    tof = tello.get_distance_tof()
    barometer = tello.get_barometer()
    print(f"Height: {height} cm TOF: {tof} Barometer: {barometer} cm")

    # wifi_signal_noise_ratio = tello.query_wifi_signal_noise_ratio()
    # sdk_version = tello.query_sdk_version()
    # serial_number = tello.query_serial_number()
    # print(f"WiFi Signal Noise Ratio: {wifi_signal_noise_ratio}")
    # print(f"SDK Version: {sdk_version}")
    # print(f"Serial Number: {serial_number}")

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    # elif key == ord('o'):
    #     tello.turn_motor_on()
    # elif key == ord('p'):
    #     tello.turn_motor_off()

tello.streamoff()
cv2.destroyAllWindows()

