import turtle
#3
def branch(n, size):
    if n == 0:
        left(180)
        return

    x = size/(n+1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        right(135)
#моя
def nastya(t, length, depth):
    """
    Построение кривой рекурсивно.

    :param t: объект turtle.
    :param length: длина текущей линии.
    :param depth: глубина рекурсии.
    """
    if depth == 0:
        t.forward(length)
    else:
        length /= 4
        t.left(120)
        mine(t, length, depth - 1)
        t.right(60)
        mine(t, length, depth - 1)
        t.right(120)
        mine(t, length, depth - 1)
        t.right(60)
        mine(t, length, depth - 1)
        mine(t, length, depth - 1)
        t.left(60)
        mine(t, length, depth - 1)
        t.left(60)
        mine(t, length, depth - 1)
        mine(t, length, depth - 1)
#6
def minkowski_curve(t, length, depth):
    """
    Recursively draw the Minkowski curve.
    
    :param t: turtle object for drawing
    :param length: current segment length
    :param depth: recursion depth
    """
    if depth == 0:
        t.forward(length)
    else:
        length /= 4
        minkowski_curve(t, length, depth - 1)
        t.left(90)
        minkowski_curve(t, length, depth - 1)
        t.right(90)
        minkowski_curve(t, length, depth - 1)
        t.right(90)
        minkowski_curve(t, length, depth - 1)
        minkowski_curve(t, length, depth - 1)
        t.left(90)
        minkowski_curve(t, length, depth - 1)
        t.left(90)
        minkowski_curve(t, length, depth - 1)
        t.right(90)
        minkowski_curve(t, length, depth - 1)
  
