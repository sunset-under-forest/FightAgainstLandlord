HEART = "HEART"
SPADE = "SPADE"
CLUB = "CLUB"
DIAMOND = "DIAMOND"
_COLORS = [HEART, SPADE, CLUB, DIAMOND]
_RED_STR = lambda x: "\033[5;31m%s\033[0m" % x
_CYAN_STR = lambda x: "\033[5;34m%s\033[0m" % x
_ICONS = {HEART: _RED_STR("♥"), SPADE: _CYAN_STR("♠"), CLUB: _CYAN_STR("♣"), DIAMOND: _RED_STR("♦"),
          "RED_JOKER": _RED_STR("■"), "BLACK_JOKER": _CYAN_STR("■")}

_VALUES = ['PASS', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','BLACK_JOKER','RED_JOKER']

_CARD_ICON = lambda a, b='',: """┌───┐
│""" + a + ' ' * (3 - len(a)) +"""│
│""" + b + """  │
└───┘"""
_JOKER = ["RED", "BLACK"]

COMPARE_TABLE = {'PASS': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11,
                  'A': 12, '2': 13, 'BLACK_JOKER': 14, 'RED_JOKER': 15}


class Card:
    def __init__(self, value, color):
        self.__value = None
        self.__color = None
        self.__isJoker = False
        self.initialize(value, color)

    def initialize(self, value, color):
        if type(value) == int: value = _VALUES[value]
        assert type(value) == str and type(color) == str, "input is in wrong type!"
        self.__value = value.upper().strip()
        self.__color = color.upper().strip()
        if self.__value in _VALUES and self.__color in _COLORS:
            return
        elif self.__value.endswith("JOKER") and self.__color in _JOKER:
            self.__isJoker = True
            self.__color = "ฏ"
            return
        raise TypeError(f"Card value is unacceptable!")

    def isJoker(self):
        return self.__isJoker

    def getValue(self):
        return COMPARE_TABLE[self.__value]

    def __str__(self):
        return _CARD_ICON(self.__color, _ICONS[self.__value]) if self.__isJoker else _CARD_ICON(self.__value,
                                                                                                _ICONS[self.__color])

    def __gt__(self, other):
        other: Card
        assert type(other) == Card
        return self.getValue() > other.getValue()

    def __lt__(self, other):
        other: Card
        assert type(other) == Card
        return self.getValue() < other.getValue()


# noinspection PyTypeChecker
CARD_POOL52 = [Card(i, j) for i in range(1, 14) for j in _COLORS]
# noinspection PyTypeChecker
HEART_A = CARD_POOL52[0]
SPADE_A = CARD_POOL52[1]
CLUB_A = CARD_POOL52[2]
DIAMOND_A = CARD_POOL52[3]
HEART_2 = CARD_POOL52[4]
SPADE_2 = CARD_POOL52[5]
CLUB_2 = CARD_POOL52[6]
DIAMOND_2 = CARD_POOL52[7]
HEART_3 = CARD_POOL52[8]
SPADE_3 = CARD_POOL52[9]
CLUB_3 = CARD_POOL52[10]
DIAMOND_3 = CARD_POOL52[11]
HEART_4 = CARD_POOL52[12]
SPADE_4 = CARD_POOL52[13]
CLUB_4 = CARD_POOL52[14]
DIAMOND_4 = CARD_POOL52[15]
HEART_5 = CARD_POOL52[16]
SPADE_5 = CARD_POOL52[17]
CLUB_5 = CARD_POOL52[18]
DIAMOND_5 = CARD_POOL52[19]
HEART_6 = CARD_POOL52[20]
SPADE_6 = CARD_POOL52[21]
CLUB_6 = CARD_POOL52[22]
DIAMOND_6 = CARD_POOL52[23]
HEART_7 = CARD_POOL52[24]
SPADE_7 = CARD_POOL52[25]
CLUB_7 = CARD_POOL52[26]
DIAMOND_7 = CARD_POOL52[27]
HEART_8 = CARD_POOL52[28]
SPADE_8 = CARD_POOL52[29]
CLUB_8 = CARD_POOL52[30]
DIAMOND_8 = CARD_POOL52[31]
HEART_9 = CARD_POOL52[32]
SPADE_9 = CARD_POOL52[33]
CLUB_9 = CARD_POOL52[34]
DIAMOND_9 = CARD_POOL52[35]
HEART_10 = CARD_POOL52[36]
SPADE_10 = CARD_POOL52[37]
CLUB_10 = CARD_POOL52[38]
DIAMOND_10 = CARD_POOL52[39]
HEART_J = CARD_POOL52[40]
SPADE_J = CARD_POOL52[41]
CLUB_J = CARD_POOL52[42]
DIAMOND_J = CARD_POOL52[43]
HEART_Q = CARD_POOL52[44]
SPADE_Q = CARD_POOL52[45]
CLUB_Q = CARD_POOL52[46]
DIAMOND_Q = CARD_POOL52[47]
HEART_K = CARD_POOL52[48]
SPADE_K = CARD_POOL52[49]
CLUB_K = CARD_POOL52[50]
DIAMOND_K = CARD_POOL52[51]
RED_JOKER = Card('RED_JOKER', "RED")
BLACK_JOKER = Card('BLACK_JOKER', "BLACK")

CARD_POOL54 = CARD_POOL52 + [RED_JOKER, BLACK_JOKER]

if __name__ == '__main__':
    # print(CLUB_K < BLACK_JOKER)
    # print(BLACK_JOKER)
    print(dict(zip(_VALUES,(tuple() for i in range(16)))))
