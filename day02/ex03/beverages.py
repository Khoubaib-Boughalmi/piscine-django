class HotBeverage:
    def __init__(self) -> None:
        self.price: float = 0.30
        self.name: str = "hot beverage"
    
    def description(self):
        return "Just some hot water in a cup"
    
    def  __str__(self):
        print (f"""
            name : {self.name}
            price : {round(self.price, 2)}
            description : {self.description()}
        """)

class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.name: str = "coffee"
        self.price: float = 0.40
    def description(self) -> str:
        return "A coffee, to stay awake."

class Tea(HotBeverage):
     def __init__(self) -> None:
        super().__init__()
        self.name: str = "tea"
    
class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.name: str = "chocolate"
        self.price: float = 0.50
    def description(self) -> str:
        return "Chocolate, sweet chocolate..."
   
class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.name: str = "cappuccino"
        self.price: float = 0.45
    def description(self) -> str:
        return "Un po’ di Italia nella sua tazza!"


if __name__ == '__main__':
    hotBeverage = HotBeverage()
    hotBeverage.__str__()
    coffee = Coffee()
    coffee.__str__()
    tea = Tea()
    tea.__str__()
    chocolate = Chocolate()
    chocolate.__str__()
    cappuccino = Cappuccino()
    cappuccino.__str__()