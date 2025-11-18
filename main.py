from turtle import *
import math


def koch(order: int, size: float) -> None:
    """"
    The function draws a Koch curve of a given order and size recursively.

    Args:
        order (int):  The depth of the recursion (the order of the curve).
        if order=0 - straight line
        size (float): Length of the current curve segment

    Returns:
        None: The function draws and does not return values.
    """

    if order == 0:
        forward(size)
    else:
        koch(order - 1, size / 3)
        lt(60)
        koch(order - 1, size / 3)
        rt(120)
        koch(order - 1, size / 3)
        lt(60)
        koch(order - 1, size / 3)


def snowflake_koch(order, size) -> None:
    """
    The function draws the Koch snowflake - three copies of the Koch curve,
    built (with the tips facing out) on the sides of a regular triangle.

    Args:
        order (int):  The depth of the recursion  for Koch curves.
        if order=0 - straight line
        size (float): Length of the current curve segment

    Returns:
        None: Функция выполняет отрисовку, не возвращает значений
    """

    for side in range(3):
        koch(order, size)
        right(120)


def branch(order: int, size: float) -> None:
    """
    Recursively draws a fractal tree with decreasing branch complexity.

    Args:
        order (int): recursion depth - determines the complexity and number of branching levels
        size (float): Length of the current curve segment

    Returns:
        None: The function only draws the tree and doesn't return any value.
    """

    if order == 0:
        forward(size)
        return

    x = size / (order + 1)
    for i in range(order):
        forward(x)
        lt(45)
        branch(order - i - 1, 0.5 * x * (order - i - 1))
        lt(90)
        branch(order - i - 1, 0.5 * x * (order - i - 1))
        rt(135)
    forward(x)
    left(180)
    forward(size)


def draw_tree(depth: int, size: float, angle: float) -> None:
    """
    The function draws a colored fractal tree recursively.

    Args:
        depth (int): Depth of recursion (defines the number of branching levels)
        size (float):  Length of the current branch
        angle (float): The angle between the left and right branches

    Returns:
        None: The function only draws branches.
    """

    if depth == 0:
        return

    colormode(255)
    green_component = 255 - int(depth * (250 / 6)) % 255
    color(0, green_component, 0)

    forward(size)

    right(angle)
    draw_tree(depth - 1, size / 2, angle)

    left(angle * 2)
    draw_tree(depth - 1, size / 2, angle)

    right(angle)
    backward(size)


def square_fractal(depth: int, size: float) -> None:
    """
    Recursively draws a fractal square.

    Args:
    size (float): side size of the square
    depth (int): recursion depth

    Returns:
        None: The function only draws squares.
    """

    if depth == 0:
        return

    for _ in range(4):
        forward(size)
        right(90)
    forward(size * 0.1)
    right(10)
    square_fractal(depth - 1, size * 0.9)


def ice_1(dpth: int, size: float) -> None:
    """
    Draws a recursive ice-like fractal.

    Args:
        dpth (int): The recursion depth.
        size (float): The length of the current segment.
    Returns:
        None: The function only draws.
    """

    if dpth == 0:
        forward(size)
    else:
        ice_1(dpth - 1, size / 2)
        left(90)
        ice_1(dpth - 1, size / 4)
        left(180)
        ice_1(dpth - 1, size / 4)
        left(90)
        ice_1(dpth - 1, size / 2)


def minkowski(order: int, size: float) -> None:
    """"
    Recursively draw the Minkowski curve.

    Args:
        order (int): recursion depth - determines the level of detail in the curve
        size (float): current segment length

    Returns:
        None: The function only draws the curve and doesn't return any value.
    """

    if order == 0:
        forward(size)
    else:
        minkowski(order - 1, size / 4)
        lt(90)
        minkowski(order - 1, size / 4)
        rt(90)
        minkowski(order - 1, size / 4)
        rt(90)
        minkowski(order - 1, size / 4)
        minkowski(order - 1, size / 4)
        lt(90)
        minkowski(order - 1, size / 4)
        lt(90)
        minkowski(order - 1, size / 4)
        rt(90)
        minkowski(order - 1, size / 4)


