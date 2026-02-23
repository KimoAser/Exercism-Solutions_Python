import re
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        self.card_num = self.card_num.replace(' ', '')
        if len(self.card_num)<=1:
            return False
        if re.search(r'[^\d ]',self.card_num):
            return False
        opposite = self.card_num[::-1]
        listed = []
        for index,char in enumerate(opposite):
            integer = int(char)
            if index % 2 == 1:
                integer *= 2
                if integer > 9:
                    integer -= 9
                    listed.append(integer)
                else:
                    listed.append(integer)
            else:
                listed.append(integer)
        normal = listed[::-1]
        total = sum(normal)
        if total % 10 == 0:
            return True
        return False