'''Khalifa Almari
Muhammed Zayed
Rihaan Ritesh Nair'''

import turtle

turn = 90

#Instruction: Drawing a cake using turtle on python!

#Khalifa Almarri's Part.
def measurements():
    turtle.speed(0)
    turtle.pensize(2)
    turtle.bgcolor("light blue")

#Khalifa Almarri's Part. "Drawing the plate of the birthday cake!"
def plate(x,y,color_fill):
    turtle.goto(x,y)
    turtle.pendown
    turtle.fillcolor(color_fill)
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(turn)
    turtle.forward(10)
    turtle.left(turn)
    turtle.forward(200)
    turtle.left(turn)
    turtle.forward(10)
    turtle.left(turn)
    turtle.forward(100)
    turtle.end_fill()

#Khalifa Almarri's Part. *Drawing the first layer of the cake!*
def layer1(x,y,color_fill1):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pencolor(color_fill1)
    turtle.pendown()
    turtle.fillcolor(color_fill1)
    turtle.begin_fill()
    turtle.forward(70)
    turtle.left(turn)
    turtle.forward(50)
    turtle.left(turn)
    turtle.forward(140)
    turtle.left(turn)
    turtle.forward(50)
    turtle.left(turn)
    turtle.forward(70)
    turtle.end_fill()

#Khalifa Almarri's Part. *Drawing the first layer of the cake!*
def layer1(x,y,color_fill1):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(color_fill1)
    turtle.begin_fill()
    turtle.forward(70)
    turtle.left(turn)
    turtle.forward(50)
    turtle.left(turn)
    turtle.forward(140)
    turtle.left(turn)
    turtle.forward(50)
    turtle.left(turn)
    turtle.forward(70)
    turtle.end_fill()

#Khalifa Almarri's Part. *Drawing a hazelnut Frosting (blurywood), for the first layer of the cake!*
def frosting1(x,y,color_fill):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pencolor(color_fill)
    turtle.pendown()
    turtle.fillcolor(color_fill)
    turtle.begin_fill()
    turtle.forward(70)
    turtle.left(turn)
    turtle.forward(10)
    turtle.left(turn)
    turtle.forward(140)
    turtle.left(turn)
    turtle.forward(10)
    turtle.left(turn)
    turtle.forward(70)
    turtle.end_fill()

#Khalifa Almarri's Part. *Drawing the second layer of the cake!*
def layer2(x,y,color_fill2):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pencolor(color_fill2)
    turtle.pendown()
    turtle.fillcolor(color_fill2)
    turtle.begin_fill()
    turtle.forward(60)
    turtle.left(turn)
    turtle.forward(25)
    turtle.left(turn)
    turtle.forward(120)
    turtle.left(turn)
    turtle.forward(25)
    turtle.left(turn)
    turtle.forward(60)
    turtle.end_fill()

#Khalifa Almarri's Part. *Drawing a hazelnut Frosting (burlywood), for the second layer of the cake!*
def frosting2(x,y,color_fill):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pencolor(color_fill)
    turtle.pendown()
    turtle.fillcolor(color_fill)
    turtle.begin_fill()
    turtle.forward(60)
    turtle.left(turn)
    turtle.forward(7)
    turtle.left(turn)
    turtle.forward(120)
    turtle.left(turn)
    turtle.forward(7)
    turtle.left(turn)
    turtle.forward(60)
    turtle.end_fill()

#Khalifa Almarri's Part. *Drawing the third layer of the cake!*
def layer3(x,y,color_fill3):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pencolor(color_fill3)
    turtle.pendown()
    turtle.fillcolor(color_fill3)
    turtle.begin_fill()
    turtle.forward(30)
    turtle.left(turn)
    turtle.forward(20)
    turtle.left(turn)
    turtle.forward(60)
    turtle.left(turn)
    turtle.forward(20)
    turtle.left(turn)
    turtle.forward(30)
    turtle.end_fill()

#Khalifa Almarri's Part. *Drawing a hazelnut Frosting (blurywood), for the second layer of the cake!*
def frosting3(x,y,color_fill):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pencolor(color_fill)
    turtle.pendown()
    turtle.fillcolor(color_fill)
    turtle.begin_fill()
    turtle.forward(30)
    turtle.left(turn)
    turtle.forward(5)
    turtle.left(turn)
    turtle.forward(60)
    turtle.left(turn)
    turtle.forward(5)
    turtle.left(turn)
    turtle.forward(30)
    turtle.end_fill()

#Rihaan Ritesh's Part. *Drawing the Table's legs!*
def table_leg():
   turtle.forward(100)
   turtle.right(turn)
   turtle.forward(100)
   turtle.right(turn)
   turtle.forward(20)
   turtle.right(turn)
   turtle.forward(100)

#Rihaan Ritesh's Part. *Drawing the Table's top!*
def table(x,y,color_fill):
   turtle.pencolor("gray0")
   turtle.goto(x,y)
   turtle.pendown()
   turtle.left(180)
   turtle.fillcolor(color_fill)
   turtle.begin_fill()
   turtle.forward(200)
   turtle.left(turn)
   turtle.forward(20)
   turtle.left(turn)
   turtle.forward(400)
   turtle.left(turn)
   turtle.forward(20)
   turtle.left(turn)
   turtle.forward(400)
   turtle.end_fill()
   turtle.left(turn)
   turtle.forward(20)
   turtle.left(turn)
   turtle.begin_fill()
   table_leg()
   turtle.right(turn)
   turtle.forward(140)
   table_leg()
   turtle.end_fill()
   turtle.penup()
   turtle.goto(x,y)
   turtle.left(turn)
   turtle.forward(200)
   turtle.pendown()

