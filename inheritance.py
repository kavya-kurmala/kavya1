class Shape:
    def __init__(self,length):
        self.length=length
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__(length)
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print(a) 
class Square(Rectangle):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
    def Area(self):
        s=self.length*self.length
        print(s)
class Cube(Square):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)
        self.height=height
    def volume(self):
        vol=self.length*self.breadth*self.height
        print(vol)
rect=Rectangle(2,3)
rect.area()
squ=Square(2,4)
squ.Area()
cube=Cube(2,3,4)
cube.volume()
