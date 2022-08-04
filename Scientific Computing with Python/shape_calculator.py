class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
      return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        self.side = width

    def set_height(self, height):
        self.height = height
        self.side = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        rows = int(self.height)
        row = "*" * self.width
        line = row + "\n"
        while rows > 1:
            line += row + "\n"
            rows -=1
        if self.width > 50 or self.height > 50:
            line = "Too big for picture."
        return line

    def get_amount_inside(self, shape_two):
        area_one = self.get_area()
        area_two = shape_two.get_area()
        num = int(area_one/area_two)
        return num



class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = self.width

    def __repr__(self):
      return f"Square(side={self.side})"

    def set_side(self, side):
        print(side)
        self.side = side
        self.width = self.side
        self.height = self.side
