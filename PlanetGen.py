import pygame

# Mid-Point Circle Drawing Algorithm


def CircleDraw(x_centre, y_centre, r, grid):
    x = r
    y = 0

    # Printing the initial point the
    # axes after translation
    grid.update_cell(x + x_centre, y + y_centre, 1)
    grid.update_cell(x_centre, y_centre - r, 1)
    grid.update_cell(x_centre - r, y_centre, 1)

    # When radius is zero only a single
    # point be printed
    if r > 0:
        grid.update_cell(x + x_centre, -y + y_centre, 1)
        grid.update_cell(y + x_centre, x + y_centre, 1)
        grid.update_cell(-y + x_centre, x + y_centre, 1)

    # Initialising the value of P
    P = 1 - r

    while x > y:

        y += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1

        # Mid-point outside the perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        # All the perimeter points have
        # already been printed
        if x < y:
            break

        # Printing the generated point its reflection
        # in the other octants after translation
        grid.update_cell(x + x_centre, y + y_centre, 1)
        grid.update_cell(-x + x_centre, y + y_centre, 1)
        grid.update_cell(x + x_centre, -y + y_centre, 1)
        grid.update_cell(-x + x_centre, -y + y_centre, 1)

        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x != y:
            grid.update_cell(y + x_centre, x + y_centre, 1)
            grid.update_cell(-y + x_centre, x + y_centre, 1)
            grid.update_cell(y + x_centre, -x + y_centre, 1)
            grid.update_cell(-y + x_centre, -x + y_centre, 1)

    return grid
