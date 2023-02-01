"""
information: 出牌规则
creating time: 2023/1/30
"""
from card import *
"""
牌型
火箭：即双王（大王和小王），最大的牌。
炸弹：四张同数值牌（如四个 7 ）。
单牌：单个牌（如红桃 5 ）。
对牌：数值相同的两张牌（如梅花 4+ 方块 4 ）。
三张牌：数值相同的三张牌（如三个 J ）。
三带一：数值相同的三张牌 + 一张单牌或一对牌。例如： 333+6 或 444+99
单顺：五张或更多的连续单牌（如： 45678 或 78910JQK ）。不包括 2 点和双王。
双顺：三对或更多的连续对牌（如： 334455、 7788991010JJ ）。不包括 2 点和双王。
三顺：二个或更多的连续三张牌（如： 333444、 555666777888 ）。不包括 2 点和双王。
飞机带翅膀：三顺+同数量的单牌（或同数量的对牌）。

补充：
四带二：数值相同的四张牌 + 两张单牌或两对牌。例如： 3333+67 或 4444+99JJ
"""


class PlayCombo:
    def __init__(self, *args):
        """
        information: 出牌组合
        creating time: 2023/1/30
        """
        self.__cardHeap = list(args)
        self.cardList = [i.getValue() for i in args]
        self.cardList.sort()
        self.combo: int = self.check()

    def raiseException(self):
        raise Exception("错误的出牌组合")

    def check(self):
        l = self.cardList
        l: list[int]
        if len(l) == 0: return 0  # "PASS"
        if len(l) == 1: return 3  # "SINGLE"
        if len(l) == 2:
            if l[0] == l[1]: return 4  # "PAIR"
            if sum(l) == 29: return 1  # "ROCKET"
        if len(l) == 3 and l[0] == l[1] == l[2]: return 5  # "TRIPLET"
        if len(l) == 4:
            if l[0] == l[1] == l[2] == l[3]: return 2  # "BOMB"
            if l[1] == l[2] == l[3] or l[0] == l[1] == l[2]: return 6  # "TRIPLET_WITH_SINGLE"
        if len(l) == 5:
            for i in range(0, 4, 2):
                if l[i] == l[i + 1] == l[i + 2] and l[(i + 3) % 5] == l[(i + 3) % 5]: return 7  # "TRIPLET_WITH_PAIR"
            tmp = l[0]
            for i in range(5):
                if tmp + i != l[i]:
                    self.raiseException()
            return 8  # "SEQUENCE"
        if len(l) == 6:
            for i in range(3):
                if l[i] == l[i + 1] == l[i + 2] == l[i + 3]: return 13  # "QUADRUPLE_WITH_TWO_SINGLES"
        if len(l) == 8:
            for i in range(0, 6, 2):
                if l[i] == l[i + 1] == l[i + 2] == l[i + 3] and l[(i + 4) % 8] == l[(i + 5) % 8] and l[(i + 6) % 8] == \
                        l[(i + 7) % 8]: return 14  # "QUADRUPLE_WITH_TWO_PAIRS"
        flag = True

        length = len(self.cardList)
        _combo = [0] * 16
        for i in l:
            _combo[i] += 1
        tmp = l[0]
        if length >= 5:
            for i in range(length):
                if tmp + i != l[i]:
                    flag = False
                    break
            if flag: return 8  # "SEQUENCE"
            if length % 2 == 0:
                flag = True
                for i in range(0, length, 2):
                    if l[i] != l[i + 1]:
                        flag = False
                        break
                if flag: return 9  # "SEQUENCE_OF_PAIR"
            if length % 3 == 0:
                flag = True
                for i in range(0, length, 3):
                    if l[i] == l[i + 1] == l[i + 2]:
                        continue
                    else:
                        flag = False
                        break
                if flag: return 10  # "SEQUENCE_OF_TRIPLETS"
            total = sum(_combo)

            if length % 4 == 0:
                pos = 0
                for i in range(16):
                    if _combo[i] >= 3:
                        pos = i
                        break
                w = 0
                while _combo[pos + w] >= 3:
                    w += 1
                    total -= 3
                if w >= 2 and total == w: return 11  # "SEQUENCE_OF_TRIPLETS_WITH_TWO_SINGLES"
            elif length % 5 == 0:
                pos = 0
                for i in range(16):
                    if _combo[i] == 3:
                        pos = i
                        break
                t = 0
                pair = 0
                while _combo[pos + t] == 3:
                    t += 1
                    total -= 3
                for i in range(16):
                    if _combo[i] == 2:
                        pair += 1
                    elif _combo[i] == 4:
                        pair += 2
                if t >= 2 and pair == t: return 12  # "SEQUENCE_OF_TRIPLETS_WITH_TWO_PAIRS"

        self.raiseException()

    def getHeap(self):
        return self.__cardHeap


