def ImplicitEquation (x, y, color):
    x = 0
    y = radius

    def ImplicitEquation(x, y, radius, color):
        ResetDisp()
        global n_pixels
        n_pixels = 0
        SimetricCirclePoints(x, y, cx, cy, color)
        while (y > x):
            x = x + 1
            y = int(math.sqrt(math.pow(radius, 2) - math.pow(x, 2)))
            SimetricCirclePoints(x, y, cx, cy, color)

            pygame.display.flip()

    return (n_pixels)





return