def draw_branch(length: float) -> None:
    """
    Recursively draws a branch:
    1. Draw a line forward.
    2. Make two turns to the right and left.
    3. Reduce the length of the branch.
    4. Stop when the branch is too short.

    Args:
        length (int): First line length.

    Returns:
        None: The function only draws a branches.
    """

    if length < 5:
        return

    forward(length)

    right(30)
    draw_branch(length * 0.7)

    left(60)
    draw_branch(length * 0.7)

    right(30)
    backward(length)


def ice_2(order: int, size: float) -> None:
    """
    Recursively draws the Ice #2 fractal pattern.

    Args:
        order (int): recursion depth - determines the level of fractal detail
        size (float): current segment length

    Returns:
        None: The function only draws the fractal and doesn't return.
    """

    if order == 0:
        forward(size)
    else:
        ice_2(order - 1, size)
        for _ in range(2):
            lt(120)
            ice_2(order - 1, size / 2)
            rt(180)
            ice_2(order - 1, size / 2)

        lt(120)
        ice_2(order - 1, size)


def levi(order: int, size: float) -> None:
    """
    Recursively draws the Levi C curve fractal.

    Args:
        order (int): recursion depth - determines the complexity of the curve
        size (float): current segment length

    Returns:
        None: The function only draws the curve and doesn't return.
    """

    if order == 0:
        forward(size)
    else:
        lt(45)
        levi(order - 1, size / (2 ** 0.5))
        rt(90)
        levi(order - 1, size / 2 ** 0.5)
        lt(45)


def k_fractal(order: int, size: float) -> None:
    """
    Recursively draws a K-shaped fractal pattern.

    Args:
        order (int): recursion depth - determines the level of detail in the K pattern
        size (float): current segment length

    Returns:
        None: The function only draws the fractal and doesn't return.
    """

    if order == 0:
        forward(size)
    else:

        lt(90)
        k_fractal(order - 1, 2 * size / 5)
        rt(135)
        k_fractal(order - 1, (2 * size / 5) * (2 ** 0.5))
        lt(45)
        k_fractal(order - 1, size / 5)
        lt(45)
        k_fractal(order - 1, (2 * size / 5) * (2 ** 0.5))
        rt(135)
        k_fractal(order - 1, 2 * size / 5)
        lt(90)


def spiral_triangle(order: int, size: float) -> None:
    """
    Draws a recursive spiral triangle fractal.

    Args:
        order (int): Recursion depth.
        size (float): Length of the triangle side.

    Returns:
        None: The function only draws the fractal and doesn't return.
    """

    if order == 0:
        for _ in range(3):
            forward(size)
            left(120)
    else:
        for _ in range(3):
            forward(size)
            left(120)
            penup()
            forward(size / 2)
            right(60)
            pendown()
            spiral_triangle(order - 1, size / 2)
            penup()
            left(60)
            backward(size / 2)
            pendown()


def nastya(depth: int, length: float) -> None:
    """
    Recursively draws the Nastya fractal curve.

    Args:
        depth (int): recursion depth - determines the level of detail in the curve
        length (float): current segment length

    Returns:
        None: The function only draws the curve and doesn't return any value.
    """

    if depth == 0:
        forward(length)
    else:
        length /= 4

        left(120)
        nastya(depth - 1, length)

        right(60)
        nastya(depth - 1, length)

        right(120)
        nastya(depth - 1, length)

        right(60)
        nastya(depth - 1, length)

        nastya(depth - 1, length)

        left(60)
        nastya(depth - 1, length)

        left(60)
        nastya(depth - 1, length)

        nastya(depth - 1, length)


