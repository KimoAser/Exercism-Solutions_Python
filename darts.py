import math
def score(x, y):
    if math.sqrt(x**2+y**2) > 10:
        return 0
    if 5 < math.sqrt(x**2+y**2) <= 10:
        return 1
    if 1 < math.sqrt(x**2+y**2) <= 5:
        return 5
    return 10
