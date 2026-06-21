def city_data(City,Country,Population = None):
    if Population:
        n = f'{City},{Country} -population {Population}'
    else:
        n = f'{City},{Country}'
    return n