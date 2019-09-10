from datetime import datetime


class Rental:
    DATE_FORMAT = '%Y-%m-%d'

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
        return self.duration * price_per_day + self.distance * price_per_km
