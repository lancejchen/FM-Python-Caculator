from src.Annuity import Annuity

if __name__ == "__main__":
    annuity_cal_0 = Annuity(2400, 2.3, 15, 12)
    annuity_cal_1 = Annuity(2400, 2.5, 20, 12)
    annuity_cal_2 = Annuity(2400, 3.0, 30, 12)
    print(f'15 year total is {annuity_cal_0.get_pv()}, 20 year total is {annuity_cal_1.get_pv()}, and 30 years is {annuity_cal_2.get_pv()}')
