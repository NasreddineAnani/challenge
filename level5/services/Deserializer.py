from models.Rental import Rental
from models.Car import Car


def get_data_information(data):
    cars = {}
    for car in data['cars']:
        cars[car['id']] = Car(car['id'], car['price_per_day'], car['price_per_km'])

    options = {}
    for option in data['options']:
        if option['rental_id'] in options:
            options[option['rental_id']].add(option['type'])
        else:
            options[option['rental_id']] = {option['type']}

    rentals = []
    for rental in data['rentals']:
        rentals.append(
            Rental(rental['id'], rental['car_id'], rental['distance'], rental['start_date'], rental['end_date'],
                   options.get(rental['id'], set())))

    return cars, options, rentals
