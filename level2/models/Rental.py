from datetime import datetime


class Rental:
    DATE_FORMAT = '%Y-%m-%d'
    PRICING_RULES = [(10, 0.5), (4, 0.7), (1, 0.9), (0, 1)]

    def __init__(self, _id, car_id, distance, start_date, end_date):
        self.id = _id
        self.car_id = car_id
        self.distance = distance
        self.start_date = start_date
        self.end_date = end_date
        self.duration = self.calculate_duration(start_date, end_date)

    def calculate_duration(self, start_date, end_date):
        duration = datetime.strptime(end_date, self.DATE_FORMAT) - datetime.strptime(start_date, self.DATE_FORMAT)
        return duration.days + 1

    def calculate_price(self, price_per_day, price_per_km):
        price = self.distance * price_per_km
        duration = self.duration

        while duration > 0:
            for i in self.PRICING_RULES:
                if duration > i[0]:
                    price += price_per_day * i[1]
                    duration -= 1
                    break

        return int(price)
