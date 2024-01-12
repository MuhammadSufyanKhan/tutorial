import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_ohio_cities():
    url = "https://en.wikipedia.org/wiki/List_of_cities_in_Ohio"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    table = soup.find("table", {"class": "wikitable"})
    df = pd.read_html(str(table))[0]
    return df

def match_cities(user_input, city_data):
    user_input = user_input.lower().replace(" ", "").replace("\n", "")
    matched_cities = []

    for _, row in city_data.iterrows():
        city_name = row.get("City", "").lower().replace(" ", "")
        if city_name and city_name in user_input:
            matched_cities.append(row)

    return matched_cities

def main():
    print("Welcome to the Ohio City Matcher!\n")
    
    city_data = fetch_ohio_cities()

    print("Fetching Ohio cities with populations...\n")

    user_input = input("Please provide a list of cities (separated by commas, spaces, or line breaks), with or without spaces, numbering, or as a list:\n")
    
    matched_cities = match_cities(user_input, city_data)

    print("\nMatching cities...\n")
    print("Here are the matched cities along with their populations:\n")
    
    for city in matched_cities:
        city_name = city.get("City", "")
        population = city.get("Population", "")
        print(f"{city_name}: {population}")


    print("\nThank you for using the Ohio City Matcher!")

if __name__ == "__main__":
    main()
