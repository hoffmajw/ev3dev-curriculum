import ev3dev.ev3 as ev3
import robot_controller_final as robo
import mqtt_remote_method_calls as com
import time


def getCheeseburgers(robot):
    """Instructs the cart to look for some cheeseburger ingredients, returns
       the items in the cart"""

    print('--------------------------------------')
    print('Getting ingredients for cheeseburgers.')
    print('--------------------------------------')

    count = 0

    while True:
        if len(robot.items_in_cart) == 5:
            robot.stop()
            break

        robot.move_forward(300, 300)

        if robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
            robot.stop()

            ev3.Sound.speak('Tomato added to cart')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Tomato']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
            robot.stop()

            ev3.Sound.speak('Lettuce added to cart')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Lettuce']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
            robot.stop()

            if count == 0:
                ev3.Sound.speak('Ground beef added to cart.')

                time.sleep(5)

                robot.items_in_cart = robot.items_in_cart + ['Ground Beef']
                count += 1
            else:
                ev3.Sound.speak('Cheese added to cart')

                time.sleep(5)

                robot.items_in_cart = robot.items_in_cart + ['Cheese']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
            robot.stop()

            ev3.Sound.speak('Onions added to cart.')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Onions']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
            robot.stop()

            if count == 0:
                ev3.Sound.speak('Ground beef added to cart.')

                time.sleep(5)

                robot.items_in_cart = robot.items_in_cart + ['Ground Beef']
                count += 1
            else:
                ev3.Sound.speak('Cheese added to cart')

                time.sleep(5)

                robot.items_in_cart = robot.items_in_cart + ['Cheese']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
                robot.move_forward(300, 300)

        elif robot.touch_sensor.is_pressed:
            clearCart(robot)
            leaveGrocery(robot)
            break

    return robot.items_in_cart


def getSalad(robot):

    """Instructs the cart to get some ingredients for a salad, returns the
       items in the cart"""
    print('--------------------------------')
    print('Getting ingredients for a salad.')
    print('--------------------------------')
    count = 0
    while True:
        if len(robot.items_in_cart) == 5:
            robot.stop()
            break

        robot.move_forward(300, 300)

        if robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
            robot.stop()

            ev3.Sound.speak('Tomato added to cart')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Tomato']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
            robot.stop()

            ev3.Sound.speak('Lettuce added to cart')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Lettuce']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
            robot.stop()

            ev3.Sound.speak('Cheese added to cart.')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Cheese']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
            robot.stop()

            ev3.Sound.speak('Croutons added to cart.')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Croutons']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
            robot.stop()

            if count == 0:
                ev3.Sound.speak('Ranch added to cart.')

                time.sleep(5)

                robot.items_in_cart = robot.items_in_cart + ['Ranch']
                count += 1
            else:
                ev3.Sound.speak('Cheese added to cart')

                time.sleep(5)

                robot.items_in_cart = robot.items_in_cart + ['Cheese']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
                robot.move_forward(300, 300)

        elif robot.touch_sensor.is_pressed:
            clearCart(robot)
            leaveGrocery(robot)
            break

    return robot.items_in_cart


def getPizza(robot):
    """Instructs the robot to get som ingredients for a pizza, returns the
       items in the cart"""

    print('--------------------------------')
    print('Getting ingredients for a pizza.')
    print('--------------------------------')
    count = 0
    while True:
        if len(robot.items_in_cart) == 5:
            robot.stop()
            break

        robot.move_forward(300, 300)

        if robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
            robot.stop()

            ev3.Sound.speak('Pepperoni added to cart')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Pepperoni']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
            robot.stop()

            ev3.Sound.speak('Peppers added to cart')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Peppers']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
            robot.stop()

            ev3.Sound.speak('Cheese added to cart.')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Cheese']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
            robot.stop()

            ev3.Sound.speak('Crust added to cart.')

            time.sleep(5)

            robot.items_in_cart = robot.items_in_cart + ['Crust']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
                robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
            robot.stop()

            if count == 0:
                ev3.Sound.speak('Mushrooms added to cart.')

                time.sleep(5)

                robot.items_in_cart = robot.items_in_cart + ['Mushrooms']
                count += 1
            else:
                ev3.Sound.speak('Cheese added to cart')

                time.sleep(5)

                robot.items_in_cart = robot.items_in_cart + ['Cheese']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
                robot.move_forward(300, 300)

        elif robot.touch_sensor.is_pressed:
            clearCart(robot)
            leaveGrocery(robot)
            break

    return robot.items_in_cart


def readCart(robot):
    """Reads and prints the items in the cart"""

    print('-------------')
    print('Reading cart.')
    print('-------------')

    print(robot.items_in_cart)

    ev3.Sound.speak('You have these items in your cart.')
    time.sleep(2.0)
    for k in range(len(robot.items_in_cart)):
        ev3.Sound.speak(robot.items_in_cart[k])
        time.sleep(1.25)


def clearCart(robot):
    """Removes all items from a cart, setting the cart's items to an empty
    list of strings (the cart can only hold 5 items"""
    print('--------------')
    print('Clearing cart.')
    print('--------------')

    ev3.Sound.speak('Cart cleared. There is nothing in your cart.')
    robot.items_in_cart = []


def leaveGrocery(robot):
    """Tells the user you are done at the grocery"""

    print('----------------')
    print('Leaving grocery.')
    print('----------------')

    robot.turn_degrees(450, 900)
    ev3.Sound.speak('All done at the grocery.')


def main():
    cart = robo.Snatch3r()

    btn = ev3.Button()
    btn.process()
    if btn.backspace:
        exit()

    mqtt_j = com.MqttClient(cart)
    mqtt_j.connect_to_pc()

    cart.loop_forever()


if __name__ == "__main__":
    main()
