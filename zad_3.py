class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Property: Area: {self.area} sqm, Rooms: {self.rooms}, "
            f"Price: ${self.price}, Address: {self.address}"
        )


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"House: Area: {self.area} sqm, Rooms: {self.rooms}, "
            f"Price: ${self.price}, Address: {self.address}, "
            f"Plot Area: {self.plot} sqm"
        )


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Flat: Area: {self.area} sqm, Rooms: {self.rooms}, "
            f"Price: ${self.price}, Address: {self.address}, "
            f"Floor: {self.floor}"
        )


house1 = House(120, 4, 250000, "123 Main St", 500)

flat1 = Flat(80, 3, 150000, "456 Elm St", 2)

print(house1)
print(flat1)
