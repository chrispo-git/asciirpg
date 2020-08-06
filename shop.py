import random

stock = 0


def shop(gold):
    global stock
    g = gold
    print(f"""
1.Stock up      {stock} in stock
2.Open up shop
""")
    shopinput = input("")
    if shopinput == "1":
        print("100 gold per stock")
        amount = input("quantity:")
        try:
            amount = int(amount)
        except ValueError:
            amount = 1
        if g > 100 * amount:
            stock += amount
            g -= 100 * amount
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
