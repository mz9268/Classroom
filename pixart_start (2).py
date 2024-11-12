from turtle import Screen, Turtle

turta = Turtle()
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'
TURN = 90

def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2) # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

#Khalifa Almarri's part.
def get_color(color_string):
    color = "Invalid"
    if color_string == "0":
        color = 'black'
    elif color_string == "1":
        color = 'white'
    elif color_string == "2":
        color = 'red'
    elif color_string == "3":
        color = 'yellow'
    elif color_string == "4":
        color = 'orange'
    elif color_string == "5":
        color = 'green'
    elif color_string == "6":
        color = 'yellowgreen'
    elif color_string == "7":
        color = 'sienna'
    elif color_string == "8":
        color = 'tan'
    elif color_string == "9":
        color = 'gray'
    elif color_string == "A":
        color = 'darkgray'
    return color

#Khalifa Almarri's part.
def draw_color_pixel(color,turta):
    '''Drawing a pixel with the size of 30 from each side (4), then filling it with a color.
    we've used a range of (4) in a "for loop" in order to draw 4 sides which creates a pixel'''
    turta.fillcolor(color)
    turta.begin_fill()
    for x in range(4): 
        turta.forward(PIXEL_SIZE)
        turta.right(TURN)
    turta.forward(30)
    turta.end_fill()

#Khalifa Almarri's part.
def draw_pixel(color_string, turta):
    '''Checking the color if it's included within the color pallete *get_color(color_string)*, if not
    Error will be raise.'''
    color = get_color(color_string)
    if color != "Invalid":
        draw_color_pixel(color,turta)
    else:
        print("Error: write the correct color code!")

#Khalifa Almarri's part.
def draw_line_from_string(color_string, turta):
    '''Rechecking if the color in the palette is valid in order to start drawing a line of pixels.'''
    for x in color_string:
        color = get_color(x)
        if color == "Invalid":
            return False
        else:
            draw_pixel(x, turta)
    return True

#Khalifa Almarri's part.
def draw_shape_from_string(turta):
    '''Now, let's ask the user for some color code strings with some conditions in order to create a grid'''

    color_1 = input("Enter your first row's color code: ") 
    color_2 = input("Enter your second row's color code:  ")
    print("Now, let's draw a checkered grid with the pattern's you've provided..")

    '''We've used the process of For the switch between the two color codes,
    we applied EVEN and ODD row numbers. First color code to even rows, the second color code to odd rows.
    In this way, the colors switch, forming a checkered design.'''
    for row in range(20):  #20 is the amount of drawing the rows we'll be creating or the (End Point), which is adjustable!
        if row % 2 == 0:
            color_string = color_1  
        else:
            color_string = color_2
        if color_string == "":
            print("Looks like your not entering any value, Exiting...")
            break
        elif draw_line_from_string(color_string,turta):
            '''The movement of the cursor in order to draw a new row under each'''
            turta.penup()
            turta.setheading(270) 
            turta.forward(PIXEL_SIZE)
            turta.setheading(0)
            '''We've used the negative sign as a form of going back'''
            turta.forward(-20 * PIXEL_SIZE)
            turta.pendown()
        else:
            print("Invalid color code entered, Exiting...")
            break


def draw_shape_from_file(file_name):
    '''Creating a file draw_Shape_from_file to ask the user for the file of their choice (provided in the activity) 
and then read the contents of the file and draw the content'''
    with open(file_name,'r') as x:
        for data in x:
            data = data.strip()   
            if draw_line_from_string(data, turta):
                cursor_row_movement()
            else:
                print("Invalid color code give, try again later..")
                break                      
    print("image printed successfully")

def cursor_row_movement():
            '''The movement of the cursor in order to draw a new row under each'''
            turta.penup()
            turta.setheading(270) 
            turta.forward(PIXEL_SIZE)
            turta.setheading(0)
            '''We've used the negative sign as a form of going back'''
            turta.forward(-20 * PIXEL_SIZE)
            turta.pendown()

def main():
    initialization(turta)
    draw_shape_from_string(turta)
    file_name=input("enter the filepath of the file u choose")
    draw_shape_from_file(file_name)
    input("Press any key to exit: ")
    


if __name__ == "__main__":
    main()

#Color code for the first row is: 02020202020202020202. Then on the second row: 20202020202020202020