from .order import Order

john_pizza_order = Order(0, "John", "27 Feb 2020", 2, "Pizza")
john_drink_order = Order(1, "John", "27 Feb 2020", 2, "Drink")
sally_calzone_order = Order(2, "Sally", "31 Dec 2023", 4, "Calzone")

orders = [john_pizza_order, john_drink_order, sally_calzone_order]