insurance_fee_rule = ('insurance_fee', .5)
assistance_fee_rule = ('assistance_fee', 100)
drivy_fee_rule = 'drivy_fee'


def calculate_commissions(price, duration):
    price = int(price * 0.3)
    insurance_fee = int(price * insurance_fee_rule[1])
    assistance_fee = duration * assistance_fee_rule[1]
    drivy_fee = price - insurance_fee - assistance_fee

    commissions = {insurance_fee_rule[0]: insurance_fee,
                   assistance_fee_rule[0]: assistance_fee,
                   drivy_fee_rule: drivy_fee}

    return commissions
