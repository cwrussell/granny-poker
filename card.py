class CardError(Exceptions): pass

class Card:

    def __init__(self, suit, face, value=None):
        self._suit = self._validate_suit(suit)
        self._face = self._validate_face(face)
        self._value = self._set_value(value)

    def _validate_face(self, face):
        face = str(face).upper()
        valid_faces = list(range(2, 11)) + ["K", "Q", "J", "A"] 
        if face not in valid_faces:
            raise CardError(f"Invalid face: {face}")
        return face

    def _validate_suit(self, suit):
        suit = str(suit).lower()
        if suit not in {"clubs", "spades", "diamonds", "hearts"}:
            raise CardError(f"Invalid suit: {suit}")
        return suit

    def _set_value(self, value):
        if value is None:
            faces = ["A"] + list(range(2, 11)) + ["J", "Q", "K"]
            def_values = {face: i + 1 for i, face in enumerate(faces)}
            return def_values[self._face]
        if type(value) != int:
            raise CardError("Card value must be int")
        return value
