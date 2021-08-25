import numpy as np


class Annuity:
    def __init__(self, annuity, rate, year, period=12):
        self.annuity = annuity
        self.rate = rate / 100
        self.year = year
        self.period = period

    def get_fv(self):
        pass

    def get_pv_ordinary_annuity(self):
        item_1_numerator = 1 - (1 / np.power((1 + (self.rate / self.period)), self.period *
                                             self.year))
        item_1_denominator = self.rate / self.period
        item_1 = item_1_numerator / item_1_denominator
        PV_OA = self.annuity * item_1
        return PV_OA

    def get_pv_annuity_due(self):
        PV_OA = self.get_pv_ordinary_annuity()
        item_2 = 1 + self.rate / self.period

        PV_AD = PV_OA * item_2
        return PV_AD
