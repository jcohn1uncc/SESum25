class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("how many quarters?: ")) * 0.25
        dimes = int(input("how many dimes?: ")) * 0.10
        nickels = int(input("how many nickels?: ")) * 0.05
        pennies = int(input("how many pennies?: ")) * 0.01
        return round(quarters + dimes + nickels + pennies, 2)

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            print("Payment successful.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
