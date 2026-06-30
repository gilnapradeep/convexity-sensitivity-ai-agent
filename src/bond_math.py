import numpy as np

def bond_price(face, coupon_rate, ytm, years, freq=2):
    coupon = face * coupon_rate / freq
    periods = int(years * freq)
    rate = ytm / freq
    cashflows = np.full(periods, coupon)
    cashflows[-1] += face
    discount = [(1 + rate) ** i for i in range(1, periods + 1)]
    price = np.sum(cashflows / discount)
    return price


def macaulay_duration(face, coupon_rate, ytm, years, freq=2):
    coupon = face * coupon_rate / freq
    periods = int(years * freq)
    rate = ytm / freq
    price = bond_price(face, coupon_rate, ytm, years, freq)
    duration = 0
    for t in range(1, periods + 1):
        cashflow = coupon
        if t == periods:
            cashflow += face

        pv = cashflow / (1 + rate) ** t
        duration += (t / freq) * pv
    return duration / price


def modified_duration(face, coupon_rate, ytm, years, freq=2):
    mac = macaulay_duration(face, coupon_rate, ytm, years, freq)
    return mac / (1 + ytm / freq)

def convexity(face, coupon_rate, ytm, years, freq=2):
    coupon = face * coupon_rate / freq
    periods = int(years * freq)
    rate = ytm / freq
    price = bond_price(face, coupon_rate, ytm, years, freq)
    conv = 0
    for t in range(1, periods + 1):
        cashflow = coupon
        if t == periods:
            cashflow += face

        pv = cashflow / (1 + rate) ** t
        conv += t * (t + 1) * pv
    return conv / (price * (freq ** 2) * ((1 + rate) ** 2))


def dv01(face, coupon_rate, ytm, years, freq=2):
    md = modified_duration(face, coupon_rate, ytm, years, freq)
    price = bond_price(face, coupon_rate, ytm, years, freq)
    return md * price / 10000

if __name__ == "__main__":
    Price = bond_price(face=100, coupon_rate=0.0726, ytm=0.0735, years=9)
    print("Price:", round(Price,2))
    Macaulay_Duration = macaulay_duration(100, 0.0726, 0.0735, 9)
    print("Macaulay Duration:", round(Macaulay_Duration,2))
    Modified_Duration = modified_duration(100, 0.0726, 0.0735, 9)
    print("Modified Duration:", round(Modified_Duration,2))
    Convexity = convexity(100, 0.0726, 0.0735, 9)
    print("Convexity:", round(Convexity,2))
    DV01 = dv01(100, 0.0726, 0.0735, 9)
    print("DV01:", round(DV01,4))