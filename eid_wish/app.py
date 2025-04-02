import turtle
import random
import time

# Screen setup with gradient background
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Eid Mubarak - Modern Design")
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Gradient background using multiple rectangles
def draw_gradient_background():
    colors = ["#000000", "#1a1a1a", "#333333", "#4d4d4d", "#666666"]
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    for i, color in enumerate(colors):
        pen.color(color)
        pen.goto(-400, 300 - i * 120)
        pen.pendown()
        pen.begin_fill()
        pen.forward(800)
        pen.right(90)
        pen.forward(120)
        pen.right(90)
        pen.forward(800)
        pen.right(90)
        pen.forward(120)
        pen.end_fill()
        pen.right(90)
    pen.hideturtle()

draw_gradient_background()

# Create a turtle object for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Function to draw an abstract crescent moon
def draw_abstract_moon(x, y, outer_radius, inner_radius):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("#f7dc6f", "#f7dc6f")  # Gold color for moon
    pen.begin_fill()
    pen.circle(outer_radius)
    pen.end_fill()

    # Inner circle to create crescent shape
    pen.penup()
    pen.goto(x + 20, y - 15)
    pen.pendown()
    pen.color("#000000", "#000000")  # Black for inner cutout
    pen.begin_fill()
    pen.circle(inner_radius)
    pen.end_fill()

# Draw the abstract moon at the top
draw_abstract_moon(0, 200, 80, 60)

# Function to draw blinking stars
def draw_blinking_star(size, x, y):
    star = turtle.Turtle()
    star.speed(0)
    star.hideturtle()
    star.penup()
    star.goto(x, y)
    star.pendown()

    def draw_star():
        star.clear()
        star.color(random.choice(["white", "yellow", "gold", "#f7dc6f", "#f8c471"]))
        star.begin_fill()
        for _ in range(5):
            star.forward(size)
            star.right(144)
        star.end_fill()
        screen.update()
    
    # Draw initial star
    draw_star()
    
    # Set up blinking animation
    def blink():
        draw_star()
        screen.ontimer(blink, t=random.randint(300, 1000))  # Random blink interval
        
    blink()

# Draw many more blinking stars
star_positions = []
for _ in range(50):  # 50 stars total
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    size = random.randint(5, 25)
    star_positions.append((size, x, y))

for size, x, y in star_positions:
    draw_blinking_star(size, x, y)

# Write "Eid Mubarak" with glowing animation
def write_glowing_text():
    text_turtle = turtle.Turtle()
    text_turtle.speed(0)
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(0, -100)
    
    colors = ["#f7dc6f", "#f8c471", "#f9e79f", "#fad7a0", "#ffdead"]  # Warm colors
    shadow_colors = ["#b8860b", "#daa520", "#cd853f", "#d2691e", "#8b4513"]
    
    def glow():
        for i in range(10):  # Glow effect loop
            text_turtle.clear()
            
            # Draw shadow text first
            text_turtle.color(shadow_colors[i % len(shadow_colors)])
            text_turtle.write("Eid Mubarak", align="center", 
                             font=("Arial", 50, "bold"))
            
            # Draw main text slightly offset
            text_turtle.color(colors[i % len(colors)])
            text_turtle.goto(0, -100)
            text_turtle.write("Eid Mubarak", align="center", 
                             font=("Arial", 50, "bold"))
            
            screen.update()
            time.sleep(0.1)  # Glow delay
        
        # Continue glowing
        screen.ontimer(glow, t=2000)  # Repeat every 2 seconds
    
    # Initial glow
    glow()

# Write "Eid Mubarak" with glowing effect
write_glowing_text()

# Add additional decorative text
def add_decorative_text():
    deco = turtle.Turtle()
    deco.speed(0)
    deco.hideturtle()
    deco.penup()
    
    # Arabic text (Eid Mubarak)
    deco.goto(0, -180)
    deco.color("#f7dc6f")
    deco.write("عيد مبارك", align="center", font=("Arial", 30, "bold"))
    
    # Subtitle
    deco.goto(0, -220)
    deco.color("white")
    deco.write("May Allah bless you with happiness and peace", 
              align="center", font=("Arial", 14, "italic"))

add_decorative_text()

# Hide the turtle and display the window
pen.hideturtle()
screen.update()
turtle.done()