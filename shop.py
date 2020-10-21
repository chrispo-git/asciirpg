import random

stock = 0


def shop(gold,c_id):
    stock_multiplier = 1
    if c_id == 8:
        stock_multiplier = 0.5
    global stock
    g = gold
    print(f"""
1.Stock up      {stock} in stock
2.Open up shop
""")
    shopinput = input("")
    if shopinput == "1":
        print(f"{int(100 * stock_multiplier)} gold per stock")
        amount = input("quantity:")
        try:
            amount = int(amount)
        except ValueError:
            amount = 1
        if g > 100 * amount * stock_multiplier:
            stock += amount
            g -= int(100 * amount * stock_multiplier)
        else:
            input("Not enough gold")
    if shopinput == "2":
        if stock > 0:
            sold = random.randint(0,stock)
            if sold > stock * 0.8:
                input(f"It was a busy day, you sold {sold} stocks")
            elif sold < stock * 0.2:
                input(f"Not many people came, so you sold {sold} stocks")
            else:
                input(f"You sold {sold} stocks")
            stock -= sold
            g += sold * 200
            input(f"Earnt {sold * 200} gold")
        else:
            input("You're out of stock")
    return g
