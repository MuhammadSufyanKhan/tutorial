import requests
from bs4 import BeautifulSoup

def get_alabama_city_names():
    url = "https://www.alabama-demographics.com/cities_by_population"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    city_elements = soup.select(".cityTable tr td:nth-child(2)")

    city_names = [city.text.strip() for city in city_elements if city.text.strip()]
    return city_names

if __name__ == "__main__":
    print("Fetching Alabama city names from the web...")
    city_names = get_alabama_city_names()

    # Sort the city names
    sorted_cities = sorted(city_names)

    # Print the sorted cities on separate lines
    print("Sorted Alabama city names:")
    for city in sorted_cities:
        print(city)
