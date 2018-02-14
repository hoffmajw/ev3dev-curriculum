
import ev3dev.ev3 as ev3
import time
import robot_controller as robo


def getCheeseburgers(robot):
    print('--------------------------------------')
    print('Getting ingredients for cheeseburgers.')
    print('--------------------------------------')

#    robot.move_forward(300, 300)

    while True:
        if robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
            print('found red')
            robot.stop()
            print('begin speaking')
            ev3.Sound.speak('Tomato added to cart').wait()
            time.sleep(.5)
            ev3.Sound.beep().wait()
            print('speaking finished')
            robot.items_in_cart = robot.items_in_cart + ['Tomato']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
                print()
            #     robot.move_forward(300, 300)

        # elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BROWN:
        #     robot.stop()
        #     ev3.Sound.speak('Ground beef added to cart.').wait()
        #     robot.items_in_cart = robot.items_in_cart + ['Ground Beef']
        #     robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
            print('Found green')
            robot.stop()
            print('begin speaking')
            ev3.Sound.speak('Lettuce added to cart').wait()
            time.sleep(.5)
            ev3.Sound.beep().wait()
            print('finished speaking')
            robot.items_in_cart = robot.items_in_cart + ['Lettuce']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
                print()
            #     robot.move_forward(300, 300)

        # elif robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
        #     robot.stop()
        #     ev3.Sound.speak('Mustard added to cart.').wait()
        #     robot.items_in_cart = robot.items_in_cart + ['Mustard']
        #     robot.move_forward(300, 300)
        # elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
        #     robot.stop()
        #     ev3.Sound.speak('Onions added to cart.').wait()
        #     robot.items_in_cart = robot.items_in_cart + ['Onions']
        #     robot.move_forward(300, 300)

        elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
            print('found blue')
            robot.stop()
            print('begin speaking')
            ev3.Sound.speak('Cheese added to cart').wait()
            time.sleep(.5)
            ev3.Sound.beep().wait()
            print('finished speaking')
            robot.items_in_cart = robot.items_in_cart + ['Cheese']

            while robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
                print()
            #     robot.move_forward(300, 300)

        if len(robot.items_in_cart) == 5:
            break

    return robot.items_in_cart


def getSalad(robot):
    print('--------------------------------')
    print('Getting ingredients for a salad.')
    print('--------------------------------')

    if robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
        robot.stop()
        ev3.Sound.speak('Tomato added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Tomato']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BROWN:
        robot.stop()
        ev3.Sound.speak('Croutons added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Croutons']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
        robot.stop()
        ev3.Sound.speak('Lettuce added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Lettuce']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
        robot.stop()
        ev3.Sound.speak('Shredded cheese added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Shredded cheese']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
        robot.stop()
        ev3.Sound.speak('Salad dressing added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Salad dressing']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
        robot.stop()
        ev3.Sound.speak('Carrots added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Carrots']
        robot.move_forward(900)

    return robot.items_in_cart


def getPizza(robot):
    print('--------------------------------')
    print('Getting ingredients for a pizza.')
    print('--------------------------------')

    robot.move_forward(500, 500)

    if robot.color_sensor.color is ev3.ColorSensor.COLOR_RED:
        robot.stop()
        ev3.Sound.speak('Tomato added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Tomato']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BROWN:
        robot.stop()
        ev3.Sound.speak('Croutons added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Croutons']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_GREEN:
        robot.stop()
        ev3.Sound.speak('Lettuce added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Lettuce']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_YELLOW:
        robot.stop()
        ev3.Sound.speak('Shredded cheese added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Shredded cheese']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLACK:
        robot.stop()
        ev3.Sound.speak('Salad dressing added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Salad dressing']
        robot.move_forward(900)
    elif robot.color_sensor.color is ev3.ColorSensor.COLOR_BLUE:
        robot.stop()
        ev3.Sound.speak('Carrots added to cart.').wait()
        robot.items_in_cart = robot.items_in_cart + ['Carrots']
        robot.move_forward(900)

    return robot.items_in_cart


def readCart(items_in_cart):
    print('----------------')
    print('Reading cart.')
    print('----------------')

    print(items_in_cart)

    for k in range(len(items_in_cart)):
        ev3.Sound.speak(items_in_cart[k]).wait()


def leaveGrocery():
    print('----------------')
    print('Leaving grocery.')
    print('----------------')


def main():
    cart = robo.Snatch3r()

    btn = ev3.Button()

    while True:
        choice = input('"c" for cheeseburger, "s" for salad, "p" for pizza, '
                       'or "cart" to see whats in your cart:    ')
        print()

        if choice == 'c':
            getCheeseburgers(cart)

        elif choice == 's':
            getSalad(cart)

        elif choice == 'p':
            getPizza(cart)

        elif choice == 'cart':
            readCart(cart.items_in_cart)

        if btn.backspace:
            break


main()
