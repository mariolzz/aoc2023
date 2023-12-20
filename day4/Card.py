class Card:
    id: int
    winning_numbers: []
    numbers: []
    points: int
    copy_num: int

    def __init__(self):
        self.winning_numbers = []
        self.numbers = []
        self.points = 0
        self.copy_num = 0

    def fromLine(self, line: str):
        prepLine = line.split("|")
        prepCardNum = prepLine[0].split(":")[0].replace("Card", "").replace(" ", "").strip()
        prepWinning = prepLine[0].split(":")[1].split(" ")
        prepNumbers = prepLine[1].split(" ")
        self.id = int(prepCardNum)
        for pw in prepWinning:
            pw = pw.strip()
            if pw != "":
                self.winning_numbers.append(pw)
        for pn in prepNumbers:
            pn = pn.strip()
            if pn != "":
                self.numbers.append(pn)

    def calc_points_and_copies(self):
        for wn in self.winning_numbers:
            if wn in self.numbers:
                self.add_points()
                self.add_copies()

    def add_points(self):
        if self.points == 0:
            self.points = 1
        else:
            self.points *= 2

    def add_copies(self):
        self.copy_num += 1

    def __str__(self):
        return str(self.winning_numbers) + str(self.numbers)
