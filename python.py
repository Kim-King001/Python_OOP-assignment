
# Question 1
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # Battery life in hours

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def charge(self):
        return f"Charging {self.brand} {self.model}... Battery life is now full."

class SmartWatch(Smartphone):
    def __init__(self, brand, model, battery_life, strap_color):
        super().__init__(brand, model, battery_life)
        self.strap_color = strap_color

    def make_call(self, number):
        return f"Making a call to {number} from the wrist with {self.brand} {self.model} watch."

    def show_time(self):
        return "Showing current time on the smartwatch display."
    
phone = Smartphone('Google', 'Pixel 7', 24)
watch = SmartWatch('Samsung', 'Galaxy Watch5', 40, 'Silver')

print(phone.make_call('555-1234'))  # Calls 555-1234 from Google Pixel 7...
print(watch.make_call('555-1234'))  # calls to 555-1234 from the wrist with Samsung Galaxy Watch5 watch.
print(watch.show_time())            # Showscurrent time on the smartwatch display.

#Question2
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Dog:
    def move(self):
        print("Running 🐕")

class Fish:
    def move(self):
        print("Swimming 🐟")

# Demonstrating the move method for each class
car = Car()
plane = Plane()
dog = Dog()
fish = Fish()

car.move()    # Output: Driving 🚗
plane.move()  # Output: Flying ✈️
dog.move()    # Output: Running 🐕
fish.move()   # Output: Swimming 🐟

