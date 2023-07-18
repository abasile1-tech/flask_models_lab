from .order import Order

john_pizza_order = Order(0, "John", "27 Feb 2020", 2, "Pizza", "The customer wants the pepperoni pizzas to be gluten-free and lactose-free")
john_drink_order = Order(1, "John", "27 Feb 2020", 2, "Drink", "The customer wants one Dr. Pepper and one Root Beer.")
sally_calzone_order = Order(2, "Sally", "31 Dec 2023", 4, "Calzone", "The customer is allergic to pine nuts, so the pesto needs to be made fresh (without pine nuts)")

orders = [john_pizza_order, john_drink_order, sally_calzone_order]