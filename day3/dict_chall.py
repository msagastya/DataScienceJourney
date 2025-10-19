# Dictionary Challenge

country_capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon"

}
def get_capital(country):
    return country_capitals.get(country, "Capital not found")
def add_country(country, capital):
    country_capitals[country] = capital
def remove_country(country):
    if country in country_capitals:
        del country_capitals[country]
def list_countries():
    return list(country_capitals.keys())
def list_capitals():
    return list(country_capitals.values())
# Example usage:
print(get_capital("Germany"))  # Output: Berlin
add_country("Netherlands", "Amsterdam")
print(list_countries())  # Output: ['France', 'Germany', 'Italy', 'Spain', 'Portugal', 'Netherlands']
remove_country("Italy") 
print(list_countries())  # Output: ['France', 'Germany', 'Spain', 'Portugal', 'Netherlands']