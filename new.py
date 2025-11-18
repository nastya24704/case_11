import turtle
#3
def branch(order, size):
    if order == 0:
        forward(size)

    x = size/(n+1)
    for i in range(order):
        forward(x)
        lt(45)
        branch(order-i-1, 0.5*x*(order-i-1))
        lt(90)
        branch(order-i-1, 0.5*x*(order-i-1))
        rt(135)
#моя
def nastya(order, size):
    if order == 0:
        forward(size)

    else:
        lt(120)
        mine(order/4, size - 1)
        rt(60)
        mine(order/4, size - 1)
        rt(120)
        mine(order/4, size - 1)
        rt(60)
        mine(order/4, size - 1)
        mine(order/4, size - 1)
        lt(60)
        mine(order, size - 1)
        lt(60)
        mine(order, size - 1)
        mine(order, size - 1)
#6
def minkowski(order, size):
    """
    Recursively draw the Minkowski curve.
    
    :param t: turtle object for drawing
    :param length: current segment length
    :param depth: recursion depth
    """
    if order == 0:
        forward(size)
    else:
        minkowski(order/4, size - 1)
        lt(90)
        minkowski(order/4, size - 1)
        rt(90)
        minkowski(order/4, size - 1)
        rt(90)
        minkowski(order/4, size - 1)
        minkowski(order/4, size - 1)
        lt(90)
        minkowski(order/4, size - 1)
        lt(90)
        minkowski(order/4, size - 1)
        rt(90)
        minkowski(order/4, size - 1)
  
