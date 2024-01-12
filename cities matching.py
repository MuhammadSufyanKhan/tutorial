def get_north_carolina_cities():
    with open('C:\Users\rizwan\Desktop\py\ nc_cities.txt', 'r') as file:
        nc_cities = [city.strip() for city in file.readlines()]
    return nc_cities

def find_matching_cities(user_input, nc_cities):
    user_input = user_input.lower()
    matching_cities = [city for city in nc_cities if user_input in city.lower()]
    return matching_cities

if __name__ == "__main__":
    nc_cities = get_north_carolina_cities()

    user_input = input("Enter a city name: ")
    
    # Find matching cities
    matching_cities = find_matching_cities(user_input, nc_cities)

    if matching_cities:
        print("Matching cities:")
        for i, city in enumerate(matching_cities, 1):
            print(f"{i}. {city}")
    else:
        print("No matching cities found.")
