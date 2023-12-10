import math

class WaterTank:
    def __init__(self, height, radius, water=0):
        self.height = height
        self.radius = radius
        self.water = water

    def get_tank_capacity(self):
        return math.pi * self.radius**2 * self.height

    def add_water(self, user_input):
        if user_input < 0:
            return "Water amount cannot be negative"
        if user_input > self.get_tank_capacity():
            return "Overflow! Cannot add more water than the tank capacity"
        
        self.water = user_input
        return f"Water added. Current water amount: {self.water}"

    def get_water_height(self):
        return self.water / (math.pi * self.radius**2)

if __name__ == "__main__":
    watertank = WaterTank(14, 2, 56)

    print(f"Tank Capacity: {watertank.get_tank_capacity()} m³")
    
    user_input = float(input("Enter the amount of water to add: "))
    print(watertank.add_water(user_input))
    
    print(f"Current Water Height: {watertank.get_water_height()} meters")
