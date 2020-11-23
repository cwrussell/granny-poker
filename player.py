
class GrannyPokerPlayer:

    def __init__(self, hand, comp=False):
        self._hand = hand
        self._comp = comp
        
    def peek(self):
        opts = [1, 2, 3, 4]
        for i in range(2):
            while True:
                sopt = ",".join([str(x) for x in opts])
                opt = input(f"Pick card to see. Enter {sopt}: ")
                iopt = int(opt.strip())
                if iopt not in opts:
                    print("Invalid value.", flush=True)
                else:
                    print(f"-> {str(self._hand[iopt-1])}", flush=True)
                    opts = [x for x in opts if x != iopt]
                    break
                    
    def swap(self, idx, card):
        self._hand[idx] = card
        
    def get_card(self, idx):
        return self._hand[idx]

    def sum(self):
        score = 0
        for card in self._hand:
            score += card.value()
        return score
