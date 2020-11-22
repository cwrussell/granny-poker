class CardError(Exception): pass

class Card:

    def __init__(self, suit, face, value):
        self._suit = self._validate_suit(suit)
        self._face = self._validate_face(face)
        self._value = self._set_value(value)

    def _validate_face(self, face):
        face = str(face).upper()
        valid_faces = [str(x) for x in range(2, 11)] + ["K", "Q", "J", "A"] 
        if face not in valid_faces:
            raise CardError(f"Invalid face: {face}")
        return face

    def _validate_suit(self, suit):
        if suit not in {"Clubs", "Spades", "Diamonds", "Hearts"}:
            raise CardError(f"Invalid suit: {suit}")
        return suit

    def _set_value(self, value):
        if type(value) != int:
            raise CardError("Card value must be int")
        return value
        
    def __str__(self):
        return f"{self._face} of {self._suit}"
