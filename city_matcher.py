def read_cities_from_file(C:\Users\rizwan\Desktop\py):
    with open(C:\Users\rizwan\Desktop\py, "r") as file:
        cities = file.read().splitlines()
    return cities

def find_matching_cities(user_input, cities):
    user_input = user_input.lower()
    matching_cities = [city for city in cities if user_input in city.lower()]
    return matching_cities

if __name__ == "__main__":
    file_path = "C:\Users\rizwan\Desktop\py"  # Replace with your file path if different
    nc_cities = read_cities_from_file(C:\Users\rizwan\Desktop\py)

    user_input = input("Enter a city name: ")
    
    # Find matching cities
    matching_cities = find_matching_cities(user_input, nc_cities)

    if matching_cities:
        print("Matching cities:")
        for i, city in enumerate(matching_cities, 1):
            print(f"{i}. {city}")
    else:
        print("No matching cities found.")
