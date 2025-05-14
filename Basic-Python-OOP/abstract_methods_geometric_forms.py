from abc import ABC, abstractmethod

class GeometricShape(ABC):

  @abstractmethod
  def area(self):
    ...
  @abstractmethod
  def perimeter(self):
    pass

class Square(GeometricShape):
  def __init__(self, area, perimeter, side):
    super().__init__(area, perimeter)
    self.side = side

  def get_side(self):
    return self.side

  def set_side(self, new_side):
    self.side = new_side

  def area(self):
    vl_area = self.side ** 2
    return vl_area

  def perimeter(self):
    vl_perimeter = 4 * self.side
    return vl_perimeter

class Circle(GeometricShape):
  def __init__(self, area, perimeter, radius):
    super().__init__(area, perimeter)
    self.radius = radius

  def get_radius(self):
    return self.radius

  def set_radius(self, new_radius):
    self.radius = new_radius

  def area(self):
    vl_area = 3.14 * self.radius ** 2
    return vl_area

  def perimeter(self):
    vl_perimeter = 2 * 3.14 * self.radius
    return vl_perimeter
