class Person:
    def __init__(self , name ) -> None:
        self.name = name
        
    def talk(self):
        print(f"I am  {self.name}")

n = str(input(":")).upper()
h = Person(n)

h.talk()