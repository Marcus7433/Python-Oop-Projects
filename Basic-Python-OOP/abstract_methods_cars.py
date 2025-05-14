from abc import ABC, abstractmethod

class Car(ABC):
  base_price = 100
  def __init__(self, model):
    self.model = model

  @abstractmethod
  def daily_price(self):
    pass

  def get_model(self):
    return self.model
  def set_model(self, new_model):
    self.model = new_model

  @classmethod
  def get_base_price(cls):
    return cls.base_price

  @classmethod
  def set_base_price(cls, new_base_price):
    cls.base_price = new_base_price

class Economy(Car):
  def __init__(self, model):
    super().__init__(model)

  def daily_price(self):
    daily_price1 = Car.base_price * 1.05
    return daily_price1

class Intermediate(Car):
  def __init__(self, model):
    super().__init__(model)

  def daily_price(self):
    daily_price1 = Car.base_price * 1.10
    return daily_price1

if __name__ == '__main__':
  economy1 = Economy("HB20")
  print(economy1.daily_price())
  Car.set_base_price(150)
  print(economy1.daily_price())