def fractal_line(order: int, size: float) -> None:
    """
    Recursively draws a fractal curve based on the Koch curve.

    Args:
        order (int): Recursion level (0 is a straight line)
        size (float): The length of the curve segment

    Returns:
        None: The function only draws the fractal and doesn't return.
    """

    if order == 0:
        forward(size)
    else:
        fractal_line(order - 1, size / 2)
        left(120)
        fractal_line(order - 1, size / 2)
        right(60)
        fractal_line(order - 1, size / 2)
        left(120)
        fractal_line(order - 1, size / 2)


def spiral_composition(depth, length) -> None:
    """"
    Draws a spiral composition of fractal curves.

    Args:
        depth (int): The level of recursion for fractals
        length (float): The base length of the segment
    Returns:
        None: The function draws and does not return values.
    """

    for ray_ind in range(6):
        up()
        goto(0, 0)

        spiral_offset = ray_ind * 15
        setheading(ray_ind * 45 + spiral_offset)
        down()

        current_size = length * (0.8 - ray_ind * 0.08)

        for fractal_small in range(2):
            fractal_line(depth, current_size / (fractal_small + 1))
            right(120 + ray_ind * 5)


def main() -> None:
    """
    The main function of the program.
    Requests parameters from the user and initiates drawing fractals
    """

    fractals = {
        '1': 'Кривая Коха',
        '2': 'Ледяной 1',
        '3': 'Ледяной 2',
        '4': 'Кривая Леви',
        '5': 'Двоичное дерево',
        '6': 'Снежинка Коха',
        '7': 'Квадрат',
        '8': 'Уникальный фрактал 1',
        '9': 'Уникальный фрактал 2',
        '10': 'Уникальный фрактал 3',
        '11': 'Уникальный фрактал 4',
        '12': 'Кривая Минковского',
        '13': 'Фрактал "Ветка"'
    }
    print("Выберите фрактал:")
    for key, name in fractals.items():
        print(f"{key}. {name}")

    choice = input("Введите номер (1-13): ").strip()

    if choice not in fractals:
        print("Некорректный ввод.")
        exit()

    if choice == '11':
        depth = int(input('Глубина рекурсии (1-3): '))
        length = int(input('Длина стороны (70-180): '))
    else:
        depth = int(input('Глубина рекурсии: '))
        length = int(input('Длина стороны: '))
    up()

    match choice:
        case '1':
            x_coord = -length // 2
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            koch(depth, length)

        case '2':
            x_coord = -2 * length
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            ice_1(depth, length)

        case '3':
            x_coord = -2 * length
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            ice_2(depth, length)

        case '4':
            x_coord = -length // 2
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            levi(depth, length)

        case '5':
            try:
                angle = int(input('Угол ветвления:'))
            except ValueError:
                print("неправильно введён угол")
            x_coord = 0
            y_coord = 0
            setposition(x_coord, y_coord)
            left(90)
            down()
            draw_tree(depth, length, angle)

        case '6':
            x_coord = -length // 2
            y_coord = length // 2
            setposition(x_coord, y_coord)
            down()
            snowflake_koch(depth, length)

        case '7':
            x_coord = 0
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            square_fractal(depth, length)

        case '8':
            x_coord = -length // 2
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            k_fractal(depth, length)

        case '9':
            bgcolor("black")
            color("orange")
            x_coord = -length / 2
            y_coord = -length / (2 * math.sqrt(3))
            setposition(x_coord, y_coord)
            down()
            spiral_triangle(depth, length)

        case '10':
            x_coord = 0
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            nastya(depth, length)

        case '11':
            x_coord = 0
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            spiral_composition(depth, length)

        case '12':
            x_coord = 0
            y_coord = 0
            setposition(x_coord, y_coord)
            down()
            minkowski(depth, length)

        case '13':
            x_coord = 0
            y_coord = 0
            setposition(x_coord, y_coord)
            left(90)
            down()
            branch(depth, length)

    update()
    done()


if __name__ == "__main__":
    main()
