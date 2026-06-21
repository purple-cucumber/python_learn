from city_functions import city_data
def test_city_country():
    city_content = city_data('Santiago','Chile')
    assert city_content == 'Santiago,Chile'
def test_city_country_population():
    city_content = city_data('guangzhou','China','700000')
    assert city_content == 'guangzhou,China -population 700000'