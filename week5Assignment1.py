# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name}, born in {self.origin}, and I wield the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Inherited class
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using {self.power}!")

# Another inherited class
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def use_power(self):
        print(f"{self.name} activates {self.gadget} to unleash {self.power}!")

# Example usage
hero1 = FlyingHero("SkyBolt", "Wind Surge", "Cloud City", 800)
hero2 = TechHero("Circuit", "Laser Blast", "Silicon Valley", "Arm Cannon")

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()


    