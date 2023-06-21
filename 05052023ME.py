# class Item:
#     def __init__(self, name, price):
#        self.name = name
#         self.price = price

#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int):
#             return self.price + other

# item1 = Item('Видеокарта', 20000)
# item2 = Item('Бархатные тяги', 100000000000)

# print(item1 + 50)


from tkinter import *
import random

window = Tk()
window.geometry('600x600')

class Fire:
    image = PhotoImage(file='elements/free-icon-fire-9509865.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay

class Water:
    image = PhotoImage(file='elements/free-icon-water-drop-4246703.png').subsample(4, 4)

class Earth:
    image = PhotoImage(file='elements/ground.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay


class Wind:
    image = PhotoImage(file='elements/wind.png').subsample(4, 4)

class Clay:
    image = PhotoImage(file='elements/free-icon-pottery-7942410.png').subsample(4, 4)


elements = [Fire(), Earth(), Water(), Wind()]

canvas = Canvas(window, width=600, height=600)
canvas.pack()

for elem in elements:
    img = canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)

def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)

    if len(images_id) == 2:
        elem1 = elements[images_id[0]-1]
        elem2 = elements[images_id[1]-1]

        new_element = elem1 + elem2

        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)

    canvas.coords(images_id, event.x, event.y)

    print(images_id)

window.bind('<B1-Motion>', move)

window.mainloop()



