

class Карти:
    def __init__(self, ранг, масть):
        self.ранг = ранг
        self.масть = масть

    def __str__(self):
        return f"{self.ранг} {self.масть}"
class Руки:
    def __init__(self):
        self.карти = []

    def додати_карту(self, карта):
        self.карти.append(карта)

    def обчислити_значення(self):
        значення = 0
        тузів = 0
        for карта in self.карти:
            if карта.ранг in ['Валет', 'Дама', 'Король']:
                значення += 10
            elif карта.ранг == 'Туз':
                значення += 11
                тузів += 1
            else:
                значення += int(карта.ранг)
        while значення > 21 and тузів:
            значення -= 10
            тузів -= 1
        return значення

    def __str__(self):
        return ', '.join(str(карта) for карта in self.карти)
