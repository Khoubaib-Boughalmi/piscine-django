

class Intern:
    
    class Coffee:
        def __str__(self) ->str:
            return "This is the worst coffee you ever tasted."
    
    def __init__(self, Name="My name? I’m nobody, an intern, I have no name.") -> None:
        self.Name = Name
    
    def __str__(self) ->str:
        return self.Name
    
    def work(self) ->str:
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self) -> Coffee():
        return Intern.Coffee()

if __name__ == '__main__':
    mark = Intern("Mark")
    other = Intern()
    print(mark.__str__())
    print(other.__str__())
    print(mark.make_coffee())
    try:
        mark.work()
    except Exception as e:
        print(f"Caught an exception: {e}")
