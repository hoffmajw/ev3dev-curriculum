#!/usr/bin/env python3
"""
Authors: David Fisher and Jaxon Hoffman and Garrett Jacobs.
"""

import tkinter
from tkinter import ttk
import ev3dev.ev3 as ev3
import time
import jacobsgmrobotcontroller as robo
import mqtt_remote_method_calls as com


def main():
    # a MyDelegate class.  Simply construct the MqttClient with no parameter in the constructor (easy).

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Sorry! BoardGame")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    canvas = tkinter.Canvas(root)
    canvas.pack(side=tkinter.LEFT)

    scrollbar = tkinter.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tkinter.LEFT, fill='y')

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', on_configure)

    main_frame = tkinter.Frame(canvas)
    canvas.create_window((0, 0), window=main_frame, anchor='nw')
    main_frame.grid()

    photo = tkinter.PhotoImage(file='sorry.gif',width =50,height = 50)
    button1 = ttk.Button(main_frame, image=photo)
    button1.image = photo
    button1.grid(column=1)
    button1['command'] = lambda: print(' You found the hidden easter egg!, '
                                       ' You automatically win the match between'
                                       ' you and you opponent! Feel free to brag!'
                                       ' Maybe even use the Gloat function hahaha!!')

    #Buttons
    drive_to_color_button = ttk.Button(main_frame, text="Color")
    drive_to_color_button.grid(row=7, column=1)
    drive_to_color_button['command'] = lambda: drive_to_color_callback(mqtt_client)
    root.bind('<c>', lambda event: drive_to_color_callback(mqtt_client))

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

    gloat_button = ttk.Button(main_frame, text="Gloat")
    gloat_button.grid(row=5, column=0)
    gloat_button['command'] = lambda: send_gloat(mqtt_client)
    root.bind('<g>', lambda event: send_gloat(mqtt_client))

    wave_button = ttk.Button(main_frame, text="Wave")
    wave_button.grid(row=6, column=0)
    wave_button['command'] = lambda: send_wave(mqtt_client)
    root.bind('<w>', lambda event: send_wave(mqtt_client))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()

def drive_to_color_callback(mqtt_client):
    mqtt_client.send_message("drive_to_color")

def back_callback(mqtt_client):
    mqtt_client.send_message("move_back",[600,600])

def left_callback(mqtt_client):
    mqtt_client.send_message("turn_degrees",[90,600])

def right_callback(mqtt_client):
    mqtt_client.send_message("turn_degrees",[-90,600])

def stop_callback(mqtt_client):
    mqtt_client.send_message("stop")

def forward_callback(mqtt_client):
    mqtt_client.send_message("move_forward_quick",[600,600])


def send_gloat(mqtt_client):
    print("You are gloating!")
    mqtt_client.send_message("arm_up")
    mqtt_client.send_message("turn_circle")
    mqtt_client.send_message("arm_down")

def send_wave(mqtt_client):
    print("You are waving!")
    mqtt_client.send_message("arm_up")
    mqtt_client.send_message("turn_degrees",[90,600])
    mqtt_client.send_message("turn_degrees",[-90,600])
    mqtt_client.send_message("arm_down")


# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
