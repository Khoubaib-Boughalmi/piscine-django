import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self) :
        self.servings: int = 0
    class EmptyCup:
        def __init__(self) -> None:
            self.name: str = "empty cup"
            self.price: float = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired")
            
    def repair(self) -> str:
        self.servings = 0
        return "Machine is fixed should be good to go"
        
    def serve(self, derivedClass):
        if (self.servings > 10):
            raise self.BrokenMachineException()
        self.servings += 1
        return derivedClass if (random.randint(1, 10) % 2) else self.EmptyCup()
    
if __name__ == '__main__':
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    cm = CoffeeMachine()
    try:
        cm.serve(coffee)
        cm.serve(tea)
        cm.serve(coffee)
        cm.serve(cappuccino)
        cm.serve(coffee)
        cm.serve(coffee)
        cm.serve(chocolate)
        cm.serve(chocolate)
        cm.serve(cappuccino)

        cm.repair()

        cm.serve(coffee)
        cm.serve(coffee)
        cm.serve(coffee)
        cm.serve(cappuccino)
        cm.serve(cappuccino)
        cm.serve(chocolate)
        cm.serve(coffee)

        cm.repair()
        
        cm.serve(chocolate)
        cm.serve(coffee)
    except Exception as e:
        print(f"Caught an exception: {e}")
