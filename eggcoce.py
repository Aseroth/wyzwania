code = input('Podaj kod z jaja:')

def egg_decode(code: str):
    method_code = int(code[0])
    method_type = None
    if method_code == 0:
        method_type = 'Organic'
    elif method_code == 1:
        method_type = 'Free range'
    elif method_code == 2:
        method_type = 'Barn'
    elif method_code == 3:
        method_type = 'Cage'

    country_code = str(code[1:3])
    country_code.lower()
    country = None
    if country_code == 'uk':
        country = 'United Kingdom'
    elif country_code == 'nl':
        country = 'Netherlands'
    elif country == 'fr':
        country = 'France'
    elif country == 'de':
        country = 'Germany'
    elif country == 'es':
        country = 'Spain'
    elif country == 'pl':
        country = 'Poland'

    farm_code = str(code[3:])
    decoded = f'Farming method: {method_type}, Country of origin: {country}, Farm ID: {farm_code}'

    return decoded


print(egg_decode(code))