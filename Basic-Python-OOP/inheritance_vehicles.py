class Vehicle(object):
    def __init__(self, model, price, km = 0):
        self.model = model
        self.price = price
        self.km = km

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def get_km(self):
        return self.km

    def set_model(self, new_model):
        self.model = new_model

    def set_price(self, new_price):
        self.price = new_price

    def set_km(self, new_km):
        self.km = new_km

    def update_price(self, new_price):
      if new_price > 0:
        self.price = self.price + new_price
      else:
        print("Invalid value.")

    def update_price_pct(self, pct):
      self.price = self.price + self.price * (pct / 100)

    def vehicle_status(self):
      if self.km == 0:
        print("New vehicle.")
      elif self.km <= 20000:
        print("Slightly used vehicle.")
      else:
        print("Used vehicle.")


class Car(Vehicle):
    def __init__(self, model, price, num_doors=0, km=0):
        super().__init__(model, price, km)
        self.num_doors = num_doors

    def get_num_doors(self):
        return self.num_doors

    def set_num_doors(self, new_num_doors):
        self.num_doors = new_num_doors

    def __str__(self):
        return f"Model: {self.model}, Price: {self.price}, Mileage: {self.km}, Number of doors: {self.num_doors}"

class Motorcycle(Vehicle):
    def __init__(self, model, price, cc, km=0):
        super().__init__(model, price, km)
        self.cc = cc

    def get_cc(self):
        return self.cc

    def set_cc(self, new_cc):
        self.cc = new_cc

if __name__ == '__main__':
    car1 = Car("HB20", 50000, 4)
    car2 = Car("Uno", 30000, 4, 10000)
    car3 = Car("Civic", 100000)

    motorcycle1 = Motorcycle("Bis", 10000, 50)
    motorcycle2 = Motorcycle("__", 20000, 100)

    print(vars(car1))
    print(motorcycle1.__dict__)

    car2.vehicle_status()
