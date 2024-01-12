import requests
from bs4 import BeautifulSoup

def fetch_north_carolina_cities():
    url = "https://www.geonames.org/US/NC/north-carolina.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    nc_cities = []

    city_table = soup.find("table", class_="restable")
    if city_table:
        city_rows = city_table.find_all("tr")[1:]  # Skip the header row
        for row in city_rows:
            city_cell = row.find("td", class_="name")
            if city_cell:
                city_name = city_cell.text.strip()
                nc_cities.append(city_name)

    return nc_cities

def save_to_file(city_list):
    with open("nc_cities.txt", "w") as file:
        for city in city_list:
            file.write(city + "\n")

if __name__ == "__main__":
    print("Fetching North Carolina city names from the web...")
    nc_cities_list = fetch_north_carolina_cities()

    if nc_cities_list:
        save_to_file(nc_cities_list)
        print("City names saved to nc_cities.txt.")
    else:
        print("No city names found for North Carolina.")
