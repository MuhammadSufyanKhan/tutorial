import requests
import pandas as pd
from bs4 import BeautifulSoup

# Get the list of Ohio cities from Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_cities_in_Ohio"
response = requests.get(url)

# Parse the HTML response
soup = BeautifulSoup(response.content, "lxml")

# Find the first table on the page (you might need to adjust this based on the page structure)
table = soup.find("table", {"class": "wikitable"})

# Create lists to store data
city_names = []
populations = []

# Iterate through rows of the table
for row in table.find_all("tr"):
    cells = row.find_all(["th", "td"])

    if len(cells) >= 2:
        city_name = cells[0].text.strip()
        population = cells[2].text.strip()

        city_names.append(city_name)
        populations.append(population)

# Convert data to a pandas DataFrame
data = {"City": city_names, "Population": populations}
df = pd.DataFrame(data)

# Print the name and population of each city
for _, row in df.iterrows():
    city_name = row["City"]
    population = row["Population"]
    print(f"{city_name}: {population}")