#Khalifa Almarri's Part. *Drawing some toppings on the cake "M&Ms"!*
def m_n_m(x,y,color_fill,radius):
   turtle.tracer(False)
   turtle.penup()
   turtle.pencolor(color_fill)
   turtle.goto(x,y-radius)
   turtle.pendown()
   turtle.fillcolor(color_fill)
   turtle.begin_fill()
   turtle.circle(6)
   turtle.end_fill()
   turtle.tracer(True)

#Muhammad Zayed's part. "each type of berry topping and its attricutes"
def cherry():
    turtle.up()
    turtle.goto(0, 120)  
    turtle.down()
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.goto(0,120)
    turtle.up()
    turtle.right(turn)
    turtle.down()
    turtle.pencolor("dark green")
    turtle.forward(10)
    turtle.up()

def blueberry():
    turtle.up()
    turtle.goto(0, 120) 
    turtle.down()
    turtle.pencolor("blue")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.goto(0,120)
    turtle.up()
    turtle.right(turn)
    turtle.down()
    turtle.pencolor("dark green")
    turtle.forward(10)
    turtle.up()

def blackberry():
    turtle.up()
    turtle.goto(0, 120)  
    turtle.down()
    turtle.pencolor("purple")
    turtle.fillcolor("purple")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.goto(0,120)
    turtle.up()
    turtle.right(turn)
    turtle.down()
    turtle.pencolor("dark green")
    turtle.forward(10)
    turtle.up()

#Muhammad Zayed's part - drawing the candles

def candle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.fillcolor("white")  
    turtle.begin_fill()
    turtle.setheading(90)  
    turtle.forward(30)  
    turtle.left(turn)
    turtle.forward(7)  
    turtle.left(turn)
    turtle.forward(30)
    turtle.left(turn)
    turtle.forward(7)
    turtle.end_fill()
    turtle.hideturtle()

#Muhammad Zayed's part to draw the flame on the candle
def draw_flame(x, y):
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor("black")  
    turtle.pendown()
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.forward(3)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(3)
    turtle.left(90)
    turtle.forward(5)
    turtle.end_fill()

#Muhammad Zayed's Part. "Turning on/off the candles"
def flame_on_off():
    response = input("Do you want us to light them up? (yes/no): ")
    if response == "yes":
        print("Flame is on!")
        draw_flame(48, 117.25)  
        draw_flame(-50, 117.25)   
    else:
        print("Flame is off..")

#Muhammad Zayeds PART. "Drawing the balloons and asking the user for their details!"
def balloon(x,y,color):
    turtle.pencolor('black')
    turtle.penup()
    turtle.goto(x, y - 100)  
    turtle.pendown()
    turtle.setheading(0)  
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(50)  
    turtle.end_fill()
    turtle.pendown()
    turtle.right(90)  
    turtle.pensize(2)
    turtle.forward(100)  
    turtle.pensize(1)  


#"Assert" and "if" on input statements was made by Khalifa Ali Almarri.
def main():
   measurements()
   plate(0,0,"dark gray")
   color_fill1 = input("Please choose the color for the cake's first layer, and we'll match it with a flavor: ")
   if color_fill1=='black':
    print("Gross, Why does your layer look burnt?")
   else:
    print("Great Choice, Chef!")
   layer1(0,12.25,color_fill1) #Recommendation: lemon chiffon.
   color_fill2 = input("Please choose the color for the cake's second layer, and we'll match it with a flavor: ")
   if color_fill2=='black':
    print("Chef, Why burning the second layer too?!")
   else:
    print("Great Choice, Chef!")
   layer2(0,62.25,color_fill2) #Recommendation: pink.
   color_fill3 = input("Please choose the color for the cake's third layer, and we'll match it with a flavor: ")
   if color_fill3=='black':
    print("I'm sorry to say, your cake is RUINED..")
   else:
    print("Great Choice, Chef!")
   layer3(0,87.25,color_fill3) #Recommendation: light coral.
   print("Now, let's add our special hazelnut frosting, I'm pretty sure you'll like it!")
   frosting1(0,43,"burlywood")
   frosting2(0,74,"burlywood")
   frosting3(0,96,"burlywood")
   print("A cake won't be completed without some toppings, Let's go for some M&Ms!")
   m_n_m(50,25,"maroon",5)
   m_n_m(25,25,"lime green",5)
   m_n_m(-50,25,"gold",5)
   m_n_m(-25,25,"deep sky blue",5)
   m_n_m(0,25,"medium orchid",5)
   turtle.penup()
   print("Let's place it down on a table now, shall we?")
   table(0,0,"sienna4")
   choice = input("Oh, the cake's missing it's signature touch, whats your pick?! (cherry, blueberry, blackberry): ")
   if choice == "blackberry":
        print("Blackberries won't taste good with this flavor.")
        blackberry()
   elif choice == "cherry":
        print("Cherries are a great choice!")
        cherry()
   elif choice == "blueberry":
        print("Cherries would taste better, but whatever you want!")
        blueberry()
   else:
        print("Invalid choice! Drawing a cherry by default.")
        cherry()
   print("Now, lets add the candles!")
   candle(53,87.25)  
   candle(-45,87.25)   
   flame_on_off()
   color=input("what color do you want the balloon to be:")
   balloon(200,300,color)
   balloon(-200,300,color)
   turtle.hideturtle()
   print("Chef, this cake is a work of ART!")

   input("Please press on the button \"Enter\" to exit:")

#Call out the functions!
if __name__=="__main__":
   main()

