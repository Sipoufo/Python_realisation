from replit import clear
import art

print(art.logo)

def high_bidder(bidders):
    high = 0
    for bidder in bidders:
        bidder_price = bidders[bidder]
        if bidder_price > high:
            high = bidder_price
    print(f"The winner is James with a bid of {high} Fcfa")

start = True
bidders = {}
while start:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: Fcfa "))
    bidders[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'")
    if other == 'yes':
        clear()
    else:
        clear()
        high_bidder(bidders)
        start = False
        