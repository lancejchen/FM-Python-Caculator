import numpy as np


class Annuity:
    def __init__(self, annuity, rate, year, period=12):
        self.annuity = annuity
        self.rate = rate / 100
        self.year = year
        self.period = period

    def get_fv(self):
        pass

    def get_pv(self):
        item_1_numerator = 1 - (1 / np.power((1 + (self.rate / self.period)), self.period *
                                             self.year))
        item_1_denominator = self.rate / self.period
        item_1 = item_1_numerator / item_1_denominator
        item_2 = 1 + self.rate / self.period

        PV = self.annuity * item_1 * item_2
        return PV
