#!/usr/bin/env python3
"""
Authors: David Fisher and Jaxon Hoffman and Garrett Jacobs.
"""

import tkinter
from tkinter import ttk
import ev3dev.ev3 as jacobsgmev3
import time
import jacobsgmrobotcontroller as robo
import mqtt_remote_method_calls as com


def main():
    # a MyDelegate class.  Simply construct the MqttClient with no parameter in the constructor (easy).
    color_to_seek_list = []
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()


    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: forward_callback(mqtt_client)
    root.bind('<Up>', lambda event: forward_callback(mqtt_client))

    left_button = ttk.Button(main_frame, text="Turn Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: left_callback(mqtt_client)
    root.bind('<Left>', lambda event: left_callback(mqtt_client))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: stop_callback(mqtt_client,)
    root.bind('<space>', lambda event: stop_callback(mqtt_client))

    right_button = ttk.Button(main_frame, text="Turn Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: right_callback(mqtt_client)
    root.bind('<Right>', lambda event: right_callback(mqtt_client))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: back_callback(mqtt_client)
    root.bind('<Down>', lambda event: back_callback(mqtt_client))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def forward_callback(mqtt_client):
    mqtt_client.send_message("move_forward",[600,600])

def back_callback(mqtt_client):
    mqtt_client.send_message("move_back",[600,600])

def left_callback(mqtt_client):
    mqtt_client.send_message("turn_degrees",90,600)

def right_callback(mqtt_client):
    mqtt_client.send_message("turn_degrees",-90,600)

def stop_callback(mqtt_client):
    mqtt_client.send_message("stop")




# Arm command callbacks
def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()

#Start of my own methods

def drive_to_color(button_state, robot, color_to_seek):
    """
    When the button_state is True (pressed), drives the robot forward until the desired color is detected.
    When the color_to_seek is detected the robot stops moving forward and reacts to each color accordingly.
    """

    if button_state:

        while True:
            robot.move_forward(300, 300)
            if robot.color_sensor.color == color_to_seek:
                robot.stop()
                break

        jacobsgmev3.Sound.speak("Found " + COLOR_NAMES[color_to_seek]).wait()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
