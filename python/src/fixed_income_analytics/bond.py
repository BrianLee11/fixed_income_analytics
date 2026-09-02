import datetime

class Bond:
    def __init__(self, 
                 face_value: float, 
                 coupon_rate: float, 
                 maturity: datetime.date,
                 payment_frequency: int # 1 = annual, 2 = semiannual, 4 = quarterly, 12 = monthly
                 ):
        self.face_value: float = face_value
        self.coupon_rate: float = coupon_rate
        self.maturity: datetime.date = maturity
        self.payment_frequency: int = 2
        