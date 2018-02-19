import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """Creates a GUI with a drop down menu, and buttons with keyboard
       binding to move the robot."""
    mqtt_j = com.MqttClient()
    mqtt_j.connect_to_ev3()

    root = tkinter.Tk()
    root.geometry('300x300')

    menu = tkinter.Menu(root)
    root.config(menu=menu)

    orderMenu = tkinter.Menu(menu)
    menu.add_cascade(label='Order', menu=orderMenu)

    orderMenu.add_command(label='Cheeseburgers', font=('Times', '12'),
                          command=lambda: handle_cheeseburger(
                              mqtt_j))
    orderMenu.add_command(label='Salad', font=('Times', '12'),
                          command=lambda: handle_salad(mqtt_j))
    orderMenu.add_command(label='Pizza', font=('Times', '12'),
                          command=lambda: handle_pizza(mqtt_j))
    orderMenu.add_separator()
    orderMenu.add_command(label='Cart', font=('Times', '12'),
                          command=lambda: handle_cart(mqtt_j))
    orderMenu.add_command(label='Clear Cart', font=('Times', '12'),
                          command=lambda: handle_clear(mqtt_j))
    orderMenu.add_command(label='Leave Grocery', font=('Times', '12'),
                          command=lambda: handle_leave(mqtt_j))

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: forward_callback(mqtt_j,
                                                         left_speed_entry,
                                                         right_speed_entry)
    root.bind('<Up>', lambda event: forward_callback(mqtt_j,
                                                     left_speed_entry,
                                                     right_speed_entry))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: left_callback(mqtt_j,
                                                   left_speed_entry,
                                                   right_speed_entry)
    root.bind('<Left>', lambda event: left_callback(mqtt_j,
                                                    left_speed_entry,
                                                    right_speed_entry))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: stop_callback(mqtt_j, )
    root.bind('<space>', lambda event: stop_callback(mqtt_j))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: right_callback(mqtt_j,
                                                     left_speed_entry,
                                                     right_speed_entry)
    root.bind('<Right>', lambda event: right_callback(mqtt_j,
                                                      left_speed_entry,
                                                      right_speed_entry))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: back_callback(mqtt_j,
                                                   left_speed_entry,
                                                   right_speed_entry)
    root.bind('<Down>', lambda event: back_callback(mqtt_j,
                                                    left_speed_entry,
                                                    right_speed_entry))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_j)
    root.bind('<u>', lambda event: send_up(mqtt_j))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_j)
    root.bind('<j>', lambda event: send_down(mqtt_j))

    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_j, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_j, True))

    root.mainloop()


def handle_cheeseburger(mqtt):
    mqtt.send_message('getCheeseburgers')


def handle_salad(mqtt):
    mqtt.send_message('getSalad')


def handle_pizza(mqtt):
    mqtt.send_message('getPizza')


def handle_cart(mqtt):
    mqtt.send_message('readCart')


def handle_clear(mqtt):
    mqtt.send_message('clearCart')


def handle_leave(mqtt):
    mqtt.send_message('leaveGrocery')


def forward_callback(mqtt_client, left_speed_entry, right_speed_entry):
    print("move_forward")
    mqtt_client.send_message("move_forward", [int(left_speed_entry.get()),
                                              int(right_speed_entry.get())])


def left_callback(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("turn_left", [int(left_speed_entry.get()),
                                           int(right_speed_entry.get())])


def stop_callback(mqtt_client):
    mqtt_client.send_message("stop")


def right_callback(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("turn_right", [int(left_speed_entry.get()),
                                            int(right_speed_entry.get())])


def back_callback(mqtt_client, left_speed_entry, right_speed_entry):
    mqtt_client.send_message("move_back", [int(left_speed_entry.get()),
                                           int(right_speed_entry.get())])


def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


main()
