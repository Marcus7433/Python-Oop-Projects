class Account(object):
  def __init__(self, name = 'undefined', balance = 0):
    self.name = name
    self.balance = balance

    def get_name(self):
      return self.name
    def get_balance(self):
      return self.balance

    def set_name(self, new_name):
      self.name = new_name
    def set_balance(self, new_balance):
      self.balance = new_balance


class Individual(Account):
    def __init__(self, name, balance, cpf, gender):
        super().__init__(name, balance)
        self.cpf = cpf
        self.gender = gender

class Business(Account):
    def __init__(self, name, balance, cnpj, type):
        super().__init__(name, balance)
        self.cnpj = cnpj
        self.type = type

if __name__ == '__main__':
  account1 = Account('Joao', 10000)
