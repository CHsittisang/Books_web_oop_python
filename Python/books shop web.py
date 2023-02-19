class Pro:
    def __init__(self,
                 name,
                 unit, 
                 tag, 
                 price, 
                 date,
                 pro_type,
                 pro_id,
                 pro_supply) -> None:
        self.name = name
        self.unit = unit
        self.tag = tag
        self.price = price
        self.date = date
        self.pro_type = pro_type
        self.pro_id = pro_id
        self.pro_supply = pro_supply

class Home:
    def __init__(self) -> None:
        pass

class User:
    def __init__(self,
                 username, 
                 password) -> None:
        self.username = username
        self.password = password

class Admin:
    def __init__(self,
                 username, 
                 password) -> None:
        self.username = username
        self.password = password

class Oder:
    def __init__(self,
                 price, 
                 unit) -> None:
        self.price = price
        self.unit = unit

class Payment:
    def __init__(self,
                 pay_with) -> None:
        self.pay_with = pay_with


