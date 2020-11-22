import sys

from deck import Deck

def message(msg):
    sys.stderr.write(f"{msg}\n")
    sys.stderr.flush()
    
def main():
    message("Granny Poker")
    deck = Deck()
    comp, user = deck.deal(2, 4)
    print("comp")
    for card in comp:
        print(str(card), card._value)
    print("\nuser")
    for card in user: print(str(card), card._value)
    
if __name__ == "__main__": main()
