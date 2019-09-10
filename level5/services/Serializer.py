from .Payment import get_actions


def generate_rentals_data(cars, options, rentals):
    rentals_data = []
    for rental in rentals:
        price = rental.calculate_price(cars[rental.car_id].price_per_day, cars[rental.car_id].price_per_km)
        commission = get_actions(price, rental.duration, rental.options)

        rentals_data.append({'id': rental.id, 'options': list(options.get(rental.id, [])), 'actions': commission})
    return rentals_data
