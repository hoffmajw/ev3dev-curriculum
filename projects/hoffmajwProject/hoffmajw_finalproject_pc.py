import tkinter


def main():
    root = tkinter.Tk()
    root.geometry('300x300')

    menu = tkinter.Menu(root)
    root.config(menu=menu)

    orderMenu = tkinter.Menu(menu)
    menu.add_cascade(label='Order', menu=orderMenu)
    orderMenu.add_command(label='Cheeseburgers', font=('Times', '12'),
                          command=getCheeseburgers(cart))
    orderMenu.add_command(label='Salad', font=('Times', '12'), command=getSalad)
    orderMenu.add_command(label='Pizza', font=('Times', '12'), command=getPizza)
    orderMenu.add_separator()
    orderMenu.add_command(label='Cart', font=('Times', '12'),
                          command=readCart(cart.items_in_cart))
    orderMenu.add_command(label='Leave Grocery', font=('Times', '12'),
                          command=leaveGrocery)

    root.mainloop()


main()
