class Progress:
    def __init__(self, progression, count, date):
        self.progression = progression
        self.count = count
        self.date = date

    def __str__(self):
        return "Progress: " + self.progression + " " + str(self.count) + " at " + self.date