COMBOLIST = ["PASS", "ROCKET", "BOMB", "SINGLE", "PAIR", "TRIPLET", "TRIPLET_WITH_SINGLE", "TRIPLET_WITH_PAIR",
             "SEQUENCE",
             "SEQUENCE_OF_PAIR", "SEQUENCE_OF_TRIPLETS", "SEQUENCE_OF_TRIPLETS_WITH_TWO_SINGLES",
             "SEQUENCE_OF_TRIPLETS_WITH_TWO_PAIRS", "QUADRUPLE_WITH_TWO_SINGLES",
             "QUADRUPLE_WITH_TWO_PAIRS"]

COMBOTYPE = {0: 'PASS', 1: 'ROCKET', 2: 'BOMB', 3: 'SINGLE', 4: 'PAIR', 5: 'TRIPLET', 6: 'TRIPLET_WITH_SINGLE',
             7: 'TRIPLET_WITH_PAIR', 8: 'SEQUENCE', 9: 'SEQUENCE_OF_PAIR', 10: 'SEQUENCE_OF_TRIPLETS',
             11: 'SEQUENCE_OF_TRIPLETS_WITH_TWO_SINGLES', 12: 'SEQUENCE_OF_TRIPLETS_WITH_TWO_PAIRS',
             13: 'QUADRUPLE_WITH_TWO_SINGLES', 14: 'QUADRUPLE_WITH_TWO_PAIRS'}

if __name__ == '__main__':
    print(dict(zip(range(len(COMBOLIST)), COMBOLIST)))

    # test

    # # PASS
    # p1 = PlayCombo()
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # SINGLE
    # p1 = PlayCombo(CLUB_A)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # PAIR
    # p1 = PlayCombo(SPADE_A,CLUB_A)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # TRIPLET
    # p1 = PlayCombo(DIAMOND_A, SPADE_A, CLUB_A)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # TRIPLET_WITH_SINGLE
    # p1 = PlayCombo(DIAMOND_A, SPADE_A, CLUB_A,RED_JOKER)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # TRIPLET_WITH_PAIR
    # p1 = PlayCombo( HEART_2, SPADE_2, DIAMOND_A, SPADE_A, CLUB_A)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # SEQUENCE
    # p1 = PlayCombo(HEART_3,HEART_4,HEART_5,HEART_6,HEART_7,HEART_8)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # SEQUENCE_OF_PAIR
    # p1 = PlayCombo(HEART_3, CLUB_3, HEART_4, CLUB_4,HEART_5, CLUB_5)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # SEQUENCE_OF_TRIPLETS
    # p1 = PlayCombo(HEART_3, CLUB_3, DIAMOND_3,HEART_4, CLUB_4, DIAMOND_4,HEART_5, CLUB_5,DIAMOND_5)
    # print(p1.cardList)
    # print(p1.combo)
    #
    #
    # # SEQUENCE_OF_TRIPLETS_WITH_TWO_SINGLES
    # p1 = PlayCombo(HEART_3, CLUB_3, DIAMOND_3, HEART_4, CLUB_4, DIAMOND_4, HEART_5, CLUB_5)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # SEQUENCE_OF_TRIPLETS_WITH_TWO_SINGLES
    # p1 = PlayCombo(HEART_3, CLUB_3, DIAMOND_3, HEART_4, CLUB_4, DIAMOND_4, HEART_5, CLUB_5, DIAMOND_5, SPADE_5)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # BOMB
    # p1 = PlayCombo( HEART_A, DIAMOND_A, SPADE_A,CLUB_A)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # ROCKET
    # p1 = PlayCombo(RED_JOKER,BLACK_JOKER)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # QUADRUPLE_WITH_TWO_PAIRS
    # p1 = PlayCombo(HEART_3,SPADE_3,HEART_2,SPADE_2, HEART_A, DIAMOND_A, SPADE_A,CLUB_A)
    # print(p1.cardList)
    # print(p1.combo)
    #
    # # QUADRUPLE_WITH_TWO_SINGLES
    # p1 = PlayCombo(SPADE_3,HEART_2, HEART_A, DIAMOND_A, SPADE_A,CLUB_A)
    # print(p1.cardList)
    # print(p1.combo)
    #

    ...
