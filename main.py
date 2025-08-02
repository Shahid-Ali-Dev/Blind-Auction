# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
dictionary = {}
def bidding():
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    person = input("Are there any other biders? Type 'yes' or 'no'.\n ").lower()
    dictionary.update({name : bid})
    if person == "yes":
        print("\n"*100)
        bidding()
    else:
        bidding_amount = 0
        winner = ""
        for key in dictionary:
            value = dictionary[key]
            if bidding_amount < value:
                bidding_amount = value
                winner = key
        print(f"The winner is {winner} with ${bidding_amount} bid.")
bidding()

