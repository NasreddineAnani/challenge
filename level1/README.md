# Run code

I did the challenge with Python3 because I don't know ruby yet :)

You need to install the latest version of python (3.7 or above) 
and inside the levels folder run

``python3 Main.py``

# Intro

We are building a peer-to-peer car rental service. Let's call it Drivy :)

Here is our plan:

- Let any car owner list her car on our platform
- Let any person (let's call him 'driver') book a car for given dates/distance

# Level 1

The car owner chooses a price per day and price per km for her car.
The driver then books the car for a given period and an approximate distance.

The rental price is the sum of:

- A time component: the number of rental days multiplied by the car's price per day
- A distance component: the number of km multiplied by the car's price per km

