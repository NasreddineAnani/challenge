import json
from services.Deserializer import get_data_information
from services.Serializer import generate_rentals_data

with open('data/input.json') as json_file:
    data = json.load(json_file)
    cars, options, rentals = get_data_information(data)

rentals_data = generate_rentals_data(cars, options, rentals)

output_data = {'rentals': rentals_data}

with open('data/output.json', 'w') as outfile:
    json.dump(output_data, outfile, indent=2)
