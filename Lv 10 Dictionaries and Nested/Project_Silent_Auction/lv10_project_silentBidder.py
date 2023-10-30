import art_silent_auction
import os

#HINT: You can call clear() to clear the output in the console.

bidsDictionary = {}

print(art_silent_auction.logo)
finished = False

def max_Bid(bidsDictionary):
  maxBid = 0
  highestBidder = ""
  for bidder in bidsDictionary:
    bidAmount = bidsDictionary[bidder]
    if (bidAmount > maxBid):
      maxBid = bidAmount
      highestBidder = bidder
  print("########################################\n")
  print(f"{highestBidder} Gratulation, Sie sind mit {maxBid} € der Höchstbietende")
  print("\n########################################")
  
        
while not finished:
  print("Willkommen ins unserem Hause.")
  name = input("Wie lautet ihr Name Sir?\n")
  bidPrice = int(input("Nennen Sie uns bitte ihr Gebot?\n€"))
  bidsDictionary[name] = bidPrice
  shouldContinue = input("Gibt es weitere Personen, die gedenken ein Gebot in unserem Hause abzugeben? Schreiben Sie Ja oder Nein\n")
  shouldContinue.lower()
  if shouldContinue == "nein":
    finished = True
    max_Bid(bidsDictionary)
  elif shouldContinue == "ja":
    os.system('cls')