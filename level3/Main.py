import json
from collections import OrderedDict
from models.Car import Car
from models.Rental import Rental
from models.Commission import calculate_commissions

with open('data/input.json') as json_file:
    data = json.load(json_file)
    cars = {}
    rentals = []
    for car in data['cars']:
        cars[car['id']] = Car(car['id'], car['price_per_day'], car['price_per_km'])
    for rental in data['rentals']:
        rentals.append(Rental(rental['id'], rental['car_id'], rental['distance'], rental['start_date'], rental['end_date']))

rentals_data = []
for rental in rentals:
    price = rental.calculate_price(cars[rental.car_id].price_per_day, cars[rental.car_id].price_per_km)
    commission = calculate_commissions(price, rental.duration)

    rentals_data.append({'id': rental.id, 'price': price, 'commission': commission})

output_data = {'rentals': rentals_data}

with open('data/output.json', 'w') as outfile:
    json.dump(output_data, outfile, indent=2)
