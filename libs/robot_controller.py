"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import sys
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def __init__(self):

        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sensor = ev3.TouchSensor()
        self.max_speed = 900

        self.unplugged()

    def unplugged(self):
        try:
            assert self.left_motor.connected
            assert self.right_motor.connected
        except AssertionError:
            print("Motors may not be connected.", file=sys.stderr)

    def loop_forever(self):
        # This is a convenience method that I don't really recommend for most programs other than m5.
        #   This method is only useful if the only input to the robot is coming via mqtt.
        #   MQTT messages will still call methods, but no other input or output happens.
        # This method is given here since the concept might be confusing.
        self.running = True
        while self.running:
            time.sleep(0.1)

    def drive_inches(self, distance, left_sp):
        self.unplugged()

        degrees_per_inch = 90
        motor_turns_needed_in_degrees = distance * degrees_per_inch

        self.left_motor.run_to_rel_pos(
            position_sp=motor_turns_needed_in_degrees,
            speed_sp=left_sp,
            stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.right_motor.run_to_rel_pos(
            position_sp=motor_turns_needed_in_degrees,
            speed_sp=left_sp,
            stop_action=ev3.Motor.STOP_ACTION_BRAKE)

        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def turn_degrees(self, degrees_to_turn, turn_speed_sp):
        degrees_to_turn = degrees_to_turn * 4.53

        self.left_motor.run_to_rel_pos(position_sp=(-1) * degrees_to_turn,
                                       speed_sp=turn_speed_sp,
                                       stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.right_motor.run_to_rel_pos(position_sp=degrees_to_turn,
                                        speed_sp=turn_speed_sp,
                                        stop_action=ev3.Motor.STOP_ACTION_BRAKE)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def arm_calibration(self):
        self.arm_motor.run_forever(speed_sp=self.max_speed)
        while True:
            if self.touch_sensor.is_pressed:
                break
            time.sleep(0.01)
        self.arm_motor.stop()
        ev3.Sound.beep()

        arm_revolutions_for_full_range = 14.2
        self.arm_motor.run_to_rel_pos(
            position_sp=-arm_revolutions_for_full_range *
                                             360, speed_sp=self.max_speed)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)

        self.arm_motor.position = 0  # Calibrate the down position as 0 (this
        # line is correct as is).

    def move_forward(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def move_back(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=-left_speed)
        self.right_motor.run_forever(speed_sp=-right_speed)

    def turn_right(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=-right_speed)

    def turn_left(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=-left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def arm_up(self):
        #self.arm_motor.run_to_rel_pos(position_sp=360*14.2,
        # speed_sp=self.max_speed)
        self.arm_motor.run_forever(speed_sp=self.max_speed)
        while True:
            if self.touch_sensor.is_pressed:
                break
            time.sleep(0.01)
        self.arm_motor.stop()

    def arm_down(self):
        self.arm_motor.run_to_rel_pos(position_sp=-14.2 * 360,
                                      speed_sp=self.max_speed)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        # Blocks until the motor finishes running
        ev3.Sound.beep()

    def shutdown(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.arm_motor.stop()
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

        print('Goodbye!')
        ev3.Sound.speak('Goodbye!')
