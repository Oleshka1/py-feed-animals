class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        food_amount = self.appetite
        if not self.is_hungry:
            food_amount = 0
        if self.is_hungry and self.appetite > 0:
            food_amount = self.appetite
            print(f"Eating {food_amount} food points...")
            self.appetite = 0
            self.is_hungry = False
        return food_amount


class Cat(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True) -> None:
        super().__init__(name, appetite, is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    food_amount = 0
    for animal in animals:
        if animal.is_hungry:
            temp = animal.feed()
            food_amount += temp
    return food_amount
