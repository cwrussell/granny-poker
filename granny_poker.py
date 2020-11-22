import random
import sys

from deck import Deck
from player import GrannyPokerPlayer

def div():
    print(f"{'-'*80}", flush=True)
    

def play(computer, human, deck):
    print("You go first", flush=True)
    waste = Deck(values={"K": 0}, waste=True)
    waste.to_left(deck.next_card())
    
    # This loop continues until the game is done
    while True:
    
        div()
    
        # Pick card
        choice_str = f"To take card from waste pile ({waste.top()}), type 'w'"
        choice_str += "\nTo take top card from draw pile, type 'd'"
        choice_str += "\nTo knock and end the game, type 'e': "
        choice = input(choice_str).strip().strip("'").lower()
        if choice == "w":
            active_card = waste.next_card()
        elif choice == "d":
            active_card = deck.next_card()
        elif choice == "e":
            return computer, human
        else:
            print("Invalid choice.\n", flush=True)
            continue
        print(f"\nYou picked up -> {str(active_card)}")
        
        # Take action
        while True:
            choice_str = "To replace with one of your cards, input the card's number (1-4)."
            choice_str += "\nTo discard the card to the waste pile, type 'w': "
            choice = input(choice_str).strip().strip("'").lower()
            if choice == "w":
                waste.to_left(active_card)
                print(f"{str(active_card)} discarded", flush=True)
                break
            elif choice in ["1", "2", "3", "4"]:
                hand_idx = int(choice) - 1
                discard = human.get_card(hand_idx)
                waste.to_left(discard)
                human.swap(hand_idx, active_card)
                print(f"Card #{choice}, the {str(discard)}, was discarded and replaced with {str(active_card)}", flush=True)
                break
            else:
                print("Invalid choice.", flush=True)
                continue


def main():
    try:
        print("Granny Poker", flush=True)
        
        # Deal cards, peek at 2 cards
        deck = Deck(values={"K": 0})
        hands = deck.deal(2, 4)
        computer = GrannyPokerPlayer(hands[0], comp=True)
        human = GrannyPokerPlayer(hands[1])
        human.peek()
        
        # Start game
        computer, human = play(computer, human, deck)
        div()
        msg = "Your hand:\n"
        for i in range(4): msg += f"- {human.get_card(i)}\n"
        human_score = human.sum()
        msg += f"score: {human_score}\n\n"
        msg += "The computer:\n"
        for i in range(4): msg += f"- {computer.get_card(i)}\n"
        computer_score = computer.sum()
        msg += f"score: {computer_score}\n\n"
        print(msg, flush=True)
        
        if human_score < computer_score:
            print("Congratulations! You won!", flush=True)
        elif human_score == computer_score:
            print("So close, you tied!", flush=True)
        else:
            print("Shame! You lost!", flush=True)
        
        
        
    except KeyboardInterrupt:
        print("\n\nOh, you got scared, huh?\n\n", flush=True)
        pass
        
if __name__ == "__main__": main()
