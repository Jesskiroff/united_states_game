# rbps ?
import turtle
import pandas


screen = turtle.Screen()

screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# def get_coor_mouse_click(x,y):
#     print(x,y)

# turtle_coodinates = turtle.onscreenclick(get_coor_mouse_click)
# turtle.mainloop()



# with open("50_states.csv" ) as united_states:
#     states_and_coordinates = united_states.read()

# # print(states_and_coordinates)

data = pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
guessed_states = []

while len (guessed_states) < 50:
    state_input = screen.textinput(title = f"{len(guessed_states)} / 50 States Correct", prompt = "What is another state?").title()
    

#if answer state is one of the states in all th estates of the 50_states.csv
    #if user gets it right:
     #create a trtle to write the name of the state at the state's x and y coordinate

if state_input in all_states:
    guessed_states.append(state_input)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == state_input]
    t.goto(int(state_data.x.item(), state_data.y.item()))
    t.write(state_data.state.item())


screen.exitonclick()