from art import logo
def highest_bid(Auction_entries):
    highest = 0
    for name in Auction_entries:
        if(highest < Auction_entries[name]):
            highest = Auction_entries[name]
            highest_bidder = name
    print(f"The winner is {highest_bidder} with a bid of ${highest}")

print(logo)
Auction = {}
Add_new_bidder = 'yes'
while Add_new_bidder == 'yes':
    key = input ("What is your name?: ")
    value = int(input("What's your bid?: $"))
    Auction[key] = value
    Add_new_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    print("\n"*100)

highest_bid(Auction)