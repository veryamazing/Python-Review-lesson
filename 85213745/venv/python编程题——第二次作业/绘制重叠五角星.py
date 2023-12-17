import turtle as t
def draw_fiveStars(leng):
    count = 1
    while count <= 5:
        t.forward(leng)
        t.right(144)
        count += 1
    leng += 10
    if leng <= 100:
        draw_fiveStars(leng)
def main():
    t.penup()
    t.backward(100)
    t.pendown()
    t.pensize(2)
    t.pencolor('blue')
    segment = 50
    draw_fiveStars(segment)
    t.exitonclick()
if __name__ == '__main__':
    main()