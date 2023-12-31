import turtle
import random
import time
import math

def draw_fireworks():
    turtle.bgcolor("black")
    turtle.title("Happy birthday !")
    turtle.speed("fastest")

    def draw_firework(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        for _ in range(36):
            turtle.color(random_color())
            draw_firework_segment()
            turtle.right(10)

    def draw_firework_segment():
        length = random.randint(50, 150)
        turtle.forward(length)
        turtle.backward(length)

    def random_color():
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]
        return random.choice(colors)

    def display_birthday_message():
        turtle.penup()
        turtle.goto(0, -200)
        turtle.pendown()
        turtle.color("white")
        turtle.hideturtle()
        turtle.write("Happy 46th birthday. Enjoy your special day !", align="center", font=("Arial", 30, "bold"))

    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        draw_firework(x, y)

    display_birthday_message()
    time.sleep(3)
    turtle.clear()


def draw_stars():
    turtle.bgcolor("black")
    turtle.title("Feu d'artifice")

    def draw_star(size):
        turtle.color(random_color())
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            turtle.right(144)
        turtle.end_fill()

    def random_color():
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]
        return random.choice(colors)

    def draw_firework():
        turtle.penup()
        turtle.goto(random.randint(-200, 200), random.randint(0, 200))
        turtle.pendown()

        for _ in range(random.randint(10, 40)):
            size = random.randint(5, 20)
            draw_star(size)
            turtle.penup()
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(50, 300)
            turtle.goto(distance * math.cos(angle), distance * math.sin(angle))
            turtle.pendown()

    for _ in range(10):
        draw_firework()

    turtle.exitonclick()

def main():
    draw_fireworks()
    draw_stars()

if __name__ == "__main__":
    main()
