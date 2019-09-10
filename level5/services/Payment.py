INSURANCE_FEE_RULE = 0.5
ASSISTANCE_FEE_RULE = 100
FEE_POURCENTAGE = 0.3

gps = ['gps', 500]
baby_seat = ['baby_seat', 200]
additional_insurance = ['additional_insurance', 1000]

driver = ['driver', 'debit', 0]
owner = ['owner', 'credit', 0]
insurance = ['insurance', 'credit', 0]
assistance = ['assistance', 'credit', 0]
drivy = ['drivy', 'credit', 0]

actors = [driver, owner, insurance, assistance, drivy]


def get_actions(price, duration, options):
    calculate_payments(price, duration, options)

    actions = []
    for actor in actors:
        actions.append({'who': actor[0], 'type': actor[1], 'amount': actor[2]})

    return actions


def calculate_payments(price, duration, options):
    owner[2] = int(price * 0.7)
    driver[2] = price

    fees = int(price * FEE_POURCENTAGE)

    insurance[2] = int(fees * INSURANCE_FEE_RULE)
    assistance[2] = duration * ASSISTANCE_FEE_RULE
    drivy[2] = fees - insurance[2] - assistance[2]
    add_options_payments(duration, options)


def add_options_payments(duration, options):
    if gps[0] in options:
        driver[2] += duration * gps[1]
        owner[2] += duration * gps[1]
    if baby_seat[0] in options:
        driver[2] += duration * baby_seat[1]
        owner[2] += duration * baby_seat[1]
    if additional_insurance[0] in options:
        driver[2] += duration * additional_insurance[1]
        drivy[2] += duration * additional_insurance[1]
