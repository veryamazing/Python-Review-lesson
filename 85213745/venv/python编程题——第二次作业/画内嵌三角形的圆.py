def main():
    import turtle as t
    import math
    # import matplotlib
    t.pensize(2)
    t.right(98)
    t.penup()
    t.forward(200)
    t.pendown()
    t.left(98)

    r = 200
    t.circle(r)

    len = r *math.sqrt(3)
    t.left(60)
    t.forward(len)
    t.left(120)
    t.forward(len)
    t.left(120)
    t.forward(len)
    t.done()
if __name__ == '__main__':
    main()