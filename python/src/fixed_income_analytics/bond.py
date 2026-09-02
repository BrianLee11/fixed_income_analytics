import datetime
""" TODO: create a bond class consisted of
1. face value (e.g. $100)
2. coupon rate (e.g. 4%)
3. maturity date (e.g. 2036-09-02)
4. payment frequency (e.g. annual, semiannual, quarterly, monthly)
"""

class Bond:
    def __init__(self, 
                 face_value: float, 
                 coupon_rate: float, 
                 maturity: datetime.date,
                 payment_frequency: int = 2 # 1 = annual, 2 = semiannual, 4 = quarterly, 12 = monthly
                 ):
        self.face_value: float = face_value
        self.coupon_rate: float = coupon_rate
        self.maturity: datetime.date = maturity
        self.payment_frequency: int = payment_frequency

""" TODO: show an example of initializing a bond
bond1 = Bond(100, 0.04, datetime.date(2036-09-02), 2)
print(bond1.face_value)  # 100
print(bond1.coupon_rate) # 0.04
print(bond1.maturity)    # 2036-09-02
print(bond1.payment_frequency)  # 2
"""
        