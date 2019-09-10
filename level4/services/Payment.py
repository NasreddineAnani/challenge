INSURANCE_FEE_RULE = 0.5
ASSISTANCE_FEE_RULE = 100
FEE_POURCENTAGE = 0.3

driver = ['driver', 'debit', 0]
owner = ['owner', 'credit', 0]
insurance = ['insurance', 'credit', 0]
assistance = ['assistance', 'credit', 0]
drivy = ['drivy', 'credit', 0]

actors = [driver, owner, insurance, assistance, drivy]


def get_actions(price, duration):
    calculate_payments(price, duration)

    actions = []
    for actor in actors:
        actions.append({'who': actor[0], 'type': actor[1], 'amount': actor[2]})

    return actions


def calculate_payments(price, duration):
    driver[2] = price
    owner[2] = int(price * 0.7)

    fees = int(price * FEE_POURCENTAGE)

    insurance[2] = int(fees * INSURANCE_FEE_RULE)
    assistance[2] = duration * ASSISTANCE_FEE_RULE
    drivy[2] = fees - insurance[2] - assistance[2]
