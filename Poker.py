"""
information: 牌堆
creating time: 2023/1/30
"""
from card import *
from random import  shuffle
from Rules import *

def cardHeapIcons(cards: list[Card]):
    x = [str(i).split('\n') for i in cards]
    y = []
    for j in range(3):
        temp = ''
        for i in x:
            temp += i[j]
        y.append(temp + '\n')
    y.append(''.join(i[3] for i in x))

    return "".join(y)


class CardHeap:
    def __init__(self, *cards, num=17):
        if len(cards) == 0 :self.cardHeap = []
        if type(cards[0]) == PlayCombo: cards = cards[0].getHeap()
        # print(cards)
        self.cardHeap = list(cards)
        self.cardHeap.sort(key=lambda x: x.getValue())
        self.cardCalc = [list() for _ in range(16)]
        self.init_calculator()

    def init_calculator(self):
        for i in self.cardHeap:
            self.cardCalc[i.getValue()].append(i)

    def __str__(self):
        return cardHeapIcons(self.cardHeap)

    def play_card(self, pcards:list[str]):
        q = len(pcards)
        if q ==0 or pcards[0]=='': return CardHeap(PlayCombo())
        tempCalc = self.cardCalc[:]
        tempHeap = self.cardHeap[:]
        combo = []
        for i in pcards:
            if len(tempCalc[COMPARE_TABLE[i]]) == 0:raise Exception("没有足够的手牌！")
            c = tempCalc[COMPARE_TABLE[i]].pop()
            combo.append(c)
            tempHeap.remove(c)
        res = PlayCombo(*combo)
        self.cardCalc = tempCalc
        self.cardHeap = tempHeap
        return CardHeap(res)



shuffle(CARD_POOL54)
LANDLORDS_CARDS = CardHeap(*CARD_POOL54[:3], num=3)
PLAYER1_CARDS = CardHeap(*CARD_POOL54[3:20])
PLAYER2_CARDS = CardHeap(*CARD_POOL54[20:37])
PLAYER3_CARDS = CardHeap(*CARD_POOL54[37:])

if __name__ == '__main__':
    test = PLAYER1_CARDS
    print(test)
    print(test.cardCalc)
    waitForPlay = input("请输入要出的牌（以空格分离）：")
    print(test.play_card(waitForPlay.strip().split(" ")))
    print(test)
    # print(PLAYER1_CARDS)
    # print(PLAYER2_CARDS)
    # print(PLAYER3_CARDS)
