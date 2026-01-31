def equilateral(sides):
    a,b,c = sides
    if a>0 and b>0 and c>0:
        if a+b>=c and a+c>=b and b+c>=a:
            if a==c and a==b:
                return True
            return False
        return False
    return False
    
def isosceles(sides):
    a,b,c = sides
    if a>0 and b>0 and c>0:
        if a+b>=c and a+c>=b and b+c>=a:
            if a==c or a==b or b==c:
                return True
            return False
        return False
    return False

def scalene(sides):
    a,b,c = sides
    if a>0 and b>0 and c>0:
        if a+b>=c and a+c>=b and b+c>=a:
            if a!=b and a!=c and b!=c:
                return True
            return False
        return False
    return False