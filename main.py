# rbps ?

import turtle
screen = turtle.Screen()

screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# def get_coor_mouse_click(x,y):
#     print(x,y)

# turtle_coodinates = turtle.onscreenclick(get_coor_mouse_click)
# turtle.mainloop()

answer_state = screen.textinput(title = "Guess The State!", prompt = "What is another state?" )
screen.exitonclick()