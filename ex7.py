class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MAX_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item =="x":
            raise ValueError("Access dined")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, name, value):
        if name=='z':
            raise ArithmeticError("Invalid attribute name")
        object.__setattr__(self, name, value)

    def __getattr__(self, item):
        return False
    
    def __delattr__(self, name):
        print("__Defattr__: "+name)
        
pt1 = Point(1, 3)
pt2 = Point(10, 20)
print(pt1.yy)

