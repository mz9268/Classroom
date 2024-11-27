class Polygon:
    def __init__(self,name,sides):
        self.name=name
        self.sides=sides
    
    def get_name(self):
        return self.name
    
    def set_name(self,new_name):
        self.name=new_name

    def get_sides(self):
        return self.sides
    
    def set_sides(self,new_sides):
        self.sides=new_sides
    def __str__(self):
        return f"Polygon(name={self.name}, sides={self.sides})"

def main():
    polygon1=Polygon("triangle",[3,3,3])
    polygon2=Polygon("square",[4,4,4,4])
    print(polygon1)
    print(polygon2)
    print(polygon1.get_name())
    print(polygon1.get_sides())
    polygon1.set_name("trapezium")
    polygon1.set_sides([4,4,4,4])
    print(polygon1)

main()

        