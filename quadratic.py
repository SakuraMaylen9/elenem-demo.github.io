import math

def solve_quadratic (a, b, c):
    dis = b * b - 4 * a * c  
    if dis > 0:
        return (-b + math.sqrt(b * b - 4 * a * c)/ (2 * a)) and (-b - math.sqrt(b * b - 4 * a *c)/ (2 * a))
    if dis == 0:
        return ( -b / 2 * a)
    if dis < 0: 
        return None

solve_quadratic(1, -5, 6)

