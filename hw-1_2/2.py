# ------------------ 1.2 ------------------
class Spaceship:
    def __init__(self, spaceship_name: str, spaceship_type: str, startship_color: str, spaceship_price: int, spaceship_equipments: list = [], spaceship_fuel: int = 100, spaceship_energy: int = 100):
        self.name = spaceship_name
        self.type = spaceship_type
        self.color = startship_color
        self.price = spaceship_price
        self.equipments = spaceship_equipments
        self.fuel = spaceship_fuel
        self.energy = spaceship_energy

    def Fly(self):
        self.fuel -= 1

    def Refueling(self, percent):
        if self.fuel + percent > 100:
            i = percent - (100 - self.fuel)
            self.fuel = 100
            print(f"Полный бак. Лишнее топливо - {i}")
        else:
            self.fuel += percent

    def CnahgeColor(self, color):
        self.color = color

class User:
    def __init__(self, user_name: str, user_money: int = 30000, user_fraction: str = None, user_rang: int = 0, user_spaceship: list = [], user_achievements: list = []):
        self.name = user_name
        self.money = user_money
        self.fraction = user_fraction
        self.rang = user_rang
        self.spaceships = user_spaceship
        self.achievements = user_achievements

    def IncrementMoney(self, amount: int):
        self.money += amount

    def DecrementMoney(self, amount: int):
        self.money -= amount

    def EarnAchivement(self, achievement):
        self.achievements.append(achievement)

    def BuyStarship(self, spaceship: Spaceship):
        if self.money < spaceship.price:
            print("Недостаточно средств")
        else:
            self.money -= spaceship.price
            self.spaceships.append(spaceship)


class Fraction:
    def __init__(self, fraction_name: str, fraction_capital: str, fraction_planets: list, fraction_language: str,
                 fraction_currency: str, fraction_population: int, fraction_established: int):
        self.name = fraction_name
        self.capital = fraction_capital
        self.planets = fraction_planets
        self.language = fraction_language
        self.currency = fraction_currency
        self.population = fraction_population
        self.established = fraction_established


# ------------------ 1.3 ------------------

sidewinder = Spaceship("Sidewinder", "Multipurpose", "Red-White", 10000)

lei = User(user_name="Lei", user_fraction="Independent")

marco = lei
marco.name = "Marco"

print("Class lei name: ", lei.name)
print("Class marco name: ", marco.name)

print(f"\nName:{lei.name}\nMoney:{lei.money}\nStarships:{lei.spaceships}\n")
lei.BuyStarship(sidewinder)
print(f"\nName:{lei.name}\nMoney:{lei.money}\nStarships:{lei.spaceships[0].name}\n")
for _ in range(50):
    lei.spaceships[0].Fly()

print(f"Fuel:{sidewinder.fuel}")
print(f"\nName:{lei.name}\nStarships:{lei.spaceships[0].name}\nFuel:{lei.spaceships[0].fuel}")

sidewinder.Refueling(150)

