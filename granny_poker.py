import random
import sys
import time

from deck import Deck
from player import GrannyPokerPlayer

def div():
    print(f"{'-'*80}", flush=True)
    

def play(computer, human, deck):
    print("You go first", flush=True)
    waste = Deck(values={"K": 0}, waste=True)
    waste.to_left(deck.next_card())
    
    comp_known = [0, 1]
    
    # This loop continues until the game is done
    while True:
    
        div()
        time.sleep(1)
    
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
                
        # Computer's turn
        # If know that have less than 10 points, end the game
        div()
        time.sleep(1)
        comp_score = computer.sum()
        if (len(comp_known) == 4) and (comp_score <= 10):
            print("Computer is knocking")
            return computer, human
            
        # Take top card from waste pile if <= 4
        top = waste.top_value()
        if top <= 4:
            active_card = waste.next_card()
            msg = f"Computer took {str(active_card)} from waste pile"
            
        # Otherwise take top card from deck
        else:
            active_card = deck.next_card()
            msg = f"Computer took {str(active_card)} from top of deck"
            
        # Discard if card value is greater than 4
        if active_card.value() > 4:
            msg += f"\nComputer discarded {str(active_card)}"
            waste.to_left(active_card)
            print(msg, flush=True)
            continue
            
        # Replace any known cards if their value is greater than 4
        card_values = {idx: computer.get_card(idx).value() for idx in comp_known}
        possible_replacements = {idx: val for idx, val in card_values.items() if val > 4}
        if possible_replacements:
            diffs = {idx: val - active_card.value() for idx, val in possible_replacements.items()}
            best = max(list(diffs.values()))
            for idx, val in diffs.items():
                if val == best:
                    discard = computer.get_card(comp_known[idx])
                    computer.swap(comp_known[idx], active_card)
                    msg += f"\nComputer replaced {str(discard)} with {str(active_card)}"
                    waste.to_left(discard)
                    
        # If no known cards have a value greater than 4
        else:
            
            # Replace an unknown card if there are unknown cards
            if len(comp_known) < 4:
                idx = 2 if 2 not in comp_known else 3
                discard = computer.get_card(idx)
                computer.swap(idx, active_card)
                msg += f"\nComputer replaced {str(discard)} with {str(active_card)}"
                waste.to_left(discard)
                comp_known.append(idx)
                
            # If all cards are known, pick the one with the greatest difference
            else:
                diffs = [computer.get_card(x).value() - active_card.value() for x in range(3)]
                best = max(diffs)
                if best > 0:
                    for i, diff in enumerate(diffs):
                        if diff == best:
                            discard = computer.get_card(i)
                            computer.swap(i, active_card)
                            msg += f"\nComputer replaced {str(discard)} with {str(active_card)}"
                            waste.to_left(discard)
                            
                # If all of the known cards have a lower or equal value than the active card, just discard
                else:
                    msg += f"\nComputer discarded {str(active_cards)}"
                    waste.to_left(active_card)
        print(msg, flush=True)


